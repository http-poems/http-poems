from django.db import models
from django.utils.translation import gettext_lazy as _


class Poet(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name=_("تخلص (انگلیسی)"), editable=False)
    name = models.CharField(max_length=64, null=True, blank=False, verbose_name=_("نام"))
    surname = models.CharField(max_length=32, verbose_name=_("تخلص"), help_text=_("چیزی که سراینده بدان ملقب است."))
    biography = models.TextField(null=True, blank=False, max_length=1024, verbose_name=_("زندگینامه"))
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="poets/avatars/",
        verbose_name=_("آواتار"),
        help_text=_("چهرک سراینده"),
    )
    ganjoor_link = models.URLField(
        max_length=200,
        verbose_name=_("پیوند گنچور"),
        help_text=_("پیوند نمایه سراینده در وبسایت گنجور"),
    )

    class Meta:
        verbose_name = _("سراینده")
        verbose_name_plural = _("سرایندگان")

    def __str__(self):
        return self.surname
