# Generated by Django 5.0 on 2023-12-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medley",
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
                ("Tune1", models.CharField(max_length=200)),
                ("Tune2", models.CharField(blank=True, max_length=200)),
                ("Tune3", models.CharField(blank=True, max_length=200)),
                ("earliest_play", models.DateField(blank=True, null=True)),
                ("latest_play", models.DateField(blank=True, null=True)),
                ("bands", models.CharField(blank=True, max_length=200)),
                ("keys", models.CharField(blank=True, max_length=32)),
                ("comments", models.CharField(blank=True, max_length=4000)),
                ("additional_notes", models.CharField(blank=True, max_length=4000)),
                (
                    "medley_type",
                    models.CharField(
                        choices=[
                            ("Contra", "Contra"),
                            ("Unplayed", "Unplayed Contra"),
                            ("Waltz", "Waltz"),
                            ("Polka", "Polka"),
                            ("English Ceildh", "English Ceildh"),
                            (
                                "Northumbrian Pipe and Fiddle",
                                "Northumbrian Pipe and Fiddle",
                            ),
                        ],
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Song",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.CharField(blank=True, max_length=4000)),
                ("abc", models.CharField(max_length=4000)),
            ],
        ),
    ]
