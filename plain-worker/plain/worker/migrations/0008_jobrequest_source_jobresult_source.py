# Generated by Plain 5.0.dev20240102205958 on 2024-01-02 21:12

from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plainworker", "0007_alter_jobresult_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobrequest",
            name="source",
            field=models.TextField(required=False),
        ),
        migrations.AddField(
            model_name="jobresult",
            name="source",
            field=models.TextField(required=False),
        ),
    ]
