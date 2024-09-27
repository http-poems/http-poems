from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StatusCodesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.status_codes"
    verbose_name = _("کد‌های وضعیت")
