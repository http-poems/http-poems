from rest_framework import generics

from apps.poets.serializers import PoetSerializer
from apps.poets.models import Poet


class PoetListAPIView(generics.ListAPIView):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer


class PoetRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
    lookup_field = "id"
