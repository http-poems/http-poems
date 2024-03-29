# Generated by Django 4.1.7 on 2023-04-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StatusCode",
            fields=[
                (
                    "code",
                    models.IntegerField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="کد وضعیت",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=32, null=True, verbose_name="عنوان"),
                ),
                (
                    "group",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Informational"),
                            (2, "Successful"),
                            (3, "Redirection"),
                            (4, "Client Error"),
                            (5, "Server Error"),
                        ],
                        verbose_name="گروه پاسخ",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="توضیحات"),
                ),
                (
                    "mdn_link",
                    models.URLField(
                        blank=True,
                        help_text="پیوند کد وضعیت مربوطه در وبسایت mdn",
                        null=True,
                        verbose_name="پیوند mdn",
                    ),
                ),
            ],
            options={
                "verbose_name": "کد وضعیت",
                "verbose_name_plural": "کد\u200cهای وضعیت",
                "ordering": ("code",),
            },
        ),
    ]
