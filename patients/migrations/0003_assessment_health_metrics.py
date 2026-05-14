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
