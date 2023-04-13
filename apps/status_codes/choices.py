from django.db import models

from django.utils.translation import gettext_lazy as _


class StatusCodeGroupChoices(models.IntegerChoices):
    INFORMATIONAL = 1, _("Informational")
    SUCCESSFUL = 2, _("Successful")
    REDIRECTION = 3, _("Redirection")
    CLIENT_ERROR = 4, _("Client Error")
    SERVER_ERROR = 5, _("Server Error")
