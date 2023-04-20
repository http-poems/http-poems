# Generated by Django 4.1.7 on 2023-04-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Poet",
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
                ("name", models.CharField(max_length=64, verbose_name="نام")),
                (
                    "fa_surname",
                    models.CharField(max_length=32, null=True, verbose_name="تخلص"),
                ),
                (
                    "en_surname",
                    models.CharField(
                        editable=False,
                        max_length=32,
                        null=True,
                        unique=True,
                        verbose_name="تخلص (انگلیسی)",
                    ),
                ),
                (
                    "biography",
                    models.TextField(
                        max_length=1024, null=True, verbose_name="زندگینامه"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        help_text="چهرک سراینده",
                        null=True,
                        upload_to="poets/avatars/",
                        verbose_name="آواتار",
                    ),
                ),
                (
                    "ganjoor_link",
                    models.URLField(
                        help_text="پیوند نمایه سراینده در وبسایت گنجور",
                        verbose_name="پیوند گنچور",
                    ),
                ),
            ],
            options={
                "verbose_name": "سراینده",
                "verbose_name_plural": "سرایندگان",
            },
        ),
    ]
