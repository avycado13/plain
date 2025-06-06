# Generated by Plain 0.32.0 on 2025-03-10 15:40

from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("plainpageviews", "0004_alter_pageview_uuid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pageview",
            name="session_key",
            field=models.CharField(max_length=255, required=False),
        ),
        migrations.AlterField(
            model_name="pageview",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="pageview",
            name="url",
            field=models.URLField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="pageview",
            name="user_id",
            field=models.CharField(max_length=255, required=False),
        ),
        migrations.AddIndex(
            model_name="pageview",
            index=models.Index(
                fields=["timestamp"], name="plainpagevi_timesta_da4eb2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pageview",
            index=models.Index(
                fields=["user_id"], name="plainpagevi_user_id_b40ca5_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pageview",
            index=models.Index(
                fields=["session_key"], name="plainpagevi_session_5545cf_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pageview",
            index=models.Index(fields=["url"], name="plainpagevi_url_d3e821_idx"),
        ),
    ]
