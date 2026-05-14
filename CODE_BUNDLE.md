# PUDPredict Full Code Bundle

This file contains the text code files arranged for the project. Binary images are included in the project folder and zip under assets/.

## Project Tree
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
+-- patients/
+-- templates/
+-- tests/
```

## manage.py
`$lang
#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pudpredict.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django is not installed. Install dependencies with: pip install -r requirements.txt"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
```

## requirements.txt
`$lang
Django>=5.0,<6.0
PyMySQL>=1.1.0
python-dotenv>=1.0.0
```

## pyproject.toml
`$lang
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "ulcerboost"
version = "0.1.0"
description = "Peptic ulcer disease risk assessment and management prototype"
requires-python = ">=3.10"
dependencies = [
  "Django>=5.0,<6.0",
  "PyMySQL>=1.1.0",
  "python-dotenv>=1.0.0"
]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

## README.md
`$lang
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
```

## INSTALLATION_STEPS.md
`$lang
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
```

## SYSTEM_DESIGN.md
`$lang
# UlcerBoost System Design

## Purpose

UlcerBoost is an intelligent peptic ulcer disease management prototype. It captures patient clinical parameters, estimates risk through a simulated Gradient Boosting model, tracks symptom history, generates reports, and offers non-diagnostic lifestyle guidance.

## Folder Layout

```text
your-project-folder/
+-- data/
+-- examples/
+-- models/
+-- reports/
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
+-- tests/
+-- requirements.txt
+-- pyproject.toml
+-- README.md
+-- SYSTEM_DESIGN.md
```

## Main Components

- `src/ulcerboost/api.py`: lightweight local preview API and static file server.
- `src/ulcerboost/model.py`: simulated Gradient Boosting / XGBoost prediction logic.
- `src/ulcerboost/storage.py`: simple JSON storage for local preview data.
- `src/ulcerboost/static/`: professional PUDPredict landing page and UI assets.
- `patients/` and `pudpredict/`: full Django implementation for the functioning web app.

## Data Flow

1. User enters clinical information.
2. System validates the submitted fields.
3. Model layer computes risk score, severity, and recommendations.
4. Result is stored and displayed in dashboard/report views.
5. AI advisor gives educational, non-diagnostic guidance based on severity and history.

## Safety Boundary

The prediction and chatbot output are educational decision-support features. They are not a medical diagnosis, emergency triage tool, or replacement for clinician assessment.
```

## .env.example
`$lang
SECRET_KEY=replace-this-with-a-secure-django-secret-key
DEBUG=True
USE_MYSQL=False
MYSQL_DATABASE=pudpredict_db
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

## database_schema.sql
`$lang
CREATE DATABASE IF NOT EXISTS pudpredict_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pudpredict_db;

-- Django creates the final tables through migrations.
-- Run after installing dependencies:
-- python manage.py migrate
```

## styles.css
`$lang
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap");

:root {
  --ink: #111827;
  --muted: #64748b;
  --line: #dbe4ef;
  --surface: #ffffff;
  --soft: #f8fafc;
  --brand: #2563eb;
  --brand-dark: #1d4ed8;
  --accent: #2dd4bf;
  --danger: #c04444;
  --success: #24895a;
  --shadow: 0 24px 70px rgba(37, 99, 235, 0.12);
  --radius: 18px;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  color: var(--ink);
  background: #fff;
  font-family: "Poppins", Arial, sans-serif;
  letter-spacing: 0;
}

a {
  color: inherit;
  text-decoration: none;
}

img {
  display: block;
  max-width: 100%;
}

button,
input,
select,
textarea {
  font: inherit;
}

html {
  scroll-behavior: smooth;
}

body.app-bg {
  background: #f8fafc;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  border-bottom: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(18px);
}

.nav-shell {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: min(1180px, calc(100% - 32px));
  margin: 0 auto;
  min-height: 76px;
  gap: 24px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: max-content;
  font-size: 1.02rem;
  font-weight: 800;
}

.brand-mark {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  color: #fff;
  border-radius: 14px;
  background: var(--brand);
  box-shadow: 0 12px 28px rgba(37, 99, 235, 0.22);
}

.brand span:last-child {
  display: block;
  line-height: 1;
}

.brand-blue {
  color: var(--brand);
}

.nav-links {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 6px;
  flex-wrap: wrap;
}

.nav-links a {
  padding: 10px 12px;
  border-radius: 12px;
  color: var(--muted);
  font-size: 0.98rem;
  font-weight: 600;
}

.nav-links a:hover,
.nav-links a.active {
  color: var(--brand);
  background: #eef4ff;
}

.nav-links .nav-cta {
  min-width: 128px;
  color: #fff;
  text-align: center;
  background: var(--brand);
  box-shadow: 0 10px 20px rgba(37, 99, 235, 0.24);
}

.nav-links .nav-cta:hover,
.nav-links .nav-cta.active {
  color: #fff;
  background: var(--brand-dark);
}

.page {
  width: min(1180px, calc(100% - 32px));
  margin: 0 auto;
}

.reveal {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity 700ms ease, transform 700ms ease;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

.hero {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1.02fr) minmax(360px, 0.98fr);
  align-items: center;
  gap: 56px;
  min-height: calc(100vh - 76px);
  padding: 64px 0 42px;
}

.hero::after {
  content: "";
  position: absolute;
  inset: 0 calc(50% - 50vw) 0 50%;
  z-index: -1;
  background:
    radial-gradient(circle at 30% 20%, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0) 35%),
    linear-gradient(135deg, #f8fbff 0%, #dcecf9 100%);
}

.hero-copy {
  max-width: 640px;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 30px;
  padding: 9px 18px;
  color: var(--brand);
  background: #e8effd;
  border: 0;
  border-radius: 999px;
  font-size: 1rem;
  font-weight: 500;
  text-transform: none;
}

h1,
h2,
h3,
p {
  margin-top: 0;
}

h1 {
  margin-bottom: 20px;
  font-size: clamp(3.1rem, 6.6vw, 5.7rem);
  line-height: 1;
  letter-spacing: 0;
}

.text-blue {
  color: var(--brand);
}

h2 {
  margin-bottom: 14px;
  font-size: clamp(1.8rem, 3vw, 2.9rem);
  line-height: 1.1;
}

h3 {
  margin-bottom: 8px;
  font-size: 1.08rem;
}

.lead {
  color: var(--muted);
  font-size: 1.28rem;
  line-height: 1.65;
}

.hero-actions,
.button-row {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 28px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  min-height: 48px;
  padding: 12px 20px;
  border: 1px solid transparent;
  border-radius: 14px;
  color: #fff;
  background: var(--brand);
  font-weight: 700;
  cursor: pointer;
  transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
}

.btn.loading,
button.loading {
  opacity: 0.68;
  pointer-events: none;
}

.btn:hover {
  transform: translateY(-1px);
  background: var(--brand-dark);
  box-shadow: 0 14px 24px rgba(37, 99, 235, 0.18);
}

.btn.secondary {
  color: var(--ink);
  background: #fff;
  border-color: var(--line);
}

.btn.secondary:hover {
  background: #f7fafc;
  box-shadow: 0 12px 22px rgba(16, 32, 51, 0.08);
}

.btn.warning {
  background: var(--accent);
}

.hero-panel {
  position: relative;
}

.dashboard-preview {
  overflow: hidden;
  border: 0;
  border-radius: 28px;
  background: #fff;
  box-shadow: 0 30px 90px rgba(15, 23, 42, 0.1);
}

.preview-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 46px 48px 24px;
  border-bottom: 1px solid var(--line);
  justify-content: flex-start;
  gap: 16px;
}

.preview-title {
  font-weight: 800;
  font-size: 1.18rem;
}

.preview-subtitle {
  display: block;
  color: var(--muted);
  font-weight: 500;
  margin-top: 4px;
}

.preview-icon {
  display: grid;
  place-items: center;
  width: 62px;
  height: 62px;
  color: var(--brand);
  border-radius: 18px;
  background: #e8effd;
}

.status-dot {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: var(--success);
  font-size: 0.82rem;
  font-weight: 700;
}

.status-dot::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--success);
}

.preview-body {
  display: block;
  padding: 26px 48px 36px;
}

.metric {
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: #fbfdfe;
}

.metric span {
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
}

.metric strong {
  display: block;
  margin-top: 8px;
  font-size: 1.85rem;
}

.risk-gauge {
  padding: 0;
  border: 0;
  border-radius: 0;
  background: #fff;
}

.gauge-track {
  height: 13px;
  overflow: hidden;
  border-radius: 999px;
  background: #e8eef3;
}

.gauge-fill {
  width: var(--value, 72%);
  height: 100%;
  background: var(--bar-color, var(--brand));
}

.bar-row {
  display: grid;
  gap: 8px;
  margin-bottom: 18px;
}

.bar-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #53667f;
  font-size: 0.95rem;
  font-weight: 600;
}

.bar-label strong {
  color: #020617;
}

.patient-strip {
  display: grid;
  gap: 10px;
  margin-top: 16px;
}

.patient-row {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 12px 0;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 0.9rem;
}

.patient-row strong {
  color: var(--ink);
}

.section {
  padding: 86px 0;
}

.app-title-row {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  padding: 56px 0 36px;
}

.app-title-row h1 {
  margin-bottom: 8px;
  font-size: clamp(2rem, 4vw, 2.8rem);
}

.app-title-row .lead {
  margin-bottom: 0;
  font-size: 1.08rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.stat-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 116px;
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
}

.stat-card span {
  display: block;
  color: #60748e;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.stat-card strong {
  display: block;
  margin-top: 8px;
  font-size: 2rem;
}

.stat-icon {
  display: grid;
  place-items: center;
  width: 66px;
  height: 66px;
  border-radius: 18px;
}

.stat-icon.blue {
  color: #2563eb;
  background: #e8effd;
}

.stat-icon.green {
  color: #20c7b5;
  background: #e0faf6;
}

.stat-icon.red {
  color: #ef4444;
  background: #fee8e8;
}

.stat-icon.purple {
  color: #8b5cf6;
  background: #f0e7ff;
}

.section-heading {
  display: block;
  max-width: 860px;
  margin: 0 auto 64px;
  text-align: center;
}

.section-heading p {
  max-width: 760px;
  margin: 0 auto;
  color: var(--muted);
  line-height: 1.6;
  font-size: 1.25rem;
}

.section-kicker {
  margin: 0 0 18px;
  color: var(--brand) !important;
  font-size: 1rem !important;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.grid-3,
.grid-2,
.grid-4 {
  display: grid;
  gap: 18px;
}

.grid-3 {
  grid-template-columns: repeat(3, 1fr);
}

.grid-2 {
  grid-template-columns: repeat(2, 1fr);
}

.grid-4 {
  grid-template-columns: repeat(4, 1fr);
}

.card,
.form-card,
.table-card {
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--surface);
  box-shadow: none;
}

.card {
  padding: 42px;
  min-height: 260px;
}

.card-icon {
  display: grid;
  place-items: center;
  width: 72px;
  height: 72px;
  margin-bottom: 34px;
  color: var(--brand);
  border-radius: 18px;
  background: #e8effd;
}

.card p,
.muted {
  color: var(--muted);
  line-height: 1.65;
}

.workflow {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 34px;
  text-align: center;
}

.step {
  position: relative;
  padding: 0;
  border: 0;
  border-radius: 0;
  background: #fff;
}

.step::after {
  content: "";
  position: absolute;
  top: 60px;
  left: calc(50% + 60px);
  width: calc(100% - 52px);
  border-top: 3px dashed #e2e8f0;
}

.step:last-child::after {
  display: none;
}

.step-icon {
  position: relative;
  display: grid;
  place-items: center;
  width: 120px;
  height: 120px;
  margin: 0 auto 34px;
  color: var(--brand);
  border-radius: 22px;
  background: #e8effd;
}

.step-number {
  position: absolute;
  top: -12px;
  right: -12px;
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  color: #fff;
  border-radius: 50%;
  background: var(--brand);
  font-weight: 800;
}

.step strong {
  display: block;
  margin-bottom: 14px;
  font-size: 1.25rem;
}

.step span {
  color: var(--muted);
  font-size: 1rem;
  line-height: 1.55;
}

.page-hero {
  padding: 62px 0 32px;
  text-align: center;
}

.page-hero .lead {
  margin-left: auto;
  margin-right: auto;
  max-width: 780px;
}

.form-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 22px;
  align-items: start;
  padding-bottom: 72px;
}

.form-card {
  padding: 24px;
}

.assessment-card {
  max-width: 940px;
  margin: 0 auto;
}

.form-section-title {
  margin: 28px 0 18px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--line);
  font-size: 1.05rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.form-section-title:first-child {
  margin-top: 0;
}

.condition-field {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 54px;
  padding: 10px 18px;
  border-radius: 16px;
  background: #f8fafc;
}

.condition-field label {
  color: #020617;
  font-size: 1rem;
}

.condition-field select {
  width: 132px;
  min-height: 38px;
  border-radius: 999px;
  color: var(--brand);
  background-color: #eef4ff;
  font-weight: 700;
}

.field-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.field {
  display: grid;
  gap: 7px;
}

.field.full {
  grid-column: span 2;
}

label {
  color: #33475b;
  font-size: 0.86rem;
  font-weight: 700;
}

input,
select,
textarea {
  width: 100%;
  min-height: 44px;
  padding: 10px 12px;
  color: var(--ink);
  border: 1px solid #cfd9e2;
  border-radius: 14px;
  background: #fff;
  outline: none;
  box-shadow: 0 2px 10px rgba(15, 23, 42, 0.03);
}

select.input-control {
  cursor: pointer;
}

