from rest_framework import serializers

from apps.poems.models import Poem
from apps.poets.serializers import PoetClientSerializer
from apps.status_codes.serializers import StatusCodeClientSerializer


class PoemSerializer(serializers.ModelSerializer):
    poet = serializers.CharField(source="poet.surname")

    class Meta:
        model = Poem
        exclude = ("id",)


class PoemClientSerializer(serializers.ModelSerializer):
    poet = PoetClientSerializer()
    status_code = StatusCodeClientSerializer()

    class Meta:
        model = Poem
        exclude = ("id",)
