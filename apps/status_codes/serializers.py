from rest_framework import serializers
from rest_framework.reverse import reverse

from apps.status_codes.models import StatusCode


class StatusCodeSerializer(serializers.ModelSerializer):
    group = serializers.CharField(source="group_label")

    class Meta:
        model = StatusCode
        fields = "__all__"


class StatusCodeClientSerializer(serializers.ModelSerializer):
    status_code_client_link = serializers.SerializerMethodField()

    def get_status_code_client_link(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(
            reverse("status-code-retrieve-template", kwargs={"code": obj.code})
        )

    class Meta:
        model = StatusCode
        fields = ("code", "status_code_client_link")
