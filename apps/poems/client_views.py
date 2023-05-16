from rest_framework import generics
from rest_framework import status as http_status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from apps.poems.models import Poem
from apps.poems.serializers import PoemClientSerializer


class StatusCodeBasedPoemListClientView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "poems/status_code_based_poem_list_template.html"

    serializer_class = PoemClientSerializer
    lookup_url_kwarg = "code"

    def get_queryset(self):
        status_code = self.kwargs.get(self.lookup_url_kwarg)
        return Poem.objects.filter(status_code=status_code)

    def list(self, request, *args, **kwargs):
        poems = self.get_queryset()
        serializer = self.get_serializer(poems, many=True)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )


class RandomPoemRetrieveClientView(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "poems/random_poem_retrieve_template.html"

    serializer_class = PoemClientSerializer
    lookup_url_kwarg = "code"

    def get_queryset(self):
        status_code = self.kwargs.get(self.lookup_url_kwarg)
        return Poem.objects.filter(status_code=status_code)

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().random()[0]
        serializer = self.get_serializer(instance)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )


class PoemListClientView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "poems/poem-list-template.html"

    queryset = Poem.objects.all()
    serializer_class = PoemClientSerializer

    def list(self, request, *args, **kwargs):
        poems = self.get_queryset()
        serializer = self.get_serializer(poems, many=True)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )


class PoemRetrieveClientView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "poems/poem-retrieve-template.html"

    queryset = Poem.objects.all()
    serializer_class = PoemClientSerializer
    lookup_field = "uid"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )
