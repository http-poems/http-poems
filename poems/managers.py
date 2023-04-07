from django.db import models

from poems.querysets import RandomQuerySet


class RandomManager(models.Manager):
    def random(self, *args, **kwargs):
        return self.get_queryset().random(*args, **kwargs)

    def get_queryset(self):
        return RandomQuerySet(self.model)
