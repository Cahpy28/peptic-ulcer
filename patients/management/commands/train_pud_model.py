from django.core.management.base import BaseCommand, CommandError

from patients.model_training import train_pud_model


class Command(BaseCommand):
    help = "Train the PUDPredict XGBoost classifier from approved, labeled PUD dataset CSV/Parquet files."

    def add_arguments(self, parser):
        parser.add_argument("datasets", nargs="+", help="Paths to labeled CSV/Parquet files exported from MIMIC-IV, MIMIC-IV-ED, eICU, NHANES, or curated clinical data.")

    def handle(self, *args, **options):
        try:
            metrics = train_pud_model(options["datasets"])
        except Exception as exc:
            raise CommandError(str(exc)) from exc
        self.stdout.write(self.style.SUCCESS("PUD XGBoost model trained and saved."))
        for key, value in metrics.items():
            self.stdout.write(f"{key}: {value}")
