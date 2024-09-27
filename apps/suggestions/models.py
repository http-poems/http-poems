from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.poets.models import Poet
from apps.status_codes.models import StatusCode
from apps.suggestions.choices import SuggestionStates


class Suggestion(models.Model):
    lyric = models.TextField(
        max_length=256, null=False, blank=False, verbose_name=_("سروده")
    )
    poet = models.ForeignKey(
        Poet,
        on_delete=models.CASCADE,
        verbose_name=_("سراینده"),
        help_text=_("سراینده این سروده پیشنهادی"),
    )
    status_code = models.ForeignKey(
        StatusCode,
        to_field="code",
        on_delete=models.CASCADE,
        verbose_name=_("کد وضعیت"),
        help_text=_("کد وضعیتی که این سروده پیشنهادی قرار است آن را توصیف می‌کند"),
    )
    state = models.SmallIntegerField(
        choices=SuggestionStates.choices,
        default=SuggestionStates.SUBMITTED,
        help_text=_("وضعیت فعلی این سروده پیشنهادی را توصیف می‌کند"),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("بیت سروده پیشنهادی")
        verbose_name_plural = _("ابیات پیشنهادی")

    def __str__(self):
        first_verse = self.lyric.split("\t")[0]
        return first_verse
