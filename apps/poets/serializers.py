from rest_framework import serializers
from rest_framework.reverse import reverse

from apps.poets.models import Poet


class PoetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = "__all__"


class PoetClientSerializer(serializers.ModelSerializer):
    poet_client_link = serializers.SerializerMethodField()

    def get_poet_client_link(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(
            reverse("poet-retrieve-client-view", kwargs={"id": obj.id})
        )

    class Meta:
        model = Poet
        fields = ("poet_client_link", "surname")
