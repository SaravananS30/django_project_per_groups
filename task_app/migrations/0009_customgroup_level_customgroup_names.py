# Generated by Django 4.2.5 on 2023-09-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_app", "0008_customgroup"),
    ]

    operations = [
        migrations.AddField(
            model_name="customgroup",
            name="level",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="customgroup",
            name="names",
            field=models.CharField(default=True, max_length=100),
        ),
    ]