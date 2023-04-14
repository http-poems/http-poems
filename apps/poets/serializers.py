from rest_framework import serializers

from apps.poets.models import Poet


class PoetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poet
        fields = "__all__"
