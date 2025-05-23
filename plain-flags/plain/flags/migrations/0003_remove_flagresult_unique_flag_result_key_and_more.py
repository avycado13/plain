# Generated by Plain 0.31.0 on 2025-03-08 21:33

import uuid

import plain.flags.models
from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plainflags", "0002_alter_flagresult_unique_together_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="flagresult",
            name="unique_flag_result_key",
        ),
        migrations.AlterField(
            model_name="flag",
            name="name",
            field=models.CharField(
                max_length=255, validators=[plain.flags.models.validate_flag_name]
            ),
        ),
        migrations.AlterField(
            model_name="flag",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="flagresult",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddConstraint(
            model_name="flag",
            constraint=models.UniqueConstraint(
                fields=("name",), name="plainflags_flag_unique_name"
            ),
        ),
        migrations.AddConstraint(
            model_name="flag",
            constraint=models.UniqueConstraint(
                fields=("uuid",), name="plainflags_flag_unique_uuid"
            ),
        ),
        migrations.AddConstraint(
            model_name="flagresult",
            constraint=models.UniqueConstraint(
                fields=("flag", "key"), name="plainflags_flagresult_unique_key"
            ),
        ),
        migrations.AddConstraint(
            model_name="flagresult",
            constraint=models.UniqueConstraint(
                fields=("uuid",), name="plainflags_flagresult_unique_uuid"
            ),
        ),
    ]
