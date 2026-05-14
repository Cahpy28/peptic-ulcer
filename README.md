# PUDPredict

Professional Django backend for an Intelligent Peptic Ulcer Disease Management System.

## Features

- Professional landing page
- Patient data entry form for clinical parameters
- XGBoost-based prediction simulated through a model-like scoring layer
- Patient history review
- Prediction results and recommendations
- Report generation and export
- Secure patient dashboard
- Email verification before dashboard access
- Symptom tracking over time
- AI chatbot for non-diagnostic lifestyle and PUD management guidance

## Folder Structure

This project now includes both:

- a full Django website (`manage.py`, `pudpredict/`, `patients/`, `templates/`)
- a clean package-style layout (`src/ulcerboost/`) matching the requested arrangement

See `SYSTEM_DESIGN.md` and `INSTALLATION_STEPS.md`.

## Run Locally

Install dependencies:

```powershell
pip install -r requirements.txt
```

Use SQLite by default:

```powershell
python manage.py migrate
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

For exact VS Code arrangement and terminal commands, see `INSTALLATION_STEPS.md`.

Create a patient account at:

```text
http://127.0.0.1:8000/register/
```

During local development, account verification emails print in the VS Code terminal.
Copy the verification link from the terminal and open it in your browser to activate the account.

To use SMTP instead, set these values in `.env`:

```text
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=PUDPredict <your_email@example.com>
EMAIL_VERIFICATION_MAX_AGE=86400
```

## Optional MySQL

Create `.env` from `.env.example`, then set:

```text
USE_MYSQL=True
MYSQL_DATABASE=pudpredict_db
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

Create the MySQL database first:

```sql
CREATE DATABASE pudpredict_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Then run:

```powershell
python manage.py migrate
python manage.py runserver
```

## Important Clinical Note

The chatbot and prediction output are educational decision-support features only.
They must not be used as a final diagnosis or emergency triage tool.

## Train a Real XGBoost Model

Place your approved labeled CSV or Parquet export in the `data` folder. Required useful fields are:

```text
age, gender, symptoms, nsaid_use, hpylori_status, smoking, alcohol, diagnosis, diagnosis_code, ulcer_type, pud_positive, medications, complications
```

Train from VS Code terminal:

```powershell
python manage.py train_pud_model data\your_labeled_pud_dataset.csv
```

The trained model is saved at:

```text
models\pud_xgboost_pipeline.joblib
```

After that file exists, the Django assessment form automatically uses the trained model for risk scoring. MIMIC-IV, MIMIC-IV-ED, and eICU can provide confirmed diagnosis labels through ICD codes. NHANES should only enrich risk factors unless you add confirmed PUD outcome labels from another source.

The AI Advisor uses retrieval-based guidance: the user question is matched against the approved PUD knowledge base, then the answer is generated only from those approved topics plus the patient’s stored risk context.
