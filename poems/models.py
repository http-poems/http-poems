from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusCode(models.Model):
    code = models.IntegerField(verbose_name=_("کد وضعیت"))
    description = models.TextField(verbose_name=_("توضیحات"))

    class Meta:
        verbose_name = _("کد وضعیت")
        verbose_name_plural = _("کد‌های وضعیت")


class Poet(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("نام"))
    pseudonym = models.CharField(max_length=100, verbose_name=_("تخلص"))
    biography = models.TextField(max_length=1024, verbose_name=_("زندگینامه"))
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
        on_delete=models.CASCADE,
        verbose_name=_("کد وضعیت"),
        help_text=_("کد وضعیتی که این بیت سروده آن را توصیف می‌کند"),
    )
    ganjoor_link = models.URLField(
        max_length=200,
        verbose_name=_("پیوند گنچور"),
        help_text=_("پیوتد قطعه کامل سروده در وبسایت گنجور"),
    )

    class Meta:
        verbose_name = _("بیت سروده")
        verbose_name_plural = _("ابیات")
