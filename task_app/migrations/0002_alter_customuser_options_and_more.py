# Generated by Django 4.2.5 on 2023-09-19 06:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={},
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
    ]