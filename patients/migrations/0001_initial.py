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
