from pathlib import Path

from django.conf import settings

try:
    import joblib
    import pandas as pd
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder
    from xgboost import XGBClassifier
except ImportError:
    joblib = None
    pd = None
    ColumnTransformer = None
    SimpleImputer = None
    accuracy_score = None
    f1_score = None
    precision_score = None
    recall_score = None
    train_test_split = None
    Pipeline = None
    OneHotEncoder = None
    XGBClassifier = None


MODEL_PATH = Path(settings.BASE_DIR) / "models" / "pud_xgboost_pipeline.joblib"
METADATA_PATH = Path(settings.BASE_DIR) / "models" / "pud_xgboost_metadata.joblib"

FEATURE_COLUMNS = [
    "age",
    "gender",
    "symptoms",
    "nsaid_use",
    "hpylori_status",
    "smoking",
    "alcohol",
    "medications",
    "complications",
]
TARGET_COLUMN = "pud_positive"

COLUMN_ALIASES = {
    "age": ["age", "anchor_age", "patient_age"],
    "gender": ["gender", "sex"],
    "symptoms": ["symptoms", "chiefcomplaint", "chief_complaint", "clinical_notes", "presenting_symptoms"],
    "nsaid_use": ["nsaid_use", "nsaid", "nsaid_usage", "regular_nsaid_use"],
    "hpylori_status": ["hpylori_status", "h_pylori", "h_pylori_status", "helicobacter_pylori"],
    "smoking": ["smoking", "smoking_history", "tobacco"],
    "alcohol": ["alcohol", "alcohol_intake", "alcohol_use"],
    "diagnosis": ["diagnosis", "long_title", "icd_title", "diagnosis_text"],
    "diagnosis_code": ["diagnosis_code", "icd_code", "icd9_code", "icd10_code"],
    "ulcer_type": ["ulcer_type", "pud_type"],
    "pud_positive": ["pud_positive", "label", "target", "outcome", "has_pud"],
    "medications": ["medications", "medication", "drug", "drugs", "current_medications"],
    "complications": ["complications", "bleeding", "perforation", "obstruction"],
}

PUD_CODES = ("K25", "K26", "K27", "K28", "531", "532", "533", "534")
PUD_TERMS = ("peptic ulcer", "duodenal ulcer", "gastric ulcer", "gastrojejunal ulcer", "pud")
NEGATIVE_TERMS = ("no ulcer", "negative", "normal", "not positive")


def _require_training_dependencies():
    if not all([joblib, pd, ColumnTransformer, SimpleImputer, Pipeline, OneHotEncoder, XGBClassifier]):
        raise ImportError(
            "Training requires pandas, scikit-learn, xgboost, and joblib. "
            "Run: pip install -r requirements.txt"
        )


def _normalize_column_name(value):
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_").replace(".", "")


def _read_sources(paths):
    _require_training_dependencies()
    frames = []
    for path in paths:
        source_path = Path(path)
        if not source_path.exists():
            raise FileNotFoundError(f"Dataset not found: {source_path}")
        if source_path.suffix.lower() == ".csv":
            frame = pd.read_csv(source_path)
        elif source_path.suffix.lower() in {".parquet", ".pq"}:
            frame = pd.read_parquet(source_path)
        else:
            raise ValueError(f"Unsupported dataset format: {source_path.suffix}. Use CSV or Parquet.")
        frame["source_dataset"] = source_path.stem
        frames.append(frame)
    if not frames:
        raise ValueError("Provide at least one dataset path.")
    return pd.concat(frames, ignore_index=True)


def _standardize_columns(frame):
    normalized = {_normalize_column_name(col): col for col in frame.columns}
    output = pd.DataFrame(index=frame.index)
    for target, aliases in COLUMN_ALIASES.items():
        source = next((normalized.get(_normalize_column_name(alias)) for alias in aliases if _normalize_column_name(alias) in normalized), None)
        output[target] = frame[source] if source else ""
    return output


