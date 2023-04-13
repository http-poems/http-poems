from django.contrib import admin
from django.utils.html import format_html

from apps.poems.models import Poem
from apps.poets.models import Poet
from apps.status_codes.models import StatusCode

admin.site.register(Poem)


@admin.register(StatusCode)
class StatusCodeModelAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "status_code_mdn_link")

    def status_code_mdn_link(self, obj):
        if obj.mdn_link:
            return format_html(
                "<a href='{url}' target='_blank'>{url}</a>", url=obj.mdn_link
            )


@admin.register(Poet)
class PoetModelAdmin(admin.ModelAdmin):
    list_display = ("fa_surname", "en_surname", "poet_profile_ganjoor_link")

    def poet_profile_ganjoor_link(self, obj):
        if obj.ganjoor_link:
            return format_html(
                "<a href='{url}' target='_blank'>{url}</a>", url=obj.ganjoor_link
            )
