from poems.models import StatusCode, Poet, Poem
from rest_framework import viewsets
from poems.serializers import StatusCodeSerializer, PoetSerializer, PoemSerializer


class StatusCodeViewSet(viewsets.ModelViewSet):
    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer


class PoetViewSet(viewsets.ModelViewSet):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer


class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
