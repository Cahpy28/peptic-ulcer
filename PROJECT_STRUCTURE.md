# Project Structure

```text
PEPTIC ULCER DISEASE/
├── manage.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── INSTALLATION_STEPS.md
├── SYSTEM_DESIGN.md
├── PROJECT_STRUCTURE.md
├── database_schema.sql
├── db.sqlite3
├── pudpredict/                  # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── patients/                    # Backend application logic
│   ├── models.py                # Patient, assessment, and symptom data models
│   ├── forms.py                 # Login-adjacent forms, assessment forms, chatbot forms
│   ├── views.py                 # Access-controlled pages and report generation
│   ├── urls.py                  # Application routes
│   ├── ml.py                    # Simulated XGBoost prediction and AI advisor guidance
│   ├── admin.py
│   ├── migrations/
│   └── templatetags/
├── templates/                   # Django HTML templates
│   ├── patients/                # Main app pages
│   └── registration/            # Login, create account, logout pages
├── frontend/                    # Frontend source/static files
│   └── static/
│       ├── css/
│       │   └── styles.css
│       ├── js/
│       │   └── app.js
│       └── assets/
│           ├── pudpredict-favicon.svg
│           ├── layer-flow.png
│           ├── patient-data-processing.png
│           ├── pud-prediction-context.png
│           └── pud-use-cases.png
├── examples/
│   └── static-prototypes/       # Old standalone prototype HTML references
├── src/ulcerboost/              # Optional API/model/storage module scaffold
└── tests/
```

## Backend Paths

- Django settings: `pudpredict/settings.py`
- Project URLs: `pudpredict/urls.py`
- Patient app URLs: `patients/urls.py`
- Main backend views: `patients/views.py`
- Database models: `patients/models.py`
- Forms and validation: `patients/forms.py`
- Prediction and AI advisor logic: `patients/ml.py`

## Frontend Paths

- HTML templates: `templates/patients/` and `templates/registration/`
- Main stylesheet: `frontend/static/css/styles.css`
- Main JavaScript: `frontend/static/js/app.js`
- Images and favicon: `frontend/static/assets/`

Django loads frontend assets through `STATICFILES_DIRS = [BASE_DIR / "frontend" / "static"]`.
```
