from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
PATIENT_STORE = DATA_DIR / "patients.json"


def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_patients():
    ensure_data_dir()
    if not PATIENT_STORE.exists():
        return []
    return json.loads(PATIENT_STORE.read_text(encoding="utf-8"))


def save_patient(record):
    patients = load_patients()
    patients.insert(0, record)
    PATIENT_STORE.write_text(json.dumps(patients, indent=2), encoding="utf-8")
    return record
