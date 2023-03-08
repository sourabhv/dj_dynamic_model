# Generated by Django 4.1.7 on 2023-03-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Field",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("TextField", "TextField"),
                            ("IntegerField", "IntegerField"),
                            ("DecimalField", "DecimalField"),
                            ("DateField", "DateField"),
                            ("DateTimeField", "DateTimeField"),
                            ("BooleanField", "BooleanField"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
            options={
                "db_table": "fields",
            },
        ),
    ]