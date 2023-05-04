from django.contrib import admin
from django.utils.html import format_html

from apps.poems.models import Poem


@admin.register(Poem)
class PoemModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "poet", "status_code", "poem_ganjoor_link")

    def poem_ganjoor_link(self, obj):
        if obj.ganjoor_link:
            return format_html(
                "<a href='{url}' target='_blank'>{url}</a>",
                url=obj.ganjoor_link,
            )
