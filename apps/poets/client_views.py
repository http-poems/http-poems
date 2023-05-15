from rest_framework import generics
from rest_framework import status as http_status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from apps.poets.models import Poet
from apps.poets.serializers import PoetSerializer


class PoetListClientView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "poets/poet-list-template.html"

    queryset = Poet.objects.all()
    serializer_class = PoetSerializer

    def list(self, request, *args, **kwargs):
        poets = self.get_queryset()
        serializer = self.get_serializer(poets, many=True)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )


class PoetRetrieveClientView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "poets/poet-retrieve-template.html"

    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )
