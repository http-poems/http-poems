from django.db import models
from django.utils.translation import gettext_lazy as _

from poems.choices import StatusCodeGroupChoices
from poems.managers import RandomManager


class StatusCode(models.Model):
    code = models.IntegerField(verbose_name=_("کد وضعیت"), unique=True)
    title = models.CharField(
        null=True, blank=False, max_length=32, verbose_name=_("عنوان")
    )
    group = models.PositiveSmallIntegerField(
        choices=StatusCodeGroupChoices.choices, verbose_name=_("گروه پاسخ")
    )
    description = models.TextField(null=True, blank=True, verbose_name=_("توضیحات"))
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


class Poet(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("نام"))
    fa_surname = models.CharField(
        null=True, blank=False, max_length=32, verbose_name=_("تخلص")
    )
    en_surname = models.CharField(
        null=True, blank=False, max_length=32, verbose_name=_("تخلص (انگلیسی)")
    )
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


class Poem(models.Model):
    lyric = models.CharField(max_length=255, verbose_name=_("بیت سروده"))
    poet = models.ForeignKey(
        Poet,
        on_delete=models.CASCADE,
        verbose_name=_("سراینده"),
        help_text=_("نام سراینده این بیت سروده"),
    )
    status_code = models.ForeignKey(
        StatusCode,
        to_field="code",
        on_delete=models.CASCADE,
        verbose_name=_("کد وضعیت"),
        help_text=_("کد وضعیتی که این بیت سروده آن را توصیف می‌کند"),
    )
    ganjoor_link = models.URLField(
        max_length=200,
        verbose_name=_("پیوند گنچور"),
        help_text=_("پیوتد قطعه کامل سروده در وبسایت گنجور"),
    )
    objects = RandomManager()

    class Meta:
        verbose_name = _("بیت سروده")
        verbose_name_plural = _("ابیات")
