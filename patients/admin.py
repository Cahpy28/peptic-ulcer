from django.contrib import admin

from .models import Assessment, ClinicalReference, DrugSafetyWarning, Patient, PUDDatasetUpload, SymptomLog


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


@admin.register(PUDDatasetUpload)
class PUDDatasetUploadAdmin(admin.ModelAdmin):
    list_display = ("original_filename", "user", "row_count", "status", "created_at")
    search_fields = ("original_filename", "message")
    list_filter = ("status", "created_at")


@admin.register(ClinicalReference)
class ClinicalReferenceAdmin(admin.ModelAdmin):
    list_display = ("source", "query", "title", "published", "created_at")
    search_fields = ("query", "title")
    list_filter = ("source", "created_at")


@admin.register(DrugSafetyWarning)
class DrugSafetyWarningAdmin(admin.ModelAdmin):
    list_display = ("medication", "created_at")
    search_fields = ("medication", "warning")
