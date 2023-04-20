# Generated by Django 4.1.7 on 2023-04-20 23:16

import apps.poems.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("poets", "0001_initial"),
        ("status_codes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poem",
            fields=[
                (
                    "uid",
                    models.CharField(
                        default=apps.poems.utils.random_uid_generator,
                        editable=False,
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("lyric", models.CharField(max_length=255, verbose_name="بیت سروده")),
                (
                    "ganjoor_link",
                    models.URLField(
                        help_text="پیوتد قطعه کامل سروده در وبسایت گنجور",
                        verbose_name="پیوند گنچور",
                    ),
                ),
                (
                    "poet",
                    models.ForeignKey(
                        editable=False,
                        help_text="نام سراینده این بیت سروده",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="poets.poet",
                        to_field="en_surname",
                        verbose_name="سراینده",
                    ),
                ),
                (
                    "status_code",
                    models.ForeignKey(
                        help_text="کد وضعیتی که این بیت سروده آن را توصیف می\u200cکند",
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
