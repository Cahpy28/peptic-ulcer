import csv
import json
import re
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

REQUIRED_PUD_FIELDS = {
    "age": ["age", "patient_age"],
    "symptoms": ["symptoms", "clinical_notes", "presenting_symptoms"],
    "nsaid_use": ["nsaid_use", "nsaid", "nsaid_usage", "regular_nsaid_use"],
    "hpylori_status": ["h_pylori", "hpylori_status", "h_pylori_status", "helicobacter_pylori"],
    "smoking_alcohol": ["smoking", "smoking_history", "alcohol", "alcohol_intake"],
    "diagnosis": ["diagnosis", "ulcer_type", "outcome", "pud_status"],
    "medications": ["medications", "medicine", "drug", "drugs", "current_medications"],
    "complications": ["complications", "bleeding", "perforation", "obstruction"],
}

PUD_POSITIVE_TERMS = ["pud", "peptic ulcer", "gastric ulcer", "duodenal ulcer", "ulcer positive", "positive"]
PUD_NEGATIVE_TERMS = ["negative", "normal", "no ulcer", "not ulcer", "not positive"]


def normalize_column(name):
    return re.sub(r"[^a-z0-9]+", "_", str(name or "").strip().lower()).strip("_")


def detect_columns(columns):
    normalized = {normalize_column(col): col for col in columns}
    coverage = {}
    for field, aliases in REQUIRED_PUD_FIELDS.items():
        matches = [normalized[a] for a in aliases if a in normalized]
        if not matches and field == "smoking_alcohol":
            matches = [original for norm, original in normalized.items() if "smok" in norm or "alcohol" in norm]
        coverage[field] = matches
    return coverage


def process_pud_dataset_upload(upload):
    path = Path(upload.file.path)
    profile = {
        "required_fields": {},
        "diagnosis_distribution": {},
        "ulcer_type_distribution": {},
        "positive_rate": 0,
        "medication_frequency": {},
        "complication_frequency": {},
        "calibration": {},
    }
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = reader.fieldnames or []
            coverage = detect_columns(columns)
            profile["required_fields"] = coverage
            diagnosis_cols = coverage.get("diagnosis", [])
            medication_cols = coverage.get("medications", [])
            complication_cols = coverage.get("complications", [])
            diagnosis_counter = Counter()
            ulcer_type_counter = Counter()
            medication_counter = Counter()
            complication_counter = Counter()
            factor_hits = defaultdict(lambda: {"total": 0, "positive": 0})
            row_count = 0
            positive_count = 0
            for row in reader:
                row_count += 1
                diagnosis_text = " ".join(str(row.get(col, "")) for col in diagnosis_cols).lower()
                is_negative = any(term in diagnosis_text for term in PUD_NEGATIVE_TERMS)
                is_positive = any(term in diagnosis_text for term in PUD_POSITIVE_TERMS) and not is_negative
                if is_positive:
                    positive_count += 1
                diagnosis_counter.update([diagnosis_text.strip() or "unknown"])
                if "duoden" in diagnosis_text:
                    ulcer_type_counter.update(["Duodenal Ulcer"])
                elif "gastric" in diagnosis_text or "stomach" in diagnosis_text:
                    ulcer_type_counter.update(["Gastric Ulcer"])
                elif is_negative:
                    ulcer_type_counter.update(["No active PUD indicated"])
                elif is_positive:
                    ulcer_type_counter.update(["Peptic Ulcer Disease"])
                for col in medication_cols:
                    for item in re.split(r"[,;/]", str(row.get(col, ""))):
                        item = item.strip().lower()
                        if item:
                            medication_counter.update([item])
                for col in complication_cols:
                    for item in re.split(r"[,;/]", str(row.get(col, ""))):
                        item = item.strip().lower()
                        if item:
                            complication_counter.update([item])
                for field, cols in coverage.items():
                    if field in {"diagnosis", "medications", "complications"}:
                        continue
                    value = " ".join(str(row.get(col, "")) for col in cols).lower()
                    if value:
                        factor_hits[field]["total"] += 1
                        if is_positive:
                            factor_hits[field]["positive"] += 1
            profile["diagnosis_distribution"] = dict(diagnosis_counter.most_common(10))
            profile["ulcer_type_distribution"] = dict(ulcer_type_counter.most_common(8))
            profile["positive_rate"] = round((positive_count / row_count) * 100, 1) if row_count else 0
            profile["medication_frequency"] = dict(medication_counter.most_common(12))
            profile["complication_frequency"] = dict(complication_counter.most_common(12))
            profile["calibration"] = {
                field: round((values["positive"] / max(values["total"], 1)) * 100, 1)
                for field, values in factor_hits.items()
            }
            upload.row_count = row_count
            upload.column_profile = profile
            upload.status = "processed"
            upload.message = "Dataset processed. Required field coverage and calibration profile are available."
    except Exception as exc:
        upload.status = "failed"
        upload.message = f"Dataset could not be processed: {exc}"
    upload.save(update_fields=["row_count", "column_profile", "status", "message"])
    return upload


def fetch_pubmed_references(query="peptic ulcer disease guidelines H pylori NSAID", limit=5):
    encoded = urllib.parse.urlencode({"db": "pubmed", "term": query, "retmode": "json", "retmax": limit})
    search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{encoded}"
    try:
        with urllib.request.urlopen(search_url, timeout=5) as response:
            ids = json.loads(response.read().decode("utf-8"))["esearchresult"].get("idlist", [])
        if not ids:
            return []
        summary_query = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(ids), "retmode": "json"})
        summary_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?{summary_query}"
        with urllib.request.urlopen(summary_url, timeout=5) as response:
            payload = json.loads(response.read().decode("utf-8"))
        refs = []
        for pmid in ids:
            item = payload.get("result", {}).get(pmid, {})
            if item:
                refs.append({
                    "source": "PubMed",
                    "title": item.get("title", "PubMed reference"),
                    "published": item.get("pubdate", ""),
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                })
        return refs
    except Exception:
        return [
            {"source": "Guidance", "title": "H. pylori testing and NSAID exposure are key evidence-based ulcer risk considerations.", "published": "fallback", "url": "https://pubmed.ncbi.nlm.nih.gov/"}
        ]


def fetch_openfda_warnings(medications):
    warnings = []
    meds = [m.strip() for m in re.split(r"[,;\n]", medications or "") if m.strip()]
    for med in meds[:6]:
        query = urllib.parse.urlencode({"search": f'openfda.brand_name:"{med}" OR openfda.generic_name:"{med}"', "limit": 1})
        url = f"https://api.fda.gov/drug/label.json?{query}"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                payload = json.loads(response.read().decode("utf-8"))
            result = (payload.get("results") or [{}])[0]
            warning_text = " ".join((result.get("warnings") or result.get("boxed_warning") or result.get("precautions") or [""])[:1])
            if warning_text:
                warnings.append({"medication": med, "warning": warning_text[:650], "source_url": "https://open.fda.gov/apis/drug/label/"})
        except Exception:
            if med.lower() in {"ibuprofen", "naproxen", "diclofenac", "aspirin", "nsaid"}:
                warnings.append({"medication": med, "warning": "NSAIDs can increase gastrointestinal irritation, ulceration, and bleeding risk. Review use with a healthcare professional.", "source_url": "https://open.fda.gov/apis/drug/label/"})
    return warnings
