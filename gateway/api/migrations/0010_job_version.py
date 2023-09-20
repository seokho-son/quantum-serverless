# Generated by Django 4.2.4 on 2023-09-20 17:35

import concurrency.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0009_alter_job_logs"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="version",
            field=concurrency.fields.IntegerVersionField(
                default=0, help_text="record revision number"
            ),
        ),
    ]
