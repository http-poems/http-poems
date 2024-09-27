from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.choices import MappedChoicesMetaClass


class SuggestionStates(models.IntegerChoices, metaclass=MappedChoicesMetaClass):
    SUBMITTED = 0, _("submitted")
    APPROVED = 1, _("approved")
    APPLIED = 2, _("applied")
    DISAPPROVED = -1, _("disapproved")
