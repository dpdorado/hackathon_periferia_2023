# Generated by Django 4.2.1 on 2023-05-07 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mutants", "0004_alter_person_dna"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stats",
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
                ("count_mutant_dna", models.IntegerField(default=0)),
                ("count_human_dna", models.IntegerField(default=0)),
                ("ratio", models.FloatField(default=0)),
            ],
        ),
    ]
