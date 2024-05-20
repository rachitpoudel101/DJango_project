# Generated by Django 5.0.6 on 2024-05-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Projects",
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
                ("title", models.CharField(max_length=50)),
                ("discription", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="portfolio/images/")),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]