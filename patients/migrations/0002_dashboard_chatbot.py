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
