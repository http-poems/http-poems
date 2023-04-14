from rest_framework import generics

from apps.poets.serializers import PoetSerializer
from apps.poets.models import Poet


class StatusCodeListAPIView(generics.ListAPIView):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
