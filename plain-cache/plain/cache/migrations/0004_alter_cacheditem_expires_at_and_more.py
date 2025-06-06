# Generated by Plain 0.32.0 on 2025-03-10 15:34

from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plaincache", "0003_alter_cacheditem_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cacheditem",
            name="expires_at",
            field=models.DateTimeField(allow_null=True, required=False),
        ),
        migrations.AddIndex(
            model_name="cacheditem",
            index=models.Index(
                fields=["expires_at"], name="plaincache__expires_5a9119_idx"
            ),
        ),
    ]
