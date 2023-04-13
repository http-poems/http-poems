from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.poems.managers import RandomManager
from apps.poets.models import Poet
from apps.status_codes.models import StatusCode


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

    def __str__(self):
        first_verse = self.lyric.split("\t")[0]
        return first_verse
