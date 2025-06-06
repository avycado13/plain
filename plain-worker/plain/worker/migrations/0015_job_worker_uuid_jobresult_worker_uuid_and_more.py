# Generated by Plain 5.0.dev20240118212224 on 2024-01-18 21:53

from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plainworker", "0014_job_unique_key_jobrequest_unique_key_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="worker_uuid",
            field=models.UUIDField(required=False, allow_null=True),
        ),
        migrations.AddField(
            model_name="jobresult",
            name="worker_uuid",
            field=models.UUIDField(required=False, allow_null=True),
        ),
        migrations.AlterField(
            model_name="jobresult",
            name="status",
            field=models.CharField(
                choices=[
                    ("SUCCESSFUL", "Successful"),
                    ("ERRORED", "Errored"),
                    ("CANCELLED", "Cancelled"),
                    ("LOST", "Lost"),
                ],
                max_length=20,
            ),
        ),
    ]
