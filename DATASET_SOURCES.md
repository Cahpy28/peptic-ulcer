# Legit Dataset Sources for PUDPredict

Use these sources to build a real labeled peptic ulcer disease dataset. Do not train the final model on random unlabeled data.

## 1. MIMIC-IV

Link: https://physionet.org/content/mimiciv/

Best use:
- Confirmed diagnosis labels from ICD-9/ICD-10 diagnosis tables.
- Medications, labs, admissions, demographics, procedures, and outcomes.

Useful PUD labels:
- ICD-10: K25 gastric ulcer, K26 duodenal ulcer, K27 peptic ulcer site unspecified, K28 gastrojejunal ulcer.
- ICD-9: 531 gastric ulcer, 532 duodenal ulcer, 533 peptic ulcer site unspecified, 534 gastrojejunal ulcer.

Recommended target columns:
- pud_positive
- ulcer_type
- diagnosis_code
- diagnosis_text
- complications

## 2. MIMIC-IV-ED

Link: https://physionet.org/content/mimic-iv-ed/

Best use:
- Emergency department diagnoses and medication reconciliation.
- Useful for symptom/risk-triage style modelling.

## 3. eICU Collaborative Research Database

Link: https://physionet.org/content/eicu-crd/

Best use:
- Multi-center ICU data with diagnoses, treatments, vitals, labs, medication and care information.
- Better for serious/complicated ulcer cases such as bleeding or critical illness.

## 4. NHANES

Link: https://wwwn.cdc.gov/nchs/nhanes/

Best use:
- Risk-factor enrichment, not final PUD diagnosis labels.
- Useful variables include alcohol use, smoking, analgesic/pain reliever use, prescription medication use, demographics, and health questionnaires.

## Suggested CSV Schema for This Project

```csv
age,gender,symptoms,nsaid_use,hpylori_status,smoking,alcohol,diagnosis,diagnosis_code,ulcer_type,pud_positive,medications,complications
```

## Training Warning

For accurate prediction, train only after you have confirmed labels. A valid positive label should come from ICD diagnosis, endoscopy report, clinician diagnosis, discharge diagnosis, or a validated clinical record. A valid negative label should come from records without PUD diagnosis and ideally with enough clinical information to avoid false negatives.

## VS Code Training Command

```powershell
cd "C:\Users\HP\Documents\PEPTIC ULCER DISEASE"
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py train_pud_model data\your_labeled_pud_dataset.csv
python manage.py runserver 8001
```

Use the demo file only to test the pipeline:

```powershell
python manage.py train_pud_model examples\pud_training_sample.csv
```

Do not use the demo file as your final clinical model. Replace it with approved MIMIC/eICU/hospital data containing confirmed outcomes.