.field:has(select) select {
  appearance: none;
  background-image:
    linear-gradient(45deg, transparent 50%, #64748b 50%),
    linear-gradient(135deg, #64748b 50%, transparent 50%);
  background-position:
    calc(100% - 18px) 50%,
    calc(100% - 13px) 50%;
  background-size: 5px 5px, 5px 5px;
  background-repeat: no-repeat;
}

textarea {
  min-height: 108px;
  resize: vertical;
}

input:focus,
select:focus,
textarea:focus {
  border-color: var(--brand);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.12);
}

.result-panel {
  position: sticky;
  top: 98px;
  padding: 26px;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: #fff;
  box-shadow: var(--shadow);
}

.score-ring {
  display: grid;
  place-items: center;
  width: 180px;
  height: 180px;
  margin: 20px auto;
  border-radius: 50%;
  background: conic-gradient(var(--brand) 0deg, var(--brand) 155deg, #e8eef3 155deg 360deg);
}

.score-ring-inner {
  display: grid;
  place-items: center;
  width: 132px;
  height: 132px;
  border-radius: 50%;
  background: #fff;
  text-align: center;
}

.score-ring strong {
  display: block;
  font-size: 2.2rem;
}

.recommendations {
  display: grid;
  gap: 10px;
  margin-top: 18px;
}

.recommendations li {
  color: var(--muted);
  line-height: 1.6;
}

.table-card {
  overflow: hidden;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 15px 16px;
  border-bottom: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}

th {
  color: #42566d;
  background: #f5f8fb;
  font-size: 0.82rem;
  text-transform: uppercase;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 5px 9px;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 800;
}

.badge.low {
  color: #176543;
  background: #e5f6ee;
}

.badge.medium {
  color: #8a590b;
  background: #fff0d6;
}

.badge.high {
  color: #9d2f2f;
  background: #ffe7e7;
}

.diagram-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  padding-bottom: 72px;
}

.diagram-card {
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: #fff;
  box-shadow: 0 14px 32px rgba(16, 32, 51, 0.06);
}

.diagram-card.wide {
  grid-column: span 2;
}

.diagram-card img {
  width: 100%;
  height: 360px;
  object-fit: contain;
  padding: 18px;
  background: #fff;
}

.diagram-card.wide img {
  height: 420px;
}

.diagram-caption {
  padding: 18px 20px;
  border-top: 1px solid var(--line);
}

.report-shell {
  display: grid;
  grid-template-columns: 0.85fr 1.15fr;
  gap: 22px;
  padding-bottom: 72px;
}

.report-preview {
  padding: 28px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: #fff;
  box-shadow: var(--shadow);
}

.report-preview header {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  padding-bottom: 16px;
  border-bottom: 2px solid var(--ink);
}

.report-preview section {
  padding: 18px 0;
  border-bottom: 1px solid var(--line);
}

.footer {
  padding: 32px 0 42px;
  color: var(--muted);
  border-top: 1px solid var(--line);
  background: #fff;
}

.empty-state {
  display: grid;
  place-items: center;
  min-height: 220px;
  color: #cbd5e1;
}

.footer .page {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

@media (max-width: 980px) {
  .hero,
  .form-grid,
  .report-shell {
    grid-template-columns: 1fr;
  }

  .hero {
    min-height: auto;
  }

  .hero::after {
    inset: 46% calc(50% - 50vw) 0 calc(50% - 50vw);
  }

  .grid-3,
  .grid-4,
  .stats-grid,
  .workflow,
  .diagram-grid {
    grid-template-columns: 1fr 1fr;
  }

  .step::after {
    display: none;
  }

  .result-panel {
    position: static;
  }
}

@media (max-width: 680px) {
  .nav-shell {
    align-items: flex-start;
    flex-direction: column;
    padding: 14px 0;
  }

  h1 {
    font-size: clamp(2.7rem, 15vw, 4.2rem);
  }

  .nav-links {
    justify-content: flex-start;
  }

  .app-title-row {
    align-items: flex-start;
    flex-direction: column;
  }

  .hero {
    padding-top: 36px;
  }

  .preview-body,
  .field-grid,
  .grid-2,
  .grid-3,
  .grid-4,
  .stats-grid,
  .workflow,
  .diagram-grid {
    grid-template-columns: 1fr;
  }

  .risk-gauge,
  .field.full,
  .diagram-card.wide {
    grid-column: span 1;
  }

  .section-heading {
    display: block;
  }

  th,
  td {
    padding: 12px;
    font-size: 0.88rem;
  }
}
```

## js/app.js
`$lang
const assessmentForm = document.querySelector("[data-assessment-form]");
const reportForm = document.querySelector("[data-report-form]");
const API_BASE = location.protocol === "file:" ? "http://127.0.0.1:8000" : "";

const samples = [
  {
    id: "PUD-2401",
    name: "Amina Yusuf",
    age: 42,
    risk: 78,
    severity: "High",
    symptoms: "Burning epigastric pain, melena alert, NSAID use",
    recommendation: "Urgent clinician review, stop NSAIDs where appropriate, H. pylori test, PPI plan",
    recommendations: ["Urgent clinician review, stop NSAIDs where appropriate, H. pylori test, PPI plan"]
  },
  {
    id: "PUD-2402",
    name: "Chinedu Okafor",
    age: 35,
    risk: 52,
    severity: "Medium",
    symptoms: "Nocturnal discomfort, nausea, high stress pattern",
    recommendation: "Schedule review, evaluate H. pylori, dietary counseling, monitor symptoms",
    recommendations: ["Schedule review, evaluate H. pylori, dietary counseling, monitor symptoms"]
  },
  {
    id: "PUD-2403",
    name: "Grace Mensah",
    age: 29,
    risk: 24,
    severity: "Low",
    symptoms: "Intermittent dyspepsia, no alarm symptoms",
    recommendation: "Lifestyle guidance, symptom tracking, routine follow-up if persistent",
    recommendations: ["Lifestyle guidance, symptom tracking, routine follow-up if persistent"]
  }
];

let assessmentCache = [];

function setActiveNav() {
  const current = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((link) => {
    const href = link.getAttribute("href");
    const match = link.getAttribute("data-nav-match");
    link.classList.toggle(
      "active",
      href === current ||
      (current === "" && href === "index.html") ||
      (match && location.pathname.includes(match))
    );
  });
}

function initUiEffects() {
  document.body.classList.toggle("app-bg", !document.querySelector(".hero"));

  const revealItems = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("visible"));
  }

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  document.querySelectorAll("[data-loading-form]").forEach((form) => {
    form.addEventListener("submit", () => {
      const button = form.querySelector("button[type='submit']");
      if (button) {
        button.classList.add("loading");
        button.innerHTML = "Processing...";
      }
    });
  });
}

function severityFromScore(score) {
  if (score >= 70) return "High";
  if (score >= 40) return "Medium";
  return "Low";
}

function badgeClass(severity) {
  return String(severity || "low").toLowerCase();
}

function computeRisk(data) {
  let score = 8;
  score += Number(data.age || 0) > 55 ? 12 : Number(data.age || 0) > 40 ? 7 : 2;
  score += Number(data.pain || 0) * 6;
  score += data.nsaid === "yes" ? 15 : data.nsaid === "sometimes" ? 8 : 0;
  score += data.hpylori === "positive" ? 18 : data.hpylori === "unknown" ? 8 : 0;
  score += data.bleeding === "yes" ? 20 : 0;
  score += data.smoking === "yes" ? 8 : 0;
  score += data.alcohol === "high" ? 8 : data.alcohol === "moderate" ? 4 : 0;
  score += data.stress === "high" ? 7 : data.stress === "moderate" ? 3 : 0;
  return Math.max(3, Math.min(96, Math.round(score)));
}

function recommendationsFor(severity, data) {
  const list = [];
  if (severity === "High") {
    list.push("Prioritize clinician review and screen immediately for alarm symptoms or bleeding.");
    list.push("Run H. pylori confirmation where status is unknown and document medication history.");
    list.push("Generate a structured report for gastroenterology referral or urgent review.");
  } else if (severity === "Medium") {
    list.push("Schedule follow-up assessment and track pain frequency, triggers, and response to therapy.");
    list.push("Recommend H. pylori testing if not recently confirmed.");
    list.push("Review NSAID exposure, diet, alcohol use, smoking, and stress contributors.");
  } else {
    list.push("Provide lifestyle guidance and symptom monitoring with routine reassessment.");
    list.push("Escalate if pain worsens, vomiting occurs, weight loss appears, or bleeding is suspected.");
    list.push("Keep baseline patient record for future model comparison.");
  }

  if (data.nsaid === "yes") list.push("Flag frequent NSAID use as a modifiable ulcer risk factor.");
  if (data.bleeding === "yes") list.push("Bleeding symptoms require urgent medical evaluation.");
  return list;
}

async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options
  });
  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.error || "Backend request failed.");
  }
  return payload;
}

function readLocalAssessments() {
  const saved = JSON.parse(localStorage.getItem("pudAssessments") || "[]");
  return saved.length ? saved : samples;
}

async function loadAssessments() {
  try {
    const payload = await apiRequest("/api/patients");
    assessmentCache = payload.patients.length ? payload.patients : samples;
  } catch (error) {
    assessmentCache = readLocalAssessments();
  }
  return assessmentCache;
}

function saveLocalAssessment(record) {
  const existing = JSON.parse(localStorage.getItem("pudAssessments") || "[]");
  existing.unshift(record);
  localStorage.setItem("pudAssessments", JSON.stringify(existing.slice(0, 20)));
}

function updateResult(score, severity, recommendations) {
  const scoreText = document.querySelector("[data-score]");
  const severityText = document.querySelector("[data-severity]");
  const ring = document.querySelector("[data-score-ring]");
  const recommendationList = document.querySelector("[data-recommendations]");
  if (!scoreText || !severityText || !ring || !recommendationList) return;

  scoreText.textContent = `${score}%`;
  severityText.textContent = `${severity} Risk`;
  const degrees = Math.round((score / 100) * 360);
  const color = severity === "High" ? "#c04444" : severity === "Medium" ? "#f2a03a" : "#24895a";
  ring.style.background = `conic-gradient(${color} 0deg, ${color} ${degrees}deg, #e8eef3 ${degrees}deg 360deg)`;
  recommendationList.innerHTML = recommendations.map((item) => `<li>${item}</li>`).join("");
}

function renderPatientTable(items = assessmentCache) {
  const body = document.querySelector("[data-patient-table]");
  if (!body) return;
  body.innerHTML = items.map((item) => `
    <tr>
      <td><strong>${item.id}</strong><br><span class="muted">${item.name}</span></td>
      <td>${item.age}</td>
      <td>${item.symptoms}</td>
      <td><span class="badge ${badgeClass(item.severity)}">${item.severity}</span></td>
      <td>${item.risk}%</td>
    </tr>
  `).join("");
}

function renderPredictionCards(items = assessmentCache) {
  const target = document.querySelector("[data-prediction-cards]");
  if (!target) return;
  target.innerHTML = items.slice(0, 6).map((item) => `
    <article class="card">
      <div class="card-icon"><i data-lucide="activity"></i></div>
      <h3>${item.name}</h3>
      <p><strong>${item.risk}% ${item.severity} risk</strong></p>
      <p>${item.recommendation}</p>
    </article>
  `).join("");
  if (window.lucide) window.lucide.createIcons();
}

function normalizeRecommendations(item) {
  if (Array.isArray(item.recommendations)) return item.recommendations;
  if (item.recommendations_json) {
    try {
      return JSON.parse(item.recommendations_json);
    } catch (error) {
      return [item.recommendation];
    }
  }
  return [item.recommendation];
}

function renderReportPreview(record) {
  const target = document.querySelector("[data-report-preview]");
  if (!target) return;
  const item = record || assessmentCache[0] || samples[0];
  const recommendations = normalizeRecommendations(item);
  target.innerHTML = `
    <header>
      <div>
        <h3>Intelligent PUD Management Report</h3>
        <p class="muted">Extreme Gradient Algorithm assessment summary</p>
      </div>
      <strong>${item.id}</strong>
    </header>
    <section>
      <h3>Patient</h3>
      <p>${item.name}, ${item.age} years</p>
    </section>
    <section>
      <h3>Prediction</h3>
      <p><span class="badge ${badgeClass(item.severity)}">${item.severity}</span> ${item.risk}% estimated PUD management risk</p>
    </section>
    <section>
      <h3>Clinical Notes</h3>
      <p>${item.symptoms}</p>
    </section>
    <section>
      <h3>Recommendations</h3>
      <ul class="recommendations">${recommendations.map((text) => `<li>${text}</li>`).join("")}</ul>
    </section>
  `;
}

function populateReportOptions(items = assessmentCache) {
  const select = document.querySelector("[data-report-patient]");
  if (!select) return;
  select.innerHTML = items.map((item) => `<option value="${item.id}">${item.id} - ${item.name}</option>`).join("");
}

async function createAssessment(formData) {
  try {
    const payload = await apiRequest("/api/assessments", {
      method: "POST",
      body: JSON.stringify(formData)
    });
    return payload.assessment;
  } catch (error) {
    const score = computeRisk(formData);
    const severity = severityFromScore(score);
    const recommendations = recommendationsFor(severity, formData);
    const record = {
      id: `PUD-${Date.now().toString().slice(-5)}`,
      name: formData.name || "New Patient",
      age: formData.age || "N/A",
      risk: score,
      severity,
      symptoms: formData.symptoms || "New assessment captured from clinical input.",
      recommendation: recommendations[0],
      recommendations
    };
    saveLocalAssessment(record);
    return record;
  }
}

if (assessmentForm) {
  assessmentForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = Object.fromEntries(new FormData(assessmentForm).entries());
    const submitButton = assessmentForm.querySelector("button[type='submit']");
    if (submitButton) submitButton.disabled = true;

    try {
      const record = await createAssessment(formData);
      updateResult(record.risk, record.severity, normalizeRecommendations(record));
      assessmentCache.unshift(record);
    } finally {
      if (submitButton) submitButton.disabled = false;
    }
  });
}

if (reportForm) {
  reportForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(reportForm).entries());
    let record = assessmentCache.find((item) => item.id === data.patient);

    try {
      const payload = await apiRequest(`/api/reports/${data.patient}`);
      record = payload.report;
    } catch (error) {
      record = record || assessmentCache[0];
    }
    renderReportPreview(record);
  });
}

async function boot() {
  setActiveNav();
  initUiEffects();
  const assessments = await loadAssessments();
  renderPatientTable(assessments);
  renderPredictionCards(assessments);
  populateReportOptions(assessments);
  renderReportPreview(assessments[0]);

  if (window.lucide) {
    window.lucide.createIcons();
  }
}

boot();
```

## src/ulcerboost/__init__.py
`$lang
"""UlcerBoost package for PUDPredict clinical decision-support prototype."""

__all__ = ["model", "storage"]
```

## src/ulcerboost/api.py
`$lang
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import time

