from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PoemsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "poems"
    verbose_name = _("سروده ها")
