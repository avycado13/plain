# Generated by Plain 5.0.dev20231229213240 on 2023-12-30 02:35

from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plainworker", "0006_rename_completed_at_jobresult_ended_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobresult",
            name="status",
            field=models.CharField(
                required=False,
                choices=[
                    ("", "Unknown"),
                    ("PROCESSING", "Processing"),
                    ("SUCCESSFUL", "Successful"),
                    ("ERRORED", "Errored"),
                ],
                default="",
                max_length=20,
            ),
        ),
    ]
