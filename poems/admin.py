from django.contrib import admin
from django.utils.html import format_html

from poems.models import StatusCode, Poet, Poem

admin.site.register(Poet)
admin.site.register(Poem)


@admin.register(StatusCode)
class StatusCodeModelAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "show_mdn_link")

    def show_mdn_link(self, obj):
        if obj.mdn_link:
            return format_html(
                "<a href='{url}' target='_blank'>{url}</a>", url=obj.mdn_link
            )
