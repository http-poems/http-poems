from django.contrib import admin

from poems.models import StatusCode, Poet, Poem

admin.site.register(StatusCode)
admin.site.register(Poet)
admin.site.register(Poem)
