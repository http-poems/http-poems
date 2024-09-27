from django.contrib import admin
from django.utils.html import format_html

from apps.status_codes.models import StatusCode


@admin.register(StatusCode)
class StatusCodeModelAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "status_code_mdn_link")

    @staticmethod
    def status_code_mdn_link(obj):
        if obj.mdn_link:
            return format_html(
                "<a href='{url}' target='_blank'>{url}</a>", url=obj.mdn_link
            )