from ulcerboost.model import predict_ulcer_risk
from ulcerboost.storage import save_patient, load_patients


STATIC_DIR = Path(__file__).resolve().parent / "static"
HOST = "127.0.0.1"
PORT = 8080


class UlcerBoostHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/patients":
            self.send_json({"patients": load_patients()})
            return
        if self.path == "/api/health":
            self.send_json({"status": "ok", "app": "UlcerBoost"})
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/predict":
            self.send_json({"error": "Endpoint not found."}, status=404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        payload = self.rfile.read(length).decode("utf-8") if length else "{}"
        features = json.loads(payload)
        prediction = predict_ulcer_risk(features)
        record = {
            "id": f"PUD-{str(int(time.time() * 1000))[-6:]}",
            "name": features.get("name", "New Patient"),
            "age": features.get("age"),
            **prediction,
        }
        save_patient(record)
        self.send_json({"prediction": record}, status=201)

    def send_json(self, payload, status=200):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    server = ThreadingHTTPServer((HOST, PORT), UlcerBoostHandler)
    print(f"UlcerBoost preview running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
```

## src/ulcerboost/model.py
`$lang
def severity_from_score(score):
    if score >= 70:
        return "High"
    if score >= 40:
        return "Medium"
    return "Low"


def predict_ulcer_risk(features):
    """Simulated Gradient Boosting predictor for peptic ulcer risk.

    This keeps the same input/output shape expected from a real XGBoost model.
    Replace this function with a loaded model from `models/` when training is ready.
    """
    age = int(features.get("age") or 0)
    pain = int(features.get("pain_severity") or features.get("pain") or 0)
    score = 8
    score += 12 if age > 55 else 7 if age > 40 else 2
    score += pain * 6
    score += 18 if features.get("hpylori_status") == "positive" else 8 if features.get("hpylori_status") == "unknown" else 0
    score += 15 if features.get("nsaid_use") == "yes" else 8 if features.get("nsaid_use") == "sometimes" else 0
    score += 20 if features.get("bleeding_symptoms") == "yes" else 0
    score += 8 if features.get("smoking_history") == "yes" else 0
    score += 8 if features.get("alcohol_intake") == "high" else 4 if features.get("alcohol_intake") == "moderate" else 0
    score += 7 if features.get("stress_level") == "high" else 3 if features.get("stress_level") == "moderate" else 0
    risk_score = max(3, min(96, round(score)))
    severity = severity_from_score(risk_score)
    return {
        "risk_score": risk_score,
        "severity": severity,
        "recommendations": recommendations_for(severity, features),
    }


def recommendations_for(severity, features):
    if severity == "High":
        tips = [
            "Prioritize clinician review and screen for alarm symptoms.",
            "Confirm H. pylori status and document medication history.",
            "Generate a report for gastroenterology or senior clinical review.",
        ]
    elif severity == "Medium":
        tips = [
            "Schedule follow-up assessment and monitor symptom pattern.",
            "Review NSAID exposure, stress, diet, alcohol, and smoking factors.",
            "Consider H. pylori testing if status is unknown.",
        ]
    else:
        tips = [
            "Provide lifestyle guidance and symptom tracking.",
            "Escalate care if symptoms persist or alarm symptoms appear.",
            "Keep baseline history for future risk comparison.",
        ]
    if features.get("bleeding_symptoms") == "yes":
        tips.insert(0, "Bleeding symptoms require urgent medical evaluation.")
    return tips
```

## src/ulcerboost/storage.py
`$lang
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
```

## src/ulcerboost/static/index.html
`$lang
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PUDPredict | Intelligent PUD Management System</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header">
    <nav class="nav-shell">
      <a class="brand" href="index.html">
        <span class="brand-mark"><i data-lucide="activity"></i></span>
        <span>PUD<span class="brand-blue">Predict</span></span>
      </a>
      <div class="nav-links">
        <a href="#features">Features</a>
        <a class="nav-cta" href="assessment.html">Open App</a>
      </div>
    </nav>
  </header>

  <main class="page">
    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow"><i data-lucide="brain"></i> Powered by XGBoost Algorithm</p>
        <h1>Intelligent <span class="text-blue">Peptic Ulcer</span> Disease Management</h1>
        <p class="lead">Leverage the power of Extreme Gradient Boosting (XGBoost) for accurate peptic ulcer disease risk assessment, prediction, and clinical decision support.</p>
        <div class="hero-actions">
          <a class="btn" href="assessment.html"><i data-lucide="clipboard-plus"></i> Start Assessment</a>
          <a class="btn secondary" href="architecture.html"><i data-lucide="network"></i> View System Flow</a>
        </div>
      </div>
      <div class="hero-panel">
        <div class="dashboard-preview">
          <div class="preview-top">
            <span class="preview-icon"><i data-lucide="bar-chart-3"></i></span>
            <span>
              <span class="preview-title">Risk Assessment</span>
              <span class="preview-subtitle">XGBoost Prediction Model</span>
            </span>
          </div>
          <div class="preview-body">
            <div class="risk-gauge">
              <div class="bar-row">
                <div class="bar-label"><span>H. pylori Status</span><strong>87%</strong></div>
                <div class="gauge-track"><div class="gauge-fill" style="--value:87%;--bar-color:#2563eb"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-label"><span>NSAID Usage</span><strong>72%</strong></div>
                <div class="gauge-track"><div class="gauge-fill" style="--value:72%;--bar-color:#2dd4bf"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-label"><span>Smoking History</span><strong>65%</strong></div>
                <div class="gauge-track"><div class="gauge-fill" style="--value:65%;--bar-color:#7c3aed"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-label"><span>Stress Level</span><strong>58%</strong></div>
                <div class="gauge-track"><div class="gauge-fill" style="--value:58%;--bar-color:#eabf52"></div></div>
              </div>
              <div class="bar-row">
                <div class="bar-label"><span>Diet Pattern</span><strong>43%</strong></div>
                <div class="gauge-track"><div class="gauge-fill" style="--value:43%;--bar-color:#ef4444"></div></div>
              </div>
              <div class="patient-row"><strong>Overall Risk</strong><span class="badge high">78%</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="features">
      <div class="section-heading">
        <h2>Comprehensive PUD Management</h2>
        <p>A full-featured intelligent system for peptic ulcer disease assessment, prediction, and clinical decision support.</p>
      </div>
      <div class="grid-3">
        <article class="card">
          <div class="card-icon"><i data-lucide="brain"></i></div>
          <h3>XGBoost Prediction</h3>
          <p>Advanced Extreme Gradient Boosting algorithm for accurate peptic ulcer disease risk assessment and classification.</p>
        </article>
        <article class="card">
          <div class="card-icon"><i data-lucide="stethoscope"></i></div>
          <h3>Clinical Data Input</h3>
          <p>Comprehensive patient data collection including symptoms, lab results, lifestyle factors, and medical history.</p>
        </article>
        <article class="card">
          <div class="card-icon"><i data-lucide="bar-chart-3"></i></div>
          <h3>Risk Visualization</h3>
          <p>Interactive charts displaying feature importance, risk scores, and contributing factors for each prediction.</p>
        </article>
      </div>
    </section>

    <section class="section workflow-section">
      <div class="section-heading">
        <p class="section-kicker">SYSTEM WORKFLOW</p>
        <h2>How It Works</h2>
        <p>A streamlined process from data entry to prediction and clinical recommendations.</p>
      </div>
      <div class="workflow">
        <div class="step">
          <div class="step-icon"><i data-lucide="user-plus"></i><span class="step-number">01</span></div>
          <strong>User Logs In</strong><span>Clinicians and authorized users securely access the system.</span>
        </div>
        <div class="step">
          <div class="step-icon"><i data-lucide="clipboard-list"></i><span class="step-number">02</span></div>
          <strong>Enter Patient Data</strong><span>Input comprehensive clinical data including symptoms and risk factors.</span>
        </div>
        <div class="step">
          <div class="step-icon"><i data-lucide="cpu"></i><span class="step-number">03</span></div>
          <strong>XGBoost Prediction</strong><span>The system validates data and generates a risk prediction.</span>
        </div>
        <div class="step">
          <div class="step-icon"><i data-lucide="file-bar-chart"></i><span class="step-number">04</span></div>
          <strong>Results & Reports</strong><span>View predictions, clinical recommendations, and export reports.</span>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="page">
      <span>PUDPredict</span>
      <span>Clinical decision support prototype</span>
    </div>
  </footer>
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
```

## src/ulcerboost/static/styles.css
`$lang
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap");

:root {
  --ink: #111827;
  --muted: #64748b;
  --line: #dbe4ef;
  --surface: #ffffff;
  --soft: #f8fafc;
  --brand: #2563eb;
  --brand-dark: #1d4ed8;
  --accent: #2dd4bf;
  --danger: #c04444;
  --success: #24895a;
  --shadow: 0 24px 70px rgba(37, 99, 235, 0.12);
  --radius: 18px;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  color: var(--ink);
  background: #fff;
  font-family: "Poppins", Arial, sans-serif;
  letter-spacing: 0;
}

a {
  color: inherit;
  text-decoration: none;
}

img {
  display: block;
  max-width: 100%;
}

button,
input,
select,
textarea {
  font: inherit;
}

html {
  scroll-behavior: smooth;
}

body.app-bg {
  background: #f8fafc;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  border-bottom: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(18px);
}

.nav-shell {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: min(1180px, calc(100% - 32px));
  margin: 0 auto;
  min-height: 76px;
  gap: 24px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: max-content;
  font-size: 1.02rem;
  font-weight: 800;
}

.brand-mark {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  color: #fff;
  border-radius: 14px;
  background: var(--brand);
  box-shadow: 0 12px 28px rgba(37, 99, 235, 0.22);
}

.brand span:last-child {
  display: block;
  line-height: 1;
}

.brand-blue {
  color: var(--brand);
}

.nav-links {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 6px;
  flex-wrap: wrap;
}

.nav-links a {
  padding: 10px 12px;
  border-radius: 12px;
  color: var(--muted);
  font-size: 0.98rem;
  font-weight: 600;
}

.nav-links a:hover,
.nav-links a.active {
  color: var(--brand);
  background: #eef4ff;
}

.nav-links .nav-cta {
  min-width: 128px;
  color: #fff;
  text-align: center;
  background: var(--brand);
  box-shadow: 0 10px 20px rgba(37, 99, 235, 0.24);
}

.nav-links .nav-cta:hover,
.nav-links .nav-cta.active {
  color: #fff;
  background: var(--brand-dark);
}

.page {
  width: min(1180px, calc(100% - 32px));
  margin: 0 auto;
}

.reveal {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity 700ms ease, transform 700ms ease;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

.hero {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1.02fr) minmax(360px, 0.98fr);
  align-items: center;
  gap: 56px;
  min-height: calc(100vh - 76px);
  padding: 64px 0 42px;
}

.hero::after {
  content: "";
  position: absolute;
  inset: 0 calc(50% - 50vw) 0 50%;
  z-index: -1;
  background:
    radial-gradient(circle at 30% 20%, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0) 35%),
    linear-gradient(135deg, #f8fbff 0%, #dcecf9 100%);
}

.hero-copy {
  max-width: 640px;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 30px;
  padding: 9px 18px;
  color: var(--brand);
  background: #e8effd;
  border: 0;
  border-radius: 999px;
  font-size: 1rem;
  font-weight: 500;
  text-transform: none;
}

h1,
h2,
h3,
p {
  margin-top: 0;
}

h1 {
  margin-bottom: 20px;
  font-size: clamp(3.1rem, 6.6vw, 5.7rem);
  line-height: 1;
  letter-spacing: 0;
}

.text-blue {
  color: var(--brand);
}

h2 {
  margin-bottom: 14px;
  font-size: clamp(1.8rem, 3vw, 2.9rem);
  line-height: 1.1;
}

h3 {
  margin-bottom: 8px;
  font-size: 1.08rem;
}

.lead {
  color: var(--muted);
  font-size: 1.28rem;
  line-height: 1.65;
}

.hero-actions,
.button-row {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 28px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  min-height: 48px;
  padding: 12px 20px;
  border: 1px solid transparent;
  border-radius: 14px;
  color: #fff;
  background: var(--brand);
  font-weight: 700;
  cursor: pointer;
  transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
}

.btn.loading,
button.loading {
  opacity: 0.68;
  pointer-events: none;
}

.btn:hover {
  transform: translateY(-1px);
  background: var(--brand-dark);
  box-shadow: 0 14px 24px rgba(37, 99, 235, 0.18);
}

.btn.secondary {
  color: var(--ink);
  background: #fff;
  border-color: var(--line);
}

.btn.secondary:hover {
  background: #f7fafc;
  box-shadow: 0 12px 22px rgba(16, 32, 51, 0.08);
}

.btn.warning {
  background: var(--accent);
}

.hero-panel {
  position: relative;
}

.dashboard-preview {
  overflow: hidden;
  border: 0;
  border-radius: 28px;
  background: #fff;
  box-shadow: 0 30px 90px rgba(15, 23, 42, 0.1);
}

.preview-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 46px 48px 24px;
  border-bottom: 1px solid var(--line);
  justify-content: flex-start;
  gap: 16px;
}

.preview-title {
  font-weight: 800;
  font-size: 1.18rem;
}

.preview-subtitle {
  display: block;
  color: var(--muted);
  font-weight: 500;
  margin-top: 4px;
}

.preview-icon {
  display: grid;
  place-items: center;
  width: 62px;
  height: 62px;
  color: var(--brand);
  border-radius: 18px;
  background: #e8effd;
}

.status-dot {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: var(--success);
  font-size: 0.82rem;
  font-weight: 700;
}

.status-dot::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--success);
}

.preview-body {
  display: block;
  padding: 26px 48px 36px;
}

.metric {
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: #fbfdfe;
}

.metric span {
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
}

.metric strong {
  display: block;
  margin-top: 8px;
  font-size: 1.85rem;
}

.risk-gauge {
  padding: 0;
  border: 0;
  border-radius: 0;
  background: #fff;
}

.gauge-track {
  height: 13px;
  overflow: hidden;
  border-radius: 999px;
  background: #e8eef3;
}

.gauge-fill {
  width: var(--value, 72%);
  height: 100%;
  background: var(--bar-color, var(--brand));
}

