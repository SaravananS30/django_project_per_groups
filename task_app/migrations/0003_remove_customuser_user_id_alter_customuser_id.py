# Generated by Django 4.2.5 on 2023-09-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_app", "0002_alter_customuser_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="user_id",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.CharField(
                max_length=8, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
