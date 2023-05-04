from django.contrib import admin
from django.utils.html import format_html

from apps.poets.models import Poet


@admin.register(Poet)
class PoetModelAdmin(admin.ModelAdmin):
    list_display = ("surname", "id", "poet_profile_ganjoor_link")

    def poet_profile_ganjoor_link(self, obj):
        if obj.ganjoor_link:
            return format_html(
                "<a href='{url}' target='_blank'>{url}</a>",
                url=obj.ganjoor_link,
            )
