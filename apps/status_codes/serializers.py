from rest_framework import serializers

from apps.status_codes.models import StatusCode


class StatusCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusCode
        fields = "__all__"
