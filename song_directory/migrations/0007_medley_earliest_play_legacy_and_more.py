# Generated by Django 5.0 on 2023-12-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("song_directory", "0006_rename_uploader_id_medley_uploader_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="medley",
            name="earliest_play_legacy",
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name="medley",
            name="latest_play_legacy",
            field=models.CharField(blank=True, max_length=32),
        ),
    ]