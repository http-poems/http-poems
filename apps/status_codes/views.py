from rest_framework import generics

from apps.status_codes.models import StatusCode
from apps.status_codes.serializers import StatusCodeSerializer


class StatusCodeListAPIView(generics.ListAPIView):
    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer


class StatusCodeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer
    lookup_field = "code"
