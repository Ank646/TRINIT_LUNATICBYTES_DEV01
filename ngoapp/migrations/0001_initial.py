# Generated by Django 4.1.5 on 2023-02-11 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ngo",
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
                ("ngoregid", models.TextField()),
                ("ngoaddress", models.TextField(blank=True)),
                ("ngofundneeds", models.TextField(blank=True)),
                ("ngotype", models.CharField(blank=True, max_length=100)),
                ("ngocity", models.TextField(blank=True)),
                ("ngoplan", models.TextField(blank=True)),
                ("ngoendgoal", models.TextField(blank=True)),
                ("ngogoal", models.TextField(blank=True)),
                ("ngowork", models.TextField(blank=True)),
                ("ngovision", models.TextField(blank=True)),
                ("ngoabout", models.TextField(blank=True)),
                ("ngofb", models.TextField(blank=True)),
                ("ngoinsta", models.TextField(blank=True)),
                ("ngolinked", models.TextField(blank=True)),
                ("ngoweb", models.TextField(blank=True)),
                (
                    "ngoname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
