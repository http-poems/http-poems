from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from apps.status_codes.models import StatusCode
from apps.status_codes.serializers import StatusCodeSerializer
from rest_framework import status as http_status


class StatusCodeListClientView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_codes/status-code-list-template.html"

    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer

    def list(self, request, *args, **kwargs):
        poets = self.get_queryset()
        serializer = self.get_serializer(poets, many=True)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )


class StatusCodeRetrieveClientView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_codes/status-code-retrieve-template.html"

    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer
    lookup_field = "code"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            data={"data": serializer.data}, status=http_status.HTTP_200_OK
        )
