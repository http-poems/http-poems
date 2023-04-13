from apps.poems.models import Poem
from apps.poets.models import Poet
from apps.status_codes.models import StatusCode
from rest_framework import serializers


class StatusCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusCode
        fields = "__all__"


class PoemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poem
        fields = "__all__"


class PoetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poet
        fields = "__all__"