.bar-row {
  display: grid;
  gap: 8px;
  margin-bottom: 18px;
}

.bar-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #53667f;
  font-size: 0.95rem;
  font-weight: 600;
}

.bar-label strong {
  color: #020617;
}

.patient-strip {
  display: grid;
  gap: 10px;
  margin-top: 16px;
}

.patient-row {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 12px 0;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 0.9rem;
}

.patient-row strong {
  color: var(--ink);
}

.section {
  padding: 86px 0;
}

.app-title-row {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  padding: 56px 0 36px;
}

.app-title-row h1 {
  margin-bottom: 8px;
  font-size: clamp(2rem, 4vw, 2.8rem);
}

.app-title-row .lead {
  margin-bottom: 0;
  font-size: 1.08rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.stat-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 116px;
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
}

.stat-card span {
  display: block;
  color: #60748e;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.stat-card strong {
  display: block;
  margin-top: 8px;
  font-size: 2rem;
}

.stat-icon {
  display: grid;
  place-items: center;
  width: 66px;
  height: 66px;
  border-radius: 18px;
}

.stat-icon.blue {
  color: #2563eb;
  background: #e8effd;
}

.stat-icon.green {
  color: #20c7b5;
  background: #e0faf6;
}

.stat-icon.red {
  color: #ef4444;
  background: #fee8e8;
}

.stat-icon.purple {
  color: #8b5cf6;
  background: #f0e7ff;
}

.section-heading {
  display: block;
  max-width: 860px;
  margin: 0 auto 64px;
  text-align: center;
}

.section-heading p {
  max-width: 760px;
  margin: 0 auto;
  color: var(--muted);
  line-height: 1.6;
  font-size: 1.25rem;
}

.section-kicker {
  margin: 0 0 18px;
  color: var(--brand) !important;
  font-size: 1rem !important;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.grid-3,
.grid-2,
.grid-4 {
  display: grid;
  gap: 18px;
}

.grid-3 {
  grid-template-columns: repeat(3, 1fr);
}

.grid-2 {
  grid-template-columns: repeat(2, 1fr);
}

.grid-4 {
  grid-template-columns: repeat(4, 1fr);
}

.card,
.form-card,
.table-card {
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--surface);
  box-shadow: none;
}

.card {
  padding: 42px;
  min-height: 260px;
}

.card-icon {
  display: grid;
  place-items: center;
  width: 72px;
  height: 72px;
  margin-bottom: 34px;
  color: var(--brand);
  border-radius: 18px;
  background: #e8effd;
}

.card p,
.muted {
  color: var(--muted);
  line-height: 1.65;
}

.workflow {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 34px;
  text-align: center;
}

.step {
  position: relative;
  padding: 0;
  border: 0;
  border-radius: 0;
  background: #fff;
}

.step::after {
  content: "";
  position: absolute;
  top: 60px;
  left: calc(50% + 60px);
  width: calc(100% - 52px);
  border-top: 3px dashed #e2e8f0;
}

.step:last-child::after {
  display: none;
}

.step-icon {
  position: relative;
  display: grid;
  place-items: center;
  width: 120px;
  height: 120px;
  margin: 0 auto 34px;
  color: var(--brand);
  border-radius: 22px;
  background: #e8effd;
}

.step-number {
  position: absolute;
  top: -12px;
  right: -12px;
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  color: #fff;
  border-radius: 50%;
  background: var(--brand);
  font-weight: 800;
}

.step strong {
  display: block;
  margin-bottom: 14px;
  font-size: 1.25rem;
}

.step span {
  color: var(--muted);
  font-size: 1rem;
  line-height: 1.55;
}

.page-hero {
  padding: 62px 0 32px;
  text-align: center;
}

.page-hero .lead {
  margin-left: auto;
  margin-right: auto;
  max-width: 780px;
}

.form-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 22px;
  align-items: start;
  padding-bottom: 72px;
}

.form-card {
  padding: 24px;
}

.assessment-card {
  max-width: 940px;
  margin: 0 auto;
}

.form-section-title {
  margin: 28px 0 18px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--line);
  font-size: 1.05rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.form-section-title:first-child {
  margin-top: 0;
}

.condition-field {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 54px;
  padding: 10px 18px;
  border-radius: 16px;
  background: #f8fafc;
}

.condition-field label {
  color: #020617;
  font-size: 1rem;
}

.condition-field select {
  width: 132px;
  min-height: 38px;
  border-radius: 999px;
  color: var(--brand);
  background-color: #eef4ff;
  font-weight: 700;
}

.field-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.field {
  display: grid;
  gap: 7px;
}

.field.full {
  grid-column: span 2;
}

label {
  color: #33475b;
  font-size: 0.86rem;
  font-weight: 700;
}

input,
select,
textarea {
  width: 100%;
  min-height: 44px;
  padding: 10px 12px;
  color: var(--ink);
  border: 1px solid #cfd9e2;
  border-radius: 14px;
  background: #fff;
  outline: none;
  box-shadow: 0 2px 10px rgba(15, 23, 42, 0.03);
}

select.input-control {
  cursor: pointer;
}

.field:has(select) select {
  appearance: none;
  background-image:
    linear-gradient(45deg, transparent 50%, #64748b 50%),
    linear-gradient(135deg, #64748b 50%, transparent 50%);
  background-position:
    calc(100% - 18px) 50%,
    calc(100% - 13px) 50%;
  background-size: 5px 5px, 5px 5px;
  background-repeat: no-repeat;
}

textarea {
  min-height: 108px;
  resize: vertical;
}

input:focus,
select:focus,
textarea:focus {
  border-color: var(--brand);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.12);
}

.result-panel {
  position: sticky;
  top: 98px;
  padding: 26px;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: #fff;
  box-shadow: var(--shadow);
}

.score-ring {
  display: grid;
  place-items: center;
  width: 180px;
  height: 180px;
  margin: 20px auto;
  border-radius: 50%;
  background: conic-gradient(var(--brand) 0deg, var(--brand) 155deg, #e8eef3 155deg 360deg);
}

.score-ring-inner {
  display: grid;
  place-items: center;
  width: 132px;
  height: 132px;
  border-radius: 50%;
  background: #fff;
  text-align: center;
}

.score-ring strong {
  display: block;
  font-size: 2.2rem;
}

.recommendations {
  display: grid;
  gap: 10px;
  margin-top: 18px;
}

.recommendations li {
  color: var(--muted);
  line-height: 1.6;
}

.table-card {
  overflow: hidden;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 15px 16px;
  border-bottom: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}

th {
  color: #42566d;
  background: #f5f8fb;
  font-size: 0.82rem;
  text-transform: uppercase;
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 5px 9px;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 800;
}

.badge.low {
  color: #176543;
  background: #e5f6ee;
}

.badge.medium {
  color: #8a590b;
  background: #fff0d6;
}

.badge.high {
  color: #9d2f2f;
  background: #ffe7e7;
}

.diagram-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  padding-bottom: 72px;
}

.diagram-card {
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: #fff;
  box-shadow: 0 14px 32px rgba(16, 32, 51, 0.06);
}

.diagram-card.wide {
  grid-column: span 2;
}

.diagram-card img {
  width: 100%;
  height: 360px;
  object-fit: contain;
  padding: 18px;
  background: #fff;
}

.diagram-card.wide img {
  height: 420px;
}

.diagram-caption {
  padding: 18px 20px;
  border-top: 1px solid var(--line);
}

.report-shell {
  display: grid;
  grid-template-columns: 0.85fr 1.15fr;
  gap: 22px;
  padding-bottom: 72px;
}

.report-preview {
  padding: 28px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: #fff;
  box-shadow: var(--shadow);
}

.report-preview header {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  padding-bottom: 16px;
  border-bottom: 2px solid var(--ink);
}

.report-preview section {
  padding: 18px 0;
  border-bottom: 1px solid var(--line);
}

.footer {
  padding: 32px 0 42px;
  color: var(--muted);
  border-top: 1px solid var(--line);
  background: #fff;
}

.empty-state {
  display: grid;
  place-items: center;
  min-height: 220px;
  color: #cbd5e1;
}

.footer .page {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

@media (max-width: 980px) {
  .hero,
  .form-grid,
  .report-shell {
    grid-template-columns: 1fr;
  }

  .hero {
    min-height: auto;
  }

  .hero::after {
    inset: 46% calc(50% - 50vw) 0 calc(50% - 50vw);
  }

  .grid-3,
  .grid-4,
  .stats-grid,
  .workflow,
  .diagram-grid {
    grid-template-columns: 1fr 1fr;
  }

  .step::after {
    display: none;
  }

  .result-panel {
    position: static;
  }
}

@media (max-width: 680px) {
  .nav-shell {
    align-items: flex-start;
    flex-direction: column;
    padding: 14px 0;
  }

  h1 {
    font-size: clamp(2.7rem, 15vw, 4.2rem);
  }

  .nav-links {
    justify-content: flex-start;
  }

  .app-title-row {
    align-items: flex-start;
    flex-direction: column;
  }

  .hero {
    padding-top: 36px;
  }

  .preview-body,
  .field-grid,
  .grid-2,
  .grid-3,
  .grid-4,
  .stats-grid,
  .workflow,
  .diagram-grid {
    grid-template-columns: 1fr;
  }

  .risk-gauge,
  .field.full,
  .diagram-card.wide {
    grid-column: span 1;
  }

  .section-heading {
    display: block;
  }

  th,
  td {
    padding: 12px;
    font-size: 0.88rem;
  }
}
```

## src/ulcerboost/static/app.js
`$lang
const assessmentForm = document.querySelector("[data-assessment-form]");
const reportForm = document.querySelector("[data-report-form]");
const API_BASE = location.protocol === "file:" ? "http://127.0.0.1:8000" : "";

const samples = [
  {
    id: "PUD-2401",
    name: "Amina Yusuf",
    age: 42,
    risk: 78,
    severity: "High",
    symptoms: "Burning epigastric pain, melena alert, NSAID use",
    recommendation: "Urgent clinician review, stop NSAIDs where appropriate, H. pylori test, PPI plan",
    recommendations: ["Urgent clinician review, stop NSAIDs where appropriate, H. pylori test, PPI plan"]
  },
  {
    id: "PUD-2402",
    name: "Chinedu Okafor",
    age: 35,
    risk: 52,
    severity: "Medium",
    symptoms: "Nocturnal discomfort, nausea, high stress pattern",
    recommendation: "Schedule review, evaluate H. pylori, dietary counseling, monitor symptoms",
    recommendations: ["Schedule review, evaluate H. pylori, dietary counseling, monitor symptoms"]
  },
  {
    id: "PUD-2403",
    name: "Grace Mensah",
    age: 29,
    risk: 24,
    severity: "Low",
    symptoms: "Intermittent dyspepsia, no alarm symptoms",
    recommendation: "Lifestyle guidance, symptom tracking, routine follow-up if persistent",
    recommendations: ["Lifestyle guidance, symptom tracking, routine follow-up if persistent"]
  }
];

let assessmentCache = [];

function setActiveNav() {
  const current = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((link) => {
    const href = link.getAttribute("href");
    const match = link.getAttribute("data-nav-match");
    link.classList.toggle(
      "active",
      href === current ||
      (current === "" && href === "index.html") ||
      (match && location.pathname.includes(match))
    );
  });
}

function initUiEffects() {
  document.body.classList.toggle("app-bg", !document.querySelector(".hero"));

  const revealItems = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("visible"));
  }

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  document.querySelectorAll("[data-loading-form]").forEach((form) => {
    form.addEventListener("submit", () => {
      const button = form.querySelector("button[type='submit']");
      if (button) {
        button.classList.add("loading");
        button.innerHTML = "Processing...";
      }
    });
  });
}

function severityFromScore(score) {
  if (score >= 70) return "High";
  if (score >= 40) return "Medium";
  return "Low";
}

function badgeClass(severity) {
  return String(severity || "low").toLowerCase();
}

function computeRisk(data) {
  let score = 8;
  score += Number(data.age || 0) > 55 ? 12 : Number(data.age || 0) > 40 ? 7 : 2;
  score += Number(data.pain || 0) * 6;
  score += data.nsaid === "yes" ? 15 : data.nsaid === "sometimes" ? 8 : 0;
  score += data.hpylori === "positive" ? 18 : data.hpylori === "unknown" ? 8 : 0;
  score += data.bleeding === "yes" ? 20 : 0;
  score += data.smoking === "yes" ? 8 : 0;
  score += data.alcohol === "high" ? 8 : data.alcohol === "moderate" ? 4 : 0;
  score += data.stress === "high" ? 7 : data.stress === "moderate" ? 3 : 0;
  return Math.max(3, Math.min(96, Math.round(score)));
}

function recommendationsFor(severity, data) {
  const list = [];
  if (severity === "High") {
    list.push("Prioritize clinician review and screen immediately for alarm symptoms or bleeding.");
    list.push("Run H. pylori confirmation where status is unknown and document medication history.");
    list.push("Generate a structured report for gastroenterology referral or urgent review.");
  } else if (severity === "Medium") {
    list.push("Schedule follow-up assessment and track pain frequency, triggers, and response to therapy.");
    list.push("Recommend H. pylori testing if not recently confirmed.");
    list.push("Review NSAID exposure, diet, alcohol use, smoking, and stress contributors.");
  } else {
    list.push("Provide lifestyle guidance and symptom monitoring with routine reassessment.");
    list.push("Escalate if pain worsens, vomiting occurs, weight loss appears, or bleeding is suspected.");
    list.push("Keep baseline patient record for future model comparison.");
  }

  if (data.nsaid === "yes") list.push("Flag frequent NSAID use as a modifiable ulcer risk factor.");
  if (data.bleeding === "yes") list.push("Bleeding symptoms require urgent medical evaluation.");
  return list;
}

async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options
  });
  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.error || "Backend request failed.");
  }
  return payload;
}

function readLocalAssessments() {
  const saved = JSON.parse(localStorage.getItem("pudAssessments") || "[]");
  return saved.length ? saved : samples;
}

async function loadAssessments() {
  try {
    const payload = await apiRequest("/api/patients");
    assessmentCache = payload.patients.length ? payload.patients : samples;
  } catch (error) {
    assessmentCache = readLocalAssessments();
  }
  return assessmentCache;
}

