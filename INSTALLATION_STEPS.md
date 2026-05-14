# PUDPredict Installation And VS Code Setup

## 1. Project Location

Open this folder in VS Code:

```text
C:\Users\HP\Documents\Codex\2026-05-08\files-mentioned-by-the-user-layer
```

In VS Code:

```text
File > Open Folder > files-mentioned-by-the-user-layer
```

## 2. Correct Project Arrangement

Your VS Code Explorer should look like this:

```text
files-mentioned-by-the-user-layer/
+-- manage.py
+-- requirements.txt
+-- pyproject.toml
+-- README.md
+-- INSTALLATION_STEPS.md
+-- SYSTEM_DESIGN.md
+-- .env.example
+-- database_schema.sql
+-- styles.css
+-- data/
+-- examples/
+-- models/
+-- reports/
+-- assets/
|   +-- layer-flow.png
|   +-- patient-data-processing.png
|   +-- pud-prediction-context.png
|   +-- pud-use-cases.png
+-- js/
|   +-- app.js
+-- src/
|   +-- ulcerboost/
|       +-- api.py
|       +-- model.py
|       +-- storage.py
|       +-- static/
|           +-- index.html
|           +-- styles.css
|           +-- app.js
|           +-- assets/
+-- pudpredict/
|   +-- __init__.py
|   +-- settings.py
|   +-- urls.py
|   +-- asgi.py
|   +-- wsgi.py
+-- patients/
|   +-- admin.py
|   +-- apps.py
|   +-- forms.py
|   +-- ml.py
|   +-- models.py
|   +-- urls.py
|   +-- views.py
|   +-- migrations/
|   +-- templatetags/
+-- templates/
    +-- patients/
    +-- registration/
+-- tests/
```

## 3. Create Virtual Environment

Open VS Code terminal:

```text
Terminal > New Terminal
```

Run:

```powershell
cd "C:\Users\HP\Documents\Codex\2026-05-08\files-mentioned-by-the-user-layer"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If `py` is not available, use:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 4. Install Requirements

```powershell
pip install -r requirements.txt
```

## 5. Run With SQLite First

SQLite is the easiest setup and works without MySQL.

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

Useful pages:

```text
Landing Page:       http://127.0.0.1:8000/
Register:           http://127.0.0.1:8000/register/
Login:              http://127.0.0.1:8000/accounts/login/
Dashboard:          http://127.0.0.1:8000/dashboard/
New Assessment:     http://127.0.0.1:8000/assessment/
Patient History:    http://127.0.0.1:8000/patients/
Reports:            http://127.0.0.1:8000/reports/
AI Advisor:         http://127.0.0.1:8000/chatbot/
Admin:              http://127.0.0.1:8000/admin/
```

## 6. Optional MySQL Setup

Only use this if MySQL is installed.

Create a `.env` file by copying `.env.example`, then set:

```text
USE_MYSQL=True
MYSQL_DATABASE=pudpredict_db
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

In MySQL:

```sql
CREATE DATABASE pudpredict_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Then run:

```powershell
python manage.py migrate
python manage.py runserver
```

## 7. Preview The Static Landing Page Without Django

You can preview the landing design immediately by opening:

```text
C:\Users\HP\Documents\Codex\2026-05-08\files-mentioned-by-the-user-layer\index.html
```

The full functioning Django website should be previewed through:

```text
http://127.0.0.1:8000
```

## 8. Optional Package-Style Preview

This matches the `src/ulcerboost` layout:

```powershell
python -m ulcerboost.api
```

If Python cannot find the package, run:

```powershell
$env:PYTHONPATH="src"
python -m ulcerboost.api
```

Then open:

```text
http://127.0.0.1:8080
```
