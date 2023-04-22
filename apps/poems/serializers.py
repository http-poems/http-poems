from apps.poems.models import Poem
from rest_framework import serializers


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        exclude = ("id",)
