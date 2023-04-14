from apps.poems.models import Poem
from rest_framework import serializers


class PoemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poem
        fields = "__all__"


