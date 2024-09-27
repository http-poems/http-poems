from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PoetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.poets"
    verbose_name = _("سرایندگان")
