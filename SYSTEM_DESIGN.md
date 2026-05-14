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