function saveLocalAssessment(record) {
  const existing = JSON.parse(localStorage.getItem("pudAssessments") || "[]");
  existing.unshift(record);
  localStorage.setItem("pudAssessments", JSON.stringify(existing.slice(0, 20)));
}

function updateResult(score, severity, recommendations) {
  const scoreText = document.querySelector("[data-score]");
  const severityText = document.querySelector("[data-severity]");
  const ring = document.querySelector("[data-score-ring]");
  const recommendationList = document.querySelector("[data-recommendations]");
  if (!scoreText || !severityText || !ring || !recommendationList) return;

  scoreText.textContent = `${score}%`;
  severityText.textContent = `${severity} Risk`;
  const degrees = Math.round((score / 100) * 360);
  const color = severity === "High" ? "#c04444" : severity === "Medium" ? "#f2a03a" : "#24895a";
  ring.style.background = `conic-gradient(${color} 0deg, ${color} ${degrees}deg, #e8eef3 ${degrees}deg 360deg)`;
  recommendationList.innerHTML = recommendations.map((item) => `<li>${item}</li>`).join("");
}

function renderPatientTable(items = assessmentCache) {
  const body = document.querySelector("[data-patient-table]");
  if (!body) return;
  body.innerHTML = items.map((item) => `
    <tr>
      <td><strong>${item.id}</strong><br><span class="muted">${item.name}</span></td>
      <td>${item.age}</td>
      <td>${item.symptoms}</td>
      <td><span class="badge ${badgeClass(item.severity)}">${item.severity}</span></td>
      <td>${item.risk}%</td>
    </tr>
  `).join("");
}

function renderPredictionCards(items = assessmentCache) {
  const target = document.querySelector("[data-prediction-cards]");
  if (!target) return;
  target.innerHTML = items.slice(0, 6).map((item) => `
    <article class="card">
      <div class="card-icon"><i data-lucide="activity"></i></div>
      <h3>${item.name}</h3>
      <p><strong>${item.risk}% ${item.severity} risk</strong></p>
      <p>${item.recommendation}</p>
    </article>
  `).join("");
  if (window.lucide) window.lucide.createIcons();
}

function normalizeRecommendations(item) {
  if (Array.isArray(item.recommendations)) return item.recommendations;
  if (item.recommendations_json) {
    try {
      return JSON.parse(item.recommendations_json);
    } catch (error) {
      return [item.recommendation];
    }
  }
  return [item.recommendation];
}

function renderReportPreview(record) {
  const target = document.querySelector("[data-report-preview]");
  if (!target) return;
  const item = record || assessmentCache[0] || samples[0];
  const recommendations = normalizeRecommendations(item);
  target.innerHTML = `
    <header>
      <div>
        <h3>Intelligent PUD Management Report</h3>
        <p class="muted">Extreme Gradient Algorithm assessment summary</p>
      </div>
      <strong>${item.id}</strong>
    </header>
    <section>
      <h3>Patient</h3>
      <p>${item.name}, ${item.age} years</p>
    </section>
    <section>
      <h3>Prediction</h3>
      <p><span class="badge ${badgeClass(item.severity)}">${item.severity}</span> ${item.risk}% estimated PUD management risk</p>
    </section>
    <section>
      <h3>Clinical Notes</h3>
      <p>${item.symptoms}</p>
    </section>
    <section>
      <h3>Recommendations</h3>
      <ul class="recommendations">${recommendations.map((text) => `<li>${text}</li>`).join("")}</ul>
    </section>
  `;
}

function populateReportOptions(items = assessmentCache) {
  const select = document.querySelector("[data-report-patient]");
  if (!select) return;
  select.innerHTML = items.map((item) => `<option value="${item.id}">${item.id} - ${item.name}</option>`).join("");
}

async function createAssessment(formData) {
  try {
    const payload = await apiRequest("/api/assessments", {
      method: "POST",
      body: JSON.stringify(formData)
    });
    return payload.assessment;
  } catch (error) {
    const score = computeRisk(formData);
    const severity = severityFromScore(score);
    const recommendations = recommendationsFor(severity, formData);
    const record = {
      id: `PUD-${Date.now().toString().slice(-5)}`,
      name: formData.name || "New Patient",
      age: formData.age || "N/A",
      risk: score,
      severity,
      symptoms: formData.symptoms || "New assessment captured from clinical input.",
      recommendation: recommendations[0],
      recommendations
    };
    saveLocalAssessment(record);
    return record;
  }
}

if (assessmentForm) {
  assessmentForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = Object.fromEntries(new FormData(assessmentForm).entries());
    const submitButton = assessmentForm.querySelector("button[type='submit']");
    if (submitButton) submitButton.disabled = true;

    try {
      const record = await createAssessment(formData);
      updateResult(record.risk, record.severity, normalizeRecommendations(record));
      assessmentCache.unshift(record);
    } finally {
      if (submitButton) submitButton.disabled = false;
    }
  });
}

if (reportForm) {
  reportForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(reportForm).entries());
    let record = assessmentCache.find((item) => item.id === data.patient);

    try {
      const payload = await apiRequest(`/api/reports/${data.patient}`);
      record = payload.report;
    } catch (error) {
      record = record || assessmentCache[0];
    }
    renderReportPreview(record);
  });
}

async function boot() {
  setActiveNav();
  initUiEffects();
  const assessments = await loadAssessments();
  renderPatientTable(assessments);
  renderPredictionCards(assessments);
  populateReportOptions(assessments);
  renderReportPreview(assessments[0]);

  if (window.lucide) {
    window.lucide.createIcons();
  }
}

boot();
```

## pudpredict/__init__.py
`$lang
try:
    import pymysql

    pymysql.install_as_MySQLdb()
except ImportError:
    pass
```

## pudpredict/settings.py
`$lang
from pathlib import Path
import os

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


BASE_DIR = Path(__file__).resolve().parent.parent

if load_dotenv:
    load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-pudpredict-secret-key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "patients",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pudpredict.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pudpredict.wsgi.application"

USE_MYSQL = os.getenv("USE_MYSQL", "False").lower() == "true"

if USE_MYSQL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("MYSQL_DATABASE", "pudpredict_db"),
            "USER": os.getenv("MYSQL_USER", "root"),
            "PASSWORD": os.getenv("MYSQL_PASSWORD", ""),
            "HOST": os.getenv("MYSQL_HOST", "127.0.0.1"),
            "PORT": os.getenv("MYSQL_PORT", "3306"),
            "OPTIONS": {
                "charset": "utf8mb4",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

MYSQL_DATABASES = {
    "mysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE", "pudpredict_db"),
        "USER": os.getenv("MYSQL_USER", "root"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD", ""),
        "HOST": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "PORT": os.getenv("MYSQL_PORT", "3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    },
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Lagos"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR]
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "patients:dashboard"
LOGOUT_REDIRECT_URL = "patients:landing"
```

## pudpredict/urls.py
`$lang
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("patients.urls")),
]
```

## pudpredict/asgi.py
`$lang
import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pudpredict.settings")

application = get_asgi_application()
```

## pudpredict/wsgi.py
`$lang
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pudpredict.settings")

application = get_wsgi_application()
```

## patients/__init__.py
`$lang

```

## patients/admin.py
`$lang
from django.contrib import admin

from .models import Assessment, Patient, SymptomLog


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("patient_code", "full_name", "age", "gender", "created_at")
    search_fields = ("patient_code", "full_name", "phone")
    list_filter = ("gender", "created_at")


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "risk_score", "severity", "hpylori_status", "nsaid_use", "created_at")
    search_fields = ("patient__patient_code", "patient__full_name", "symptoms")
    list_filter = ("severity", "hpylori_status", "nsaid_use", "created_at")


@admin.register(SymptomLog)
class SymptomLogAdmin(admin.ModelAdmin):
    list_display = ("user", "abdominal_pain", "nausea", "heartburn", "estimated_risk", "created_at")
    search_fields = ("user__username", "notes", "meal_trigger")
    list_filter = ("created_at",)
```

## patients/apps.py
`$lang
from django.apps import AppConfig


class PatientsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "patients"
```

## patients/forms.py
`$lang
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Assessment, Patient, SymptomLog


class PatientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class PatientAssessmentForm(forms.Form):
    full_name = forms.CharField(max_length=120, label="Patient Name")
    age = forms.IntegerField(min_value=1, max_value=120)
    gender = forms.ChoiceField(choices=Patient.GENDER_CHOICES)
    phone = forms.CharField(max_length=32, required=False)
    systolic_bp = forms.IntegerField(min_value=60, max_value=240, required=False, label="Systolic BP (mmHg)")
    diastolic_bp = forms.IntegerField(min_value=40, max_value=160, required=False, label="Diastolic BP (mmHg)")
    weight = forms.DecimalField(min_value=20, max_value=250, required=False, label="Weight (kg)")
    pain_severity = forms.ChoiceField(choices=Assessment.PAIN_CHOICES)
    hpylori_status = forms.ChoiceField(choices=Assessment.HPYLORI_CHOICES, label="H. pylori Status")
    nsaid_use = forms.ChoiceField(choices=Assessment.NSAID_CHOICES, label="NSAID Use")
    bleeding_symptoms = forms.ChoiceField(choices=Assessment.YES_NO_CHOICES)
    smoking_history = forms.ChoiceField(choices=Assessment.YES_NO_CHOICES)
    alcohol_intake = forms.ChoiceField(choices=Assessment.LEVEL_CHOICES)
    stress_level = forms.ChoiceField(choices=Assessment.LEVEL_CHOICES)
    diet_pattern = forms.ChoiceField(choices=Assessment.LEVEL_CHOICES)
    previous_ulcer = forms.ChoiceField(choices=Assessment.YES_NO_CHOICES)
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False,
        help_text="Clinical notes, presenting symptoms, medication history, and relevant observations.",
    )

    def clean_pain_severity(self):
        return int(self.cleaned_data["pain_severity"])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Enter full name",
            "age": "e.g. 42",
            "phone": "Optional phone number",
            "systolic_bp": "e.g. 120",
            "diastolic_bp": "e.g. 80",
            "weight": "e.g. 70",
            "symptoms": "Burning pain, nausea, meal triggers, medication history",
        }
        for name, field in self.fields.items():
            field.widget.attrs.setdefault("class", "input-control")
            if name in placeholders:
                field.widget.attrs.setdefault("placeholder", placeholders[name])


class SymptomLogForm(forms.ModelForm):
    class Meta:
        model = SymptomLog
        fields = [
            "abdominal_pain",
            "nausea",
            "heartburn",
            "appetite_loss",
            "medication_taken",
            "meal_trigger",
            "notes",
        ]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "input-control")


class ChatbotForm(forms.Form):
    severity_level = forms.ChoiceField(
        choices=[("low", "Low"), ("moderate", "Moderate"), ("high", "High")],
        label="Current Symptom Severity",
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Ask for lifestyle guidance, symptom tracking tips, or report interpretation help."}),
        label="Message",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "input-control")
```

## patients/ml.py
`$lang
def severity_from_score(score):
    if score >= 70:
        return "High"
    if score >= 40:
        return "Medium"
    return "Low"


def simulated_xgboost_prediction(data):
    """LLM-simulated XGBoost predictor for the project prototype.

    The interface mirrors a real model pipeline: validated clinical features go in,
    risk score, feature importance, and recommendations come out. A trained XGBoost
    model can later replace this function without changing the views or database.
    """
    age = int(data.get("age") or 0)
    pain = int(data.get("pain_severity") or 0)

    contributions = {
        "Age": 12 if age > 55 else 7 if age > 40 else 2,
        "Pain Severity": pain * 6,
        "H. pylori Status": 18 if data.get("hpylori_status") == "positive" else 8 if data.get("hpylori_status") == "unknown" else 0,
        "NSAID Usage": 15 if data.get("nsaid_use") == "yes" else 8 if data.get("nsaid_use") == "sometimes" else 0,
        "Bleeding Symptoms": 20 if data.get("bleeding_symptoms") == "yes" else 0,
        "Smoking History": 8 if data.get("smoking_history") == "yes" else 0,
        "Alcohol Intake": 8 if data.get("alcohol_intake") == "high" else 4 if data.get("alcohol_intake") == "moderate" else 0,
        "Stress Level": 7 if data.get("stress_level") == "high" else 3 if data.get("stress_level") == "moderate" else 0,
        "Diet Pattern": 7 if data.get("diet_pattern") == "high" else 3 if data.get("diet_pattern") == "moderate" else 0,
        "Previous Ulcer": 9 if data.get("previous_ulcer") == "yes" else 0,
    }

    raw_score = 8 + sum(contributions.values())
    risk_score = max(3, min(96, round(raw_score)))
    severity = severity_from_score(risk_score)
    total = max(sum(contributions.values()), 1)
    feature_importance = {
        key: round((value / total) * 100)
        for key, value in sorted(contributions.items(), key=lambda item: item[1], reverse=True)
        if value > 0
    }

    recommendations = recommendations_for(severity, data)
    return {
        "risk_score": risk_score,
        "severity": severity,
        "feature_importance": feature_importance,
        "recommendations": recommendations,
    }


def recommendations_for(severity, data):
    if severity == "High":
        items = [
            "Prioritize clinician review and screen immediately for bleeding, weight loss, vomiting, or severe persistent pain.",
            "Request or confirm H. pylori testing and document eradication plan where applicable.",
            "Review NSAID exposure and consider gastroprotection or alternative pain management under clinician guidance.",
            "Generate an urgent report for gastroenterology referral or senior clinical review.",
        ]
    elif severity == "Medium":
        items = [
            "Schedule follow-up assessment and monitor pain frequency, triggers, medication use, and response to treatment.",
            "Recommend H. pylori testing if status is unknown or symptoms persist.",
            "Provide counseling on diet pattern, alcohol intake, stress, smoking, and NSAID risk.",
        ]
    else:
        items = [
            "Provide lifestyle guidance and symptom tracking with routine reassessment.",
            "Escalate if alarm symptoms develop or symptoms persist despite initial management.",
            "Keep the patient record for future comparison and prediction history.",
        ]

    if data.get("bleeding_symptoms") == "yes":
        items.insert(0, "Bleeding symptoms require urgent medical evaluation.")
    if data.get("nsaid_use") == "yes":
        items.append("Frequent NSAID use is flagged as a modifiable ulcer risk factor.")
    return items


