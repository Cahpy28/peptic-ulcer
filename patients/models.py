from django.db import models
from django.conf import settings
from django.utils import timezone


class EmailVerificationCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="email_verification_codes")
    code = models.CharField(max_length=6)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)
    attempts = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"{self.user.email} verification code"


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


class PUDDatasetUpload(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processed", "Processed"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pud_dataset_uploads")
    file = models.FileField(upload_to="datasets/")
    original_filename = models.CharField(max_length=255)
    row_count = models.PositiveIntegerField(default=0)
    column_profile = models.JSONField(default=dict)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="pending")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.original_filename} ({self.status})"


class ClinicalReference(models.Model):
    source = models.CharField(max_length=40, default="PubMed")
    query = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    url = models.URLField(blank=True)
    published = models.CharField(max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class DrugSafetyWarning(models.Model):
    medication = models.CharField(max_length=120)
    warning = models.TextField()
    source_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.medication


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
    diagnosis = models.CharField(max_length=160, blank=True)
    medications = models.TextField(blank=True)
    complications = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    predicted_ulcer_type = models.CharField(max_length=80, default="Not indicated")
    is_pud_positive = models.BooleanField(default=False)
    prediction_details = models.JSONField(default=dict)
    research_references = models.JSONField(default=list)
    drug_warnings = models.JSONField(default=list)
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

