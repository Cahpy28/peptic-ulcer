from django.urls import path

from . import views


app_name = "patients"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("register/", views.register, name="register"),
    path("verify-email/sent/", views.verification_sent, name="verification_sent"),
    path("verify-email/resend/", views.resend_verification, name="resend_verification"),
    path("verify-email/<uidb64>/<token>/", views.verify_email, name="verify_email"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("assessment/", views.assessment_create, name="assessment"),
    path("symptoms/new/", views.symptom_log_create, name="symptom_log"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("data-layer/", views.data_layer, name="data_layer"),
    path("patients/", views.patient_history, name="history"),
    path("patients/<int:patient_id>/delete/", views.delete_patient, name="delete_patient"),
    path("predictions/", views.prediction_results, name="predictions"),
    path("reports/", views.reports, name="reports"),
    path("reports/<int:assessment_id>/", views.report_detail, name="report_detail"),
    path("reports/<int:assessment_id>/export/", views.export_report, name="export_report"),
    path("architecture/", views.architecture, name="architecture"),
]



