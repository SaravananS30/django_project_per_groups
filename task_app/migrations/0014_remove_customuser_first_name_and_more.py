# Generated by Django 4.2.5 on 2023-09-20 11:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_app", "0013_remove_custompermission_resource"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="last_name",
        ),
    ]