def symptom_log_risk(data, latest_assessment=None):
    pain = int(data.get("abdominal_pain") or 0)
    nausea = int(data.get("nausea") or 0)
    heartburn = int(data.get("heartburn") or 0)
    appetite_loss = int(data.get("appetite_loss") or 0)
    baseline = latest_assessment.risk_score * 0.35 if latest_assessment else 12
    symptom_score = (pain * 4) + (nausea * 2.5) + (heartburn * 2.5) + (appetite_loss * 2)
    return max(3, min(96, round(baseline + symptom_score)))


def chatbot_guidance(message, severity_level, latest_assessment=None, recent_logs=None):
    recent_logs = recent_logs or []
    latest_risk = latest_assessment.risk_score if latest_assessment else None
    avg_symptom = None
    if recent_logs:
        avg_symptom = round(sum(log.severity_average for log in recent_logs) / len(recent_logs), 1)

    tips = [
        "I can share general education and self-management ideas, but I cannot diagnose or replace a clinician.",
        "Keep a simple symptom diary noting pain timing, meals, medicines, stress, and sleep because patterns help clinical review.",
    ]

    if severity_level == "high":
        tips.extend([
            "Because your current symptom severity is high, arrange medical review promptly, especially if pain is worsening or persistent.",
            "Seek urgent care immediately for black stools, vomiting blood, fainting, severe sudden pain, unexplained weight loss, or repeated vomiting.",
        ])
    elif severity_level == "moderate":
        tips.extend([
            "For moderate symptoms, avoid NSAIDs unless prescribed, limit alcohol, stop smoking where applicable, and consider smaller low-irritant meals.",
            "If symptoms continue, ask a clinician about H. pylori testing and whether acid suppression is appropriate for you.",
        ])
    else:
        tips.extend([
            "For mild symptoms, continue tracking triggers and maintain regular meals, hydration, sleep, and stress reduction habits.",
            "Escalate care if mild symptoms become frequent, intense, or start affecting eating, sleep, or daily activities.",
        ])

    if latest_risk is not None:
        tips.append(f"Your latest stored risk profile is {latest_risk}%, so use that trend as a discussion point with your clinician.")
    if avg_symptom is not None:
        tips.append(f"Your recent average symptom severity is {avg_symptom}/10; rising averages should prompt reassessment.")

    if "diet" in message.lower() or "food" in message.lower():
        tips.append("Diet triggers vary, but many patients track spicy foods, alcohol, caffeine, very fatty meals, late-night meals, and long fasting periods.")
    if "medicine" in message.lower() or "drug" in message.lower() or "nsaid" in message.lower():
        tips.append("Avoid starting, stopping, or combining ulcer-related medicines without clinician guidance, especially if you use NSAIDs, aspirin, anticoagulants, or steroids.")

    return tips
```

## patients/models.py
`$lang
from django.db import models
from django.conf import settings


class Patient(models.Model):
    GENDER_CHOICES = [
        ("female", "Female"),
        ("male", "Male"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="patient_records")
    patient_code = models.CharField(max_length=24, unique=True)
    full_name = models.CharField(max_length=120)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=32, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.patient_code} - {self.full_name}"


class Assessment(models.Model):
    YES_NO_CHOICES = [("no", "No"), ("yes", "Yes")]
    LEVEL_CHOICES = [("low", "Low"), ("moderate", "Moderate"), ("high", "High")]
    PAIN_CHOICES = [(1, "Mild"), (2, "Moderate"), (3, "Severe")]
    HPYLORI_CHOICES = [
        ("unknown", "Unknown"),
        ("negative", "Negative"),
        ("positive", "Positive"),
    ]
    NSAID_CHOICES = [
        ("no", "No"),
        ("sometimes", "Sometimes"),
        ("yes", "Frequent"),
    ]
    SEVERITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="assessments")
    systolic_bp = models.PositiveSmallIntegerField(null=True, blank=True)
    diastolic_bp = models.PositiveSmallIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pain_severity = models.PositiveSmallIntegerField(choices=PAIN_CHOICES)
    hpylori_status = models.CharField(max_length=16, choices=HPYLORI_CHOICES)
    nsaid_use = models.CharField(max_length=16, choices=NSAID_CHOICES)
    bleeding_symptoms = models.CharField(max_length=8, choices=YES_NO_CHOICES)
    smoking_history = models.CharField(max_length=8, choices=YES_NO_CHOICES)
    alcohol_intake = models.CharField(max_length=16, choices=LEVEL_CHOICES)
    stress_level = models.CharField(max_length=16, choices=LEVEL_CHOICES)
    diet_pattern = models.CharField(max_length=16, choices=LEVEL_CHOICES, default="moderate")
    previous_ulcer = models.CharField(max_length=8, choices=YES_NO_CHOICES, default="no")
    symptoms = models.TextField(blank=True)
    risk_score = models.PositiveSmallIntegerField(default=0)
    severity = models.CharField(max_length=16, choices=SEVERITY_CHOICES, default="Low")
    feature_importance = models.JSONField(default=dict)
    recommendations = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.patient.full_name} - {self.risk_score}%"


class SymptomLog(models.Model):
    SEVERITY_CHOICES = [(value, str(value)) for value in range(1, 11)]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="symptom_logs")
    abdominal_pain = models.PositiveSmallIntegerField(choices=SEVERITY_CHOICES)
    nausea = models.PositiveSmallIntegerField(choices=SEVERITY_CHOICES)
    heartburn = models.PositiveSmallIntegerField(choices=SEVERITY_CHOICES)
    appetite_loss = models.PositiveSmallIntegerField(choices=SEVERITY_CHOICES)
    medication_taken = models.CharField(max_length=120, blank=True)
    meal_trigger = models.CharField(max_length=160, blank=True)
    notes = models.TextField(blank=True)
    estimated_risk = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def severity_average(self):
        return round((self.abdominal_pain + self.nausea + self.heartburn + self.appetite_loss) / 4, 1)

    def __str__(self):
        return f"{self.user.username} symptom log - {self.severity_average}/10"
```

## patients/urls.py
`$lang
from django.urls import path

from . import views


app_name = "patients"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("assessment/", views.assessment_create, name="assessment"),
    path("symptoms/new/", views.symptom_log_create, name="symptom_log"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("patients/", views.patient_history, name="history"),
    path("predictions/", views.prediction_results, name="predictions"),
    path("reports/", views.reports, name="reports"),
    path("reports/<int:assessment_id>/", views.report_detail, name="report_detail"),
    path("reports/<int:assessment_id>/export/", views.export_report, name="export_report"),
    path("architecture/", views.architecture, name="architecture"),
]
```

## patients/views.py
`$lang
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import ChatbotForm, PatientAssessmentForm, PatientRegistrationForm, SymptomLogForm
from .ml import chatbot_guidance, simulated_xgboost_prediction, symptom_log_risk
from .models import Assessment, Patient, SymptomLog


def landing(request):
    return render(request, "patients/landing.html")