def _derive_labels(frame):
    diagnosis_text = (
        frame["diagnosis"].fillna("").astype(str)
        + " "
        + frame["diagnosis_code"].fillna("").astype(str)
        + " "
        + frame["ulcer_type"].fillna("").astype(str)
    ).str.lower()
    code_positive = frame["diagnosis_code"].fillna("").astype(str).str.upper().str.startswith(PUD_CODES)
    term_positive = diagnosis_text.apply(lambda value: any(term in value for term in PUD_TERMS))
    term_negative = diagnosis_text.apply(lambda value: any(term in value for term in NEGATIVE_TERMS))
    existing = pd.to_numeric(frame["pud_positive"], errors="coerce")
    derived = ((code_positive | term_positive) & ~term_negative).astype(int)
    frame["pud_positive"] = existing.fillna(derived).astype(int)
    return frame


def _prepare_frame(paths):
    raw = _read_sources(paths)
    frame = _standardize_columns(raw)
    frame = _derive_labels(frame)
    for column in FEATURE_COLUMNS:
        if column == "age":
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
        else:
            frame[column] = frame[column].fillna("unknown").astype(str).str.lower().str.strip()
    return frame


def train_pud_model(dataset_paths, output_path=MODEL_PATH):
    _require_training_dependencies()
    frame = _prepare_frame(dataset_paths)
    if frame[TARGET_COLUMN].nunique() < 2:
        raise ValueError("Training data needs both PUD-positive and PUD-negative confirmed outcomes.")

    X = frame[FEATURE_COLUMNS]
    y = frame[TARGET_COLUMN]
    stratify = y if y.value_counts().min() >= 2 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=stratify,
    )

    numeric_features = ["age"]
    categorical_features = [column for column in FEATURE_COLUMNS if column not in numeric_features]
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", SimpleImputer(strategy="median"), numeric_features),
            ("cat", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore")),
            ]), categorical_features),
        ]
    )
    model = XGBClassifier(
        n_estimators=220,
        max_depth=4,
        learning_rate=0.06,
        subsample=0.9,
        colsample_bytree=0.9,
        eval_metric="logloss",
        random_state=42,
    )
    pipeline = Pipeline([("preprocess", preprocessor), ("model", model)])
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
    probabilities = pipeline.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": round(accuracy_score(y_test, predictions), 4),
        "precision": round(precision_score(y_test, predictions, zero_division=0), 4),
        "recall": round(recall_score(y_test, predictions, zero_division=0), 4),
        "f1": round(f1_score(y_test, predictions, zero_division=0), 4),
        "rows": int(len(frame)),
        "positive_rows": int(y.sum()),
        "negative_rows": int((1 - y).sum()),
        "average_test_probability": round(float(probabilities.mean()), 4),
        "features": FEATURE_COLUMNS,
    }
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, output_path)
    joblib.dump(metrics, METADATA_PATH)
    return metrics


def predict_with_trained_model(data):
    if not MODEL_PATH.exists() or not all([joblib, pd]):
        return None
    pipeline = joblib.load(MODEL_PATH)
    row = pd.DataFrame([{
        "age": data.get("age"),
        "gender": data.get("gender", "unknown"),
        "symptoms": data.get("symptoms", "unknown"),
        "nsaid_use": data.get("nsaid_use", "unknown"),
        "hpylori_status": data.get("hpylori_status", "unknown"),
        "smoking": data.get("smoking_history", "unknown"),
        "alcohol": data.get("alcohol_intake", "unknown"),
        "medications": data.get("medications", "unknown"),
        "complications": data.get("complications", "unknown"),
    }])
    probability = float(pipeline.predict_proba(row)[0][1])
    label = int(probability >= 0.5)
    return {
        "risk_score": max(1, min(99, round(probability * 100))),
        "is_pud_positive": bool(label),
        "model_source": "trained_xgboost",
    }


def load_model_metadata():
    if METADATA_PATH.exists() and joblib:
        return joblib.load(METADATA_PATH)
    return None
