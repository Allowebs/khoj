# Generated by Django 4.2.10 on 2024-03-23 16:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0032_merge_20240322_0427"),
    ]

    operations = [
        migrations.RenameField(
            model_name="agent",
            old_name="tuning",
            new_name="personality",
        ),
    ]