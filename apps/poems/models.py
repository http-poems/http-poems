from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.poems.managers import RandomManager
from apps.poems.utils import random_uid_generator
from apps.poets.models import Poet
from apps.status_codes.models import StatusCode


class Poem(models.Model):
    uid = models.CharField(primary_key=True, max_length=8, default=random_uid_generator, editable=False)
    lyric = models.TextField(max_length=256, null=False, blank=False, verbose_name=_("سروده"))
    poet = models.ForeignKey(
        Poet,
        on_delete=models.CASCADE,
        verbose_name=_("سراینده"),
        help_text=_("سراینده این سروده"),
    )
    status_code = models.ForeignKey(
        StatusCode,
        to_field="code",
        on_delete=models.CASCADE,
        verbose_name=_("کد وضعیت"),
        help_text=_("کد وضعیتی که این سروده آن را توصیف می‌کند"),
    )
    ganjoor_link = models.URLField(
        max_length=200,
        verbose_name=_("پیوند گنچور"),
        help_text=_("پیوتد سروده در وبسایت گنجور"),
    )
    objects = RandomManager()

    class Meta:
        verbose_name = _("بیت سروده")
        verbose_name_plural = _("ابیات")

    def __str__(self):
        first_verse = self.lyric.split("\t")[0]
        return first_verse
