# Generated by Django 4.2.16 on 2024-09-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TgUser",
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
                ("tg_url", models.URLField()),
                ("tg_name", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("photo", models.ImageField(upload_to="images")),
                ("description", models.TextField()),
            ],
        ),
    ]
