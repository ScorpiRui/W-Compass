# Generated by Django 4.1.7 on 2024-04-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Locations",
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
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="logo",
            field=models.ImageField(default=None, upload_to="logos/"),
        ),
        migrations.AddField(
            model_name="company",
            name="location",
            field=models.ManyToManyField(to="main.locations"),
        ),
    ]