def register(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created. Your secure patient dashboard is ready.")
            return redirect("patients:dashboard")
    else:
        form = PatientRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


def assessment_create(request):
    prediction = None
    if request.method == "POST":
        form = PatientAssessmentForm(request.POST)
        if form.is_valid():
            patient = Patient.objects.create(
                user=request.user if request.user.is_authenticated else None,
                patient_code=f"PUD-{timezone.now().strftime('%H%M%S')}",
                full_name=form.cleaned_data["full_name"],
                age=form.cleaned_data["age"],
                gender=form.cleaned_data["gender"],
                phone=form.cleaned_data["phone"],
            )
            prediction = simulated_xgboost_prediction(form.cleaned_data)
            assessment = Assessment.objects.create(
                patient=patient,
                systolic_bp=form.cleaned_data.get("systolic_bp"),
                diastolic_bp=form.cleaned_data.get("diastolic_bp"),
                weight=form.cleaned_data.get("weight"),
                pain_severity=form.cleaned_data["pain_severity"],
                hpylori_status=form.cleaned_data["hpylori_status"],
                nsaid_use=form.cleaned_data["nsaid_use"],
                bleeding_symptoms=form.cleaned_data["bleeding_symptoms"],
                smoking_history=form.cleaned_data["smoking_history"],
                alcohol_intake=form.cleaned_data["alcohol_intake"],
                stress_level=form.cleaned_data["stress_level"],
                diet_pattern=form.cleaned_data["diet_pattern"],
                previous_ulcer=form.cleaned_data["previous_ulcer"],
                symptoms=form.cleaned_data["symptoms"],
                risk_score=prediction["risk_score"],
                severity=prediction["severity"],
                feature_importance=prediction["feature_importance"],
                recommendations=prediction["recommendations"],
            )
            messages.success(request, "Patient assessment saved and prediction generated.")
            return redirect(reverse("patients:report_detail", args=[assessment.id]))
    else:
        form = PatientAssessmentForm()

    return render(request, "patients/assessment.html", {"form": form, "prediction": prediction})


def patient_history(request):
    patients = Patient.objects.prefetch_related("assessments").all()
    return render(request, "patients/history.html", {"patients": patients})


def prediction_results(request):
    assessments = Assessment.objects.select_related("patient").all()
    return render(request, "patients/predictions.html", {"assessments": assessments})


def reports(request):
    assessments = Assessment.objects.select_related("patient").all()
    return render(request, "patients/reports.html", {"assessments": assessments})


def report_detail(request, assessment_id):
    assessment = get_object_or_404(Assessment.objects.select_related("patient"), id=assessment_id)
    return render(request, "patients/report_detail.html", {"assessment": assessment})


def export_report(request, assessment_id):
    assessment = get_object_or_404(Assessment.objects.select_related("patient"), id=assessment_id)
    lines = [
        "PUDPredict Clinical Report",
        f"Patient ID: {assessment.patient.patient_code}",
        f"Patient Name: {assessment.patient.full_name}",
        f"Age: {assessment.patient.age}",
        f"Risk Score: {assessment.risk_score}%",
        f"Severity: {assessment.severity}",
        "",
        "Clinical Notes:",
        assessment.symptoms or "No additional notes supplied.",
        "",
        "Recommendations:",
        *[f"- {item}" for item in assessment.recommendations],
    ]
    response = HttpResponse("\n".join(lines), content_type="text/plain")
    response["Content-Disposition"] = f'attachment; filename="{assessment.patient.patient_code}-report.txt"'
    return response


def architecture(request):
    return render(request, "patients/architecture.html")


@login_required
def dashboard(request):
    assessments = Assessment.objects.select_related("patient").filter(patient__user=request.user)[:8]
    symptom_logs = SymptomLog.objects.filter(user=request.user)[:10]
    latest_assessment = assessments.first()
    latest_log = symptom_logs.first()
    return render(
        request,
        "patients/dashboard.html",
        {
            "assessments": assessments,
            "symptom_logs": symptom_logs,
            "latest_assessment": latest_assessment,
            "latest_log": latest_log,
        },
    )


@login_required
def symptom_log_create(request):
    latest_assessment = Assessment.objects.filter(patient__user=request.user).select_related("patient").first()
    if request.method == "POST":
        form = SymptomLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.estimated_risk = symptom_log_risk(form.cleaned_data, latest_assessment)
            log.save()
            messages.success(request, "Symptom log saved and risk trend updated.")
            return redirect("patients:dashboard")
    else:
        form = SymptomLogForm()
    return render(request, "patients/symptom_log.html", {"form": form, "latest_assessment": latest_assessment})


@login_required
def chatbot(request):
    latest_assessment = Assessment.objects.filter(patient__user=request.user).select_related("patient").first()
    recent_logs = list(SymptomLog.objects.filter(user=request.user)[:5])
    response = None
    if request.method == "POST":
        form = ChatbotForm(request.POST)
        if form.is_valid():
            response = chatbot_guidance(
                form.cleaned_data["message"],
                form.cleaned_data["severity_level"],
                latest_assessment,
                recent_logs,
            )
    else:
        form = ChatbotForm()
    return render(
        request,
        "patients/chatbot.html",
        {
            "form": form,
            "response": response,
            "latest_assessment": latest_assessment,
            "recent_logs": recent_logs,
        },
    )
```

## patients/migrations/__init__.py
`$lang

```

## patients/migrations/0001_initial.py
`$lang
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("patient_code", models.CharField(max_length=24, unique=True)),
                ("full_name", models.CharField(max_length=120)),
                ("age", models.PositiveSmallIntegerField()),
                ("gender", models.CharField(choices=[("female", "Female"), ("male", "Male"), ("other", "Other")], max_length=16)),
                ("phone", models.CharField(blank=True, max_length=32)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Assessment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("pain_severity", models.PositiveSmallIntegerField(choices=[(1, "Mild"), (2, "Moderate"), (3, "Severe")])),
                ("hpylori_status", models.CharField(choices=[("unknown", "Unknown"), ("negative", "Negative"), ("positive", "Positive")], max_length=16)),
                ("nsaid_use", models.CharField(choices=[("no", "No"), ("sometimes", "Sometimes"), ("yes", "Frequent")], max_length=16)),
                ("bleeding_symptoms", models.CharField(choices=[("no", "No"), ("yes", "Yes")], max_length=8)),
                ("smoking_history", models.CharField(choices=[("no", "No"), ("yes", "Yes")], max_length=8)),
                ("alcohol_intake", models.CharField(choices=[("low", "Low"), ("moderate", "Moderate"), ("high", "High")], max_length=16)),
                ("stress_level", models.CharField(choices=[("low", "Low"), ("moderate", "Moderate"), ("high", "High")], max_length=16)),
                ("diet_pattern", models.CharField(choices=[("low", "Low"), ("moderate", "Moderate"), ("high", "High")], default="moderate", max_length=16)),
                ("previous_ulcer", models.CharField(choices=[("no", "No"), ("yes", "Yes")], default="no", max_length=8)),
                ("symptoms", models.TextField(blank=True)),
                ("risk_score", models.PositiveSmallIntegerField(default=0)),
                ("severity", models.CharField(choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")], default="Low", max_length=16)),
                ("feature_importance", models.JSONField(default=dict)),
                ("recommendations", models.JSONField(default=list)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="assessments", to="patients.patient")),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
```

## patients/migrations/0002_dashboard_chatbot.py
`$lang
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="user",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="patient_records", to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name="SymptomLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("abdominal_pain", models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")])),
                ("nausea", models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")])),
                ("heartburn", models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")])),
                ("appetite_loss", models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")])),
                ("medication_taken", models.CharField(blank=True, max_length=120)),
                ("meal_trigger", models.CharField(blank=True, max_length=160)),
                ("notes", models.TextField(blank=True)),
                ("estimated_risk", models.PositiveSmallIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="symptom_logs", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
```

## patients/migrations/0003_assessment_health_metrics.py
`$lang
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0002_dashboard_chatbot"),
    ]

    operations = [
        migrations.AddField(
            model_name="assessment",
            name="systolic_bp",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assessment",
            name="diastolic_bp",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assessment",
            name="weight",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
```

## patients/templatetags/__init__.py
`$lang

```

## patients/templatetags/patient_extras.py
`$lang
from django import template


register = template.Library()


@register.filter
def badge_class(value):
    return str(value or "low").lower()
```

## templates/patients/base.html
`$lang
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}PUDPredict{% endblock %}</title>
  <link rel="stylesheet" href="{% static 'styles.css' %}">
</head>
<body>
  <header class="site-header" data-header>
    <nav class="nav-shell">
      <a class="brand" href="{% url 'patients:landing' %}">
        <span class="brand-mark"><i data-lucide="activity"></i></span>
        <span>PUD<span class="brand-blue">Predict</span></span>
      </a>
      {% block nav %}
      <div class="nav-links">
        <a href="{% url 'patients:dashboard' %}" data-nav-match="/dashboard/">Dashboard</a>
        <a href="{% url 'patients:assessment' %}" data-nav-match="/assessment/">New Assessment</a>
        <a href="{% url 'patients:history' %}" data-nav-match="/patients/">Patient History</a>
        <a href="{% url 'patients:reports' %}" data-nav-match="/reports/">Reports</a>
        <a href="{% url 'patients:chatbot' %}" data-nav-match="/chatbot/">AI Advisor</a>
        {% if user.is_authenticated %}
          <form method="post" action="{% url 'logout' %}" style="margin:0;">
            {% csrf_token %}
            <button class="nav-cta" type="submit" style="border:0;cursor:pointer;">Logout</button>
          </form>
        {% else %}
          <a class="nav-cta" href="{% url 'login' %}">Login</a>
        {% endif %}
      </div>
      {% endblock %}
    </nav>
  </header>
  {% if messages %}
    <div class="page" style="padding-top:18px;">
      {% for message in messages %}
        <div class="card" style="min-height:auto;padding:16px 20px;">{{ message }}</div>
      {% endfor %}
    </div>
  {% endif %}
  {% block content %}{% endblock %}
  <footer class="footer">
    <div class="page">
      <span>PUDPredict</span>
      <span>Django backend with optional MySQL storage</span>
    </div>
  </footer>
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <script src="{% static 'js/app.js' %}"></script>
</body>
</html>
```

## templates/patients/landing.html
`$lang
{% extends "patients/base.html" %}
{% block title %}PUDPredict | Intelligent PUD Management{% endblock %}
{% block nav %}
<div class="nav-links landing-nav">
  <a href="#features">Features</a>
  <a class="nav-cta" href="{% url 'patients:dashboard' %}">Open App</a>
</div>
{% endblock %}
{% block content %}
<main class="page">
  <section class="hero reveal">
    <div class="hero-copy">
      <p class="eyebrow"><i data-lucide="brain"></i> Powered by XGBoost Algorithm</p>
      <h1>Intelligent <span class="text-blue">Peptic Ulcer</span> Disease Management</h1>
      <p class="lead">A professional Django system for clinical data entry, simulated XGBoost prediction, patient history review, recommendations, and report export.</p>
      <div class="hero-actions">
        <a class="btn" href="{% url 'patients:assessment' %}"><i data-lucide="clipboard-plus"></i> Start Assessment</a>
        <a class="btn secondary" href="{% url 'patients:architecture' %}"><i data-lucide="network"></i> View System Flow</a>
      </div>
    </div>
    <div class="hero-panel">
      <div class="dashboard-preview">
        <div class="preview-top">
          <span class="preview-icon"><i data-lucide="bar-chart-3"></i></span>
          <span><span class="preview-title">Risk Assessment</span><span class="preview-subtitle">LLM-simulated XGBoost Model</span></span>
        </div>
        <div class="preview-body">
          <div class="risk-gauge">
            <div class="bar-row"><div class="bar-label"><span>H. pylori Status</span><strong>87%</strong></div><div class="gauge-track"><div class="gauge-fill" style="--value:87%;--bar-color:#2563eb"></div></div></div>
            <div class="bar-row"><div class="bar-label"><span>NSAID Usage</span><strong>72%</strong></div><div class="gauge-track"><div class="gauge-fill" style="--value:72%;--bar-color:#2dd4bf"></div></div></div>
            <div class="bar-row"><div class="bar-label"><span>Smoking History</span><strong>65%</strong></div><div class="gauge-track"><div class="gauge-fill" style="--value:65%;--bar-color:#7c3aed"></div></div></div>
            <div class="bar-row"><div class="bar-label"><span>Stress Level</span><strong>58%</strong></div><div class="gauge-track"><div class="gauge-fill" style="--value:58%;--bar-color:#eabf52"></div></div></div>
            <div class="patient-row"><strong>Overall Risk</strong><span class="badge high">78%</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section reveal" id="features">
    <div class="section-heading">
      <h2>Comprehensive PUD Management</h2>
      <p>A full-featured intelligent system for peptic ulcer disease assessment, prediction, and clinical decision support.</p>
    </div>
    <div class="grid-3">
      <article class="card"><div class="card-icon"><i data-lucide="brain"></i></div><h3>XGBoost Prediction</h3><p>Simulated Extreme Gradient Boosting logic for PUD risk assessment and classification.</p></article>
      <article class="card"><div class="card-icon"><i data-lucide="stethoscope"></i></div><h3>Clinical Data Input</h3><p>Captures symptoms, lab indicators, lifestyle factors, medication history, and previous ulcer status.</p></article>
      <article class="card"><div class="card-icon"><i data-lucide="file-down"></i></div><h3>Report Export</h3><p>Generates clean patient reports with prediction score, risk level, and clinical recommendations.</p></article>
    </div>
  </section>

  <section class="section workflow-section reveal">
    <div class="section-heading">
      <p class="section-kicker">SYSTEM WORKFLOW</p>
      <h2>How It Works</h2>
      <p>A streamlined process from data entry to prediction and clinical recommendations.</p>
    </div>
    <div class="workflow">
      <div class="step"><div class="step-icon"><i data-lucide="user-plus"></i><span class="step-number">01</span></div><strong>User Logs In</strong><span>Authorized users access the Django system.</span></div>
      <div class="step"><div class="step-icon"><i data-lucide="clipboard-list"></i><span class="step-number">02</span></div><strong>Enter Patient Data</strong><span>Clinical parameters are validated and stored.</span></div>
      <div class="step"><div class="step-icon"><i data-lucide="cpu"></i><span class="step-number">03</span></div><strong>XGBoost Prediction</strong><span>The simulated model returns risk score and feature importance.</span></div>
      <div class="step"><div class="step-icon"><i data-lucide="file-bar-chart"></i><span class="step-number">04</span></div><strong>Results & Reports</strong><span>Review recommendations and export reports.</span></div>
    </div>
  </section>
</main>
{% endblock %}
```

## templates/patients/assessment.html
`$lang
{% extends "patients/base.html" %}
{% block title %}Assessment | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="app-title-row reveal">
    <div>
      <h1>New Assessment</h1>
      <p class="lead">Enter patient metrics and clinical symptoms to run prediction.</p>
    </div>
  </section>
  <section class="form-grid reveal">
    <form class="form-card assessment-card" method="post" data-loading-form>
      {% csrf_token %}
      <h3 class="form-section-title">Patient Information</h3>
      <div class="field-grid">
        {% for field in form %}
          {% if field.name == "full_name" or field.name == "age" or field.name == "gender" or field.name == "phone" or field.name == "systolic_bp" or field.name == "diastolic_bp" or field.name == "weight" %}
            <div class="field">{{ field.label_tag }}{{ field }}{% for error in field.errors %}<span class="muted">{{ error }}</span>{% endfor %}</div>
          {% endif %}
        {% endfor %}
      </div>
      <h3 class="form-section-title">Symptoms & Conditions</h3>
      <div class="field-grid">
        {% for field in form %}
          {% if field.name != "full_name" and field.name != "age" and field.name != "gender" and field.name != "phone" and field.name != "systolic_bp" and field.name != "diastolic_bp" and field.name != "weight" and field.name != "symptoms" %}
            <div class="field condition-field">{{ field.label_tag }}{{ field }}{% for error in field.errors %}<span class="muted">{{ error }}</span>{% endfor %}</div>
          {% endif %}
        {% endfor %}
        <div class="field full">{{ form.symptoms.label_tag }}{{ form.symptoms }}{% for error in form.symptoms.errors %}<span class="muted">{{ error }}</span>{% endfor %}</div>
      </div>
      <div class="button-row">
        <button class="btn" type="submit"><i data-lucide="brain"></i> Run Prediction</button>
        <a class="btn secondary" href="{% url 'patients:history' %}"><i data-lucide="users"></i> Patient History</a>
      </div>
    </form>
    <aside class="result-panel">
      <p class="eyebrow"><i data-lucide="bar-chart-3"></i> Prediction Output</p>
      <h2>Ready for Assessment</h2>
      <div class="score-ring"><div class="score-ring-inner"><strong>--%</strong><span class="muted">risk score</span></div></div>
      <h3>Backend Data Flow</h3>
      <ul class="recommendations">
        <li>Django validates the submitted form.</li>
        <li>Patient and assessment records are stored in the configured database.</li>
        <li>The simulated XGBoost layer returns risk and recommendations.</li>
      </ul>
    </aside>
  </section>
</main>
{% endblock %}
```

## templates/patients/dashboard.html
`$lang
{% extends "patients/base.html" %}
{% load patient_extras %}
{% block title %}Patient Dashboard | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="app-title-row reveal">
    <div>
      <h1>Dashboard</h1>
      <p class="lead">Peptic Ulcer Disease Management Overview</p>
    </div>
    <a class="btn" href="{% url 'patients:assessment' %}"><i data-lucide="plus"></i> New Assessment</a>
  </section>

  <section class="stats-grid reveal">
    <article class="stat-card">
      <div><span>Total Patients</span><strong>{{ assessments|length }}</strong></div>
      <div class="stat-icon blue"><i data-lucide="users"></i></div>
    </article>
    <article class="stat-card">
      <div><span>Assessments</span><strong>{{ assessments|length }}</strong></div>
      <div class="stat-icon green"><i data-lucide="activity"></i></div>
    </article>
    <article class="stat-card">
      <div><span>High Risk Cases</span><strong>{% if latest_assessment and latest_assessment.severity == "High" %}1{% else %}0{% endif %}</strong></div>
      <div class="stat-icon red"><i data-lucide="triangle-alert"></i></div>
    </article>
    <article class="stat-card">
      <div><span>Avg Risk Score</span><strong>{% if latest_assessment %}{{ latest_assessment.risk_score }}%{% else %}0%{% endif %}</strong></div>
      <div class="stat-icon purple"><i data-lucide="clipboard-list"></i></div>
    </article>
  </section>

  <section class="grid-3 section reveal" style="padding-top:48px;">
    <article class="card">
      <div class="card-icon"><i data-lucide="activity"></i></div>
      <h3>Latest Assessment</h3>
      {% if latest_assessment %}
        <p><strong>{{ latest_assessment.risk_score }}% {{ latest_assessment.severity }} risk</strong></p>
        <p>{{ latest_assessment.created_at|date:"M d, Y H:i" }}</p>
      {% else %}
        <p>No clinical assessment has been saved for this account yet.</p>
      {% endif %}
    </article>
    <article class="card">
      <div class="card-icon"><i data-lucide="thermometer"></i></div>
      <h3>Latest Symptom Log</h3>
      {% if latest_log %}
        <p><strong>{{ latest_log.severity_average }}/10 average severity</strong></p>
        <p>Estimated risk trend: {{ latest_log.estimated_risk }}%</p>
      {% else %}
        <p>Start tracking your symptoms to build a trend profile.</p>
      {% endif %}
    </article>
    <article class="card">
      <div class="card-icon"><i data-lucide="bot"></i></div>
      <h3>AI Guidance</h3>
      <p>Get non-diagnostic lifestyle tips based on current symptom severity and your stored risk profile.</p>
      <a class="btn secondary" href="{% url 'patients:chatbot' %}">Open Chatbot</a>
    </article>
  </section>

  <section class="report-shell reveal">
    <article class="table-card">
      <table>
        <thead><tr><th>Date</th><th>Pain</th><th>Nausea</th><th>Heartburn</th><th>Risk Trend</th></tr></thead>
        <tbody>
          {% for log in symptom_logs %}
            <tr><td>{{ log.created_at|date:"M d, H:i" }}</td><td>{{ log.abdominal_pain }}/10</td><td>{{ log.nausea }}/10</td><td>{{ log.heartburn }}/10</td><td>{{ log.estimated_risk }}%</td></tr>
          {% empty %}
            <tr><td colspan="5">No symptom logs yet.</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </article>
    <aside class="form-card">
      <h2>Risk Visualization</h2>
      {% for assessment in assessments %}
        <div class="bar-row"><div class="bar-label"><span>{{ assessment.created_at|date:"M d" }} - {{ assessment.severity }}</span><strong>{{ assessment.risk_score }}%</strong></div><div class="gauge-track"><div class="gauge-fill" style="--value:{{ assessment.risk_score }}%;--bar-color:#2563eb"></div></div></div>
      {% empty %}
        <p class="muted">Run an assessment to display risk history.</p>
      {% endfor %}
      <div class="button-row"><a class="btn" href="{% url 'patients:symptom_log' %}"><i data-lucide="plus"></i> Add Symptom Log</a><a class="btn secondary" href="{% url 'patients:assessment' %}">New Assessment</a></div>
    </aside>
  </section>
</main>
{% endblock %}
```

## templates/patients/history.html
`$lang
{% extends "patients/base.html" %}
{% load patient_extras %}
{% block title %}Patient History | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero reveal">
    <p class="eyebrow"><i data-lucide="users"></i> Patient History Review</p>
    <h1>Patient Records</h1>
    <p class="lead">Review saved patients and their latest clinical predictions.</p>
  </section>
  <section class="section reveal" style="padding-top:8px;">
    <div class="table-card">
      <table>
        <thead><tr><th>Patient</th><th>Age</th><th>Latest Prediction</th><th>Clinical Notes</th><th>Report</th></tr></thead>
        <tbody>
          {% for patient in patients %}
            {% with latest=patient.assessments.first %}
              <tr>
                <td><strong>{{ patient.patient_code }}</strong><br><span class="muted">{{ patient.full_name }}</span></td>
                <td>{{ patient.age }}</td>
                <td>{% if latest %}<span class="badge {{ latest.severity|badge_class }}">{{ latest.severity }}</span> {{ latest.risk_score }}%{% else %}No prediction{% endif %}</td>
                <td>{% if latest %}{{ latest.symptoms|default:"No notes supplied." }}{% endif %}</td>
                <td>{% if latest %}<a class="btn secondary" href="{% url 'patients:report_detail' latest.id %}">View</a>{% endif %}</td>
              </tr>
            {% endwith %}
          {% empty %}
            <tr><td colspan="5">No patient records yet.</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </section>
</main>
{% endblock %}
```

## templates/patients/predictions.html
`$lang
{% extends "patients/base.html" %}
{% load patient_extras %}
{% block title %}Predictions | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero reveal">
    <p class="eyebrow"><i data-lucide="line-chart"></i> Prediction Results</p>
    <h1>Prediction Dashboard</h1>
    <p class="lead">Review model output, severity classification, and recommendation summaries.</p>
  </section>
  <section class="grid-3 section reveal" style="padding-top:8px;">
    {% for assessment in assessments %}
      <article class="card">
        <div class="card-icon"><i data-lucide="activity"></i></div>
        <h3>{{ assessment.patient.full_name }}</h3>
        <p><strong>{{ assessment.risk_score }}% {{ assessment.severity }} risk</strong></p>
        <p>{{ assessment.recommendations.0 }}</p>
        <p><span class="badge {{ assessment.severity|badge_class }}">{{ assessment.severity }}</span></p>
      </article>
    {% empty %}
      <article class="card"><h3>No Predictions Yet</h3><p>Run an assessment to generate prediction results.</p></article>
    {% endfor %}
  </section>
</main>
{% endblock %}
```

## templates/patients/reports.html
`$lang
{% extends "patients/base.html" %}
{% load patient_extras %}
{% block title %}Reports | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero reveal">
    <p class="eyebrow"><i data-lucide="file-down"></i> Report Generation</p>
    <h1>Clinical Reports</h1>
    <p class="lead">Generate and export patient prediction reports.</p>
  </section>
  <section class="section reveal" style="padding-top:8px;">
    <div class="table-card">
      <table>
        <thead><tr><th>Patient</th><th>Prediction</th><th>Date</th><th>Actions</th></tr></thead>
        <tbody>
          {% for assessment in assessments %}
            <tr>
              <td><strong>{{ assessment.patient.patient_code }}</strong><br>{{ assessment.patient.full_name }}</td>
              <td><span class="badge {{ assessment.severity|badge_class }}">{{ assessment.severity }}</span> {{ assessment.risk_score }}%</td>
              <td>{{ assessment.created_at|date:"M d, Y H:i" }}</td>
              <td><a class="btn secondary" href="{% url 'patients:report_detail' assessment.id %}">View</a> <a class="btn" href="{% url 'patients:export_report' assessment.id %}">Export</a></td>
            </tr>
          {% empty %}
            <tr><td colspan="4">No reports available yet.</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </section>
</main>
{% endblock %}
```

## templates/patients/report_detail.html
`$lang
{% extends "patients/base.html" %}
{% load patient_extras %}
{% block title %}Report | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero">
    <p class="eyebrow"><i data-lucide="file-text"></i> Clinical Report</p>
    <h1>{{ assessment.patient.full_name }}</h1>
    <p class="lead">{{ assessment.patient.patient_code }} â€¢ {{ assessment.risk_score }}% {{ assessment.severity }} risk</p>
  </section>
  <section class="report-shell">
    <article class="report-preview">
      <header>
        <div><h3>Intelligent PUD Management Report</h3><p class="muted">Simulated XGBoost prediction summary</p></div>
        <strong>{{ assessment.patient.patient_code }}</strong>
      </header>
      <section><h3>Patient</h3><p>{{ assessment.patient.full_name }}, {{ assessment.patient.age }} years</p></section>
      <section><h3>Health Metrics</h3><p>BP: {{ assessment.systolic_bp|default:"--" }}/{{ assessment.diastolic_bp|default:"--" }} mmHg Â· Weight: {{ assessment.weight|default:"--" }} kg</p></section>
      <section><h3>Prediction</h3><p><span class="badge {{ assessment.severity|badge_class }}">{{ assessment.severity }}</span> {{ assessment.risk_score }}% estimated PUD management risk</p></section>
      <section><h3>Clinical Notes</h3><p>{{ assessment.symptoms|default:"No additional notes supplied." }}</p></section>
      <section><h3>Recommendations</h3><ul class="recommendations">{% for item in assessment.recommendations %}<li>{{ item }}</li>{% endfor %}</ul></section>
    </article>
    <aside class="form-card">
      <h2>Feature Importance</h2>
      {% for name, value in assessment.feature_importance.items %}
        <div class="bar-row"><div class="bar-label"><span>{{ name }}</span><strong>{{ value }}%</strong></div><div class="gauge-track"><div class="gauge-fill" style="--value:{{ value }}%;--bar-color:#2563eb"></div></div></div>
      {% empty %}
        <p class="muted">No feature importance data available.</p>
      {% endfor %}
      <div class="button-row">
        <a class="btn" href="{% url 'patients:export_report' assessment.id %}"><i data-lucide="download"></i> Export Report</a>
        <a class="btn secondary" href="{% url 'patients:assessment' %}"><i data-lucide="plus"></i> New Assessment</a>
      </div>
    </aside>
  </section>
</main>
{% endblock %}
```

## templates/patients/symptom_log.html
`$lang
{% extends "patients/base.html" %}
{% block title %}Symptom Log | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero reveal">
    <p class="eyebrow"><i data-lucide="clipboard-plus"></i> Health Metrics</p>
    <h1>Track Symptoms</h1>
    <p class="lead">Record current symptom levels and update your patient risk trend.</p>
  </section>
  <section class="form-grid reveal">
    <form class="form-card" method="post">
      {% csrf_token %}
      <div class="field-grid">
        {% for field in form %}
          <div class="field {% if field.name == 'notes' %}full{% endif %}">{{ field.label_tag }}{{ field }}{% for error in field.errors %}<span class="muted">{{ error }}</span>{% endfor %}</div>
        {% endfor %}
      </div>
      <div class="button-row">
        <button class="btn" type="submit"><i data-lucide="save"></i> Save Symptom Log</button>
        <a class="btn secondary" href="{% url 'patients:dashboard' %}">Dashboard</a>
      </div>
    </form>
    <aside class="result-panel">
      <p class="eyebrow"><i data-lucide="shield-alert"></i> Safety Note</p>
      <h2>Non-Diagnostic Tracking</h2>
      <ul class="recommendations">
        <li>This tracker supports personal monitoring and clinical discussion.</li>
        <li>Seek urgent medical care for black stools, vomiting blood, fainting, severe sudden pain, or persistent vomiting.</li>
        {% if latest_assessment %}<li>Your latest model risk is {{ latest_assessment.risk_score }}% {{ latest_assessment.severity }}.</li>{% endif %}
      </ul>
    </aside>
  </section>
</main>
{% endblock %}
```

## templates/patients/chatbot.html
`$lang
{% extends "patients/base.html" %}
{% block title %}AI Chatbot | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero reveal">
    <p class="eyebrow"><i data-lucide="bot"></i> AI Lifestyle Guidance</p>
    <h1>PUD Guidance Chatbot</h1>
    <p class="lead">Ask for non-diagnostic, evidence-informed lifestyle tips based on symptom severity and historical risk profile.</p>
  </section>
  <section class="report-shell reveal">
    <form class="form-card" method="post">
      {% csrf_token %}
      <div class="field-grid">
        {% for field in form %}
          <div class="field full">{{ field.label_tag }}{{ field }}{% for error in field.errors %}<span class="muted">{{ error }}</span>{% endfor %}</div>
        {% endfor %}
      </div>
      <div class="button-row">
        <button class="btn" type="submit"><i data-lucide="send"></i> Ask Chatbot</button>
        <a class="btn secondary" href="{% url 'patients:dashboard' %}">Dashboard</a>
      </div>
    </form>
    <article class="report-preview">
      <header>
        <div><h3>Guidance Response</h3><p class="muted">Educational support only, not a diagnosis.</p></div>
        <strong>AI</strong>
      </header>
      <section>
        {% if response %}
          <ul class="recommendations">{% for item in response %}<li>{{ item }}</li>{% endfor %}</ul>
        {% else %}
          <p class="muted">Submit a question to receive personalized educational guidance.</p>
        {% endif %}
      </section>
      <section>
        <h3>Profile Context</h3>
        <p>{% if latest_assessment %}Latest stored risk: {{ latest_assessment.risk_score }}% {{ latest_assessment.severity }}.{% else %}No stored assessment yet.{% endif %}</p>
        <p>Recent symptom logs: {{ recent_logs|length }}</p>
      </section>
    </article>
  </section>
</main>
{% endblock %}
```

## templates/patients/architecture.html
`$lang
{% extends "patients/base.html" %}
{% load static %}
{% block title %}Architecture | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero">
    <p class="eyebrow"><i data-lucide="network"></i> System Analysis</p>
    <h1>Architecture and Flow Diagrams</h1>
    <p class="lead">The Django views, model layer, database storage, prediction workflow, and reports follow the supplied system analysis diagrams.</p>
  </section>
  <section class="diagram-grid">
    <article class="diagram-card wide"><img src="{% static 'assets/layer-flow.png' %}" alt="Layered architecture"><div class="diagram-caption"><h3>Layered Architecture</h3><p class="muted">Presentation, application, simulated model processing, results visualization, and database storage.</p></div></article>
    <article class="diagram-card"><img src="{% static 'assets/patient-data-processing.png' %}" alt="Patient data processing"><div class="diagram-caption"><h3>Patient Data Processing</h3><p class="muted">Login, data entry, validation, prediction, recommendations, and report export.</p></div></article>
    <article class="diagram-card"><img src="{% static 'assets/pud-prediction-context.png' %}" alt="Prediction context"><div class="diagram-caption"><h3>Prediction Context</h3><p class="muted">Patient data enters the system and returns prediction reports.</p></div></article>
    <article class="diagram-card wide"><img src="{% static 'assets/pud-use-cases.png' %}" alt="Use case diagram"><div class="diagram-caption"><h3>Use Case Model</h3><p class="muted">Clinicians and patients use login, data entry, history review, prediction, and report export.</p></div></article>
  </section>
</main>
{% endblock %}
```

## templates/registration/login.html
`$lang
{% extends "patients/base.html" %}
{% block title %}Login | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero">
    <p class="eyebrow"><i data-lucide="lock"></i> Secure Access</p>
    <h1>Patient Login</h1>
    <p class="lead">Access your private symptom tracker, risk history, and AI guidance workspace.</p>
  </section>
  <section class="form-grid">
    <form class="form-card" method="post">
      {% csrf_token %}
      <div class="field-grid">
        {% for field in form %}
          <div class="field full">{{ field.label_tag }}{{ field }}{% for error in field.errors %}<span class="muted">{{ error }}</span>{% endfor %}</div>
        {% endfor %}
      </div>
      <div class="button-row">
        <button class="btn" type="submit"><i data-lucide="log-in"></i> Login</button>
        <a class="btn secondary" href="{% url 'patients:register' %}">Create Account</a>
      </div>
    </form>
  </section>
</main>
{% endblock %}
```

## templates/registration/register.html
`$lang
{% extends "patients/base.html" %}
{% block title %}Register | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero">
    <p class="eyebrow"><i data-lucide="user-plus"></i> Secure Patient Account</p>
    <h1>Create Account</h1>
    <p class="lead">Create a protected account for patient dashboard access.</p>
  </section>
  <section class="form-grid">
    <form class="form-card" method="post">
      {% csrf_token %}
      <div class="field-grid">
        {% for field in form %}
          <div class="field full">{{ field.label_tag }}{{ field }}{% for error in field.errors %}<span class="muted">{{ error }}</span>{% endfor %}</div>
        {% endfor %}
      </div>
      <div class="button-row">
        <button class="btn" type="submit"><i data-lucide="shield-check"></i> Create Account</button>
        <a class="btn secondary" href="{% url 'login' %}">Login</a>
      </div>
    </form>
  </section>
</main>
{% endblock %}
```

## templates/registration/logged_out.html
`$lang
{% extends "patients/base.html" %}
{% block title %}Logged Out | PUDPredict{% endblock %}
{% block content %}
<main class="page">
  <section class="page-hero">
    <p class="eyebrow"><i data-lucide="shield"></i> Session Ended</p>
    <h1>You are logged out</h1>
    <p class="lead">Your secure patient session has ended.</p>
    <div class="button-row" style="justify-content:center;"><a class="btn" href="{% url 'login' %}">Login Again</a></div>
  </section>
</main>
{% endblock %}
```

## examples/sample_patient.json
`$lang
{
  "name": "Demo Patient",
  "age": 42,
  "pain_severity": 3,
  "hpylori_status": "unknown",
  "nsaid_use": "sometimes",
  "bleeding_symptoms": "no",
  "smoking_history": "no",
  "alcohol_intake": "moderate",
  "stress_level": "high"
}
```

## tests/test_model.py
`$lang
from ulcerboost.model import predict_ulcer_risk


def test_high_risk_prediction():
    result = predict_ulcer_risk(
        {
            "age": 62,
            "pain_severity": 3,
            "hpylori_status": "positive",
            "nsaid_use": "yes",
            "bleeding_symptoms": "yes",
            "smoking_history": "yes",
            "alcohol_intake": "high",
            "stress_level": "high",
        }
    )
    assert result["severity"] == "High"
    assert result["risk_score"] >= 70
```
