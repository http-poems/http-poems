# Generated by Django 4.1.7 on 2023-04-22 02:45

import apps.poems.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("status_codes", "0001_initial"),
        ("poets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poem",
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
                (
                    "uid",
                    models.CharField(
                        default=apps.poems.utils.random_uid_generator,
                        editable=False,
                        max_length=8,
                        unique=True,
                    ),
                ),
                ("lyric", models.TextField(max_length=256, verbose_name="سروده")),
                (
                    "ganjoor_link",
                    models.URLField(
                        help_text="پیوتد سروده در وبسایت گنجور",
                        verbose_name="پیوند گنچور",
                    ),
                ),
                (
                    "poet",
                    models.ForeignKey(
                        help_text="سراینده این سروده",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="poets.poet",
                        verbose_name="سراینده",
                    ),
                ),
                (
                    "status_code",
                    models.ForeignKey(
                        help_text="کد وضعیتی که این سروده آن را توصیف می\u200cکند",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="status_codes.statuscode",
                        verbose_name="کد وضعیت",
                    ),
                ),
            ],
            options={
                "verbose_name": "بیت سروده",
                "verbose_name_plural": "ابیات",
            },
        ),
    ]
