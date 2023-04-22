from rest_framework import generics
from rest_framework import status as http_status
from rest_framework.response import Response

from apps.poems.models import Poem
from apps.poems.serializers import PoemSerializer


class StatusCodeBasedPoemListAPIView(generics.ListAPIView):
    serializer_class = PoemSerializer
    lookup_url_kwarg = "code"

    def get_queryset(self):
        status_code = self.kwargs.get(self.lookup_url_kwarg)
        return Poem.objects.filter(status_code=status_code)


class RandomPoemRetrieveAPIView(generics.GenericAPIView):
    serializer_class = PoemSerializer
    lookup_url_kwarg = "code"

    def get_queryset(self):
        status_code = self.kwargs.get(self.lookup_url_kwarg)
        return Poem.objects.filter(status_code=status_code)

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().random()[0]
        serializer = self.get_serializer(instance)
        return Response(data=serializer.data, status=http_status.HTTP_200_OK)


class PoemListAPIView(generics.ListAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


class PoemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    lookup_field = "uid"
