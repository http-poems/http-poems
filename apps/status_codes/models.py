from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.status_codes.choices import StatusCodeGroupChoices


# Create your models here.
class StatusCode(models.Model):
    code = models.IntegerField(
        verbose_name=_("کد وضعیت"), primary_key=True, editable=False
    )
    title = models.CharField(
        null=True, blank=False, max_length=32, verbose_name=_("عنوان")
    )
    group = models.PositiveSmallIntegerField(
        choices=StatusCodeGroupChoices.choices, verbose_name=_("گروه پاسخ")
    )
    description = models.TextField(
        null=True, blank=True, verbose_name=_("توضیحات")
    )
    mdn_link = models.URLField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name=_("پیوند mdn"),
        help_text=_("پیوند کد وضعیت مربوطه در وبسایت mdn"),
    )

    class Meta:
        ordering = ("code",)
        verbose_name = _("کد وضعیت")
        verbose_name_plural = _("کد‌های وضعیت")

    def __str__(self):
        return f"({self.title}) {self.code}"

    @property
    def group_label(self):
        return StatusCodeGroupChoices(self.group).label
