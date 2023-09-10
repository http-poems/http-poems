from django.db.models import F
from rest_framework import generics
from rest_framework import status as http_status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from apps.poems.models import Poem
from apps.poems.serializers import PoemSerializer
from apps.status_codes.models import StatusCode
from apps.status_codes.serializers import StatusCodeSerializer
from apps.utils.functions import get_repo_contributors


class HomePageView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "utils/index.html"

    queryset = (
        Poem.objects.annotate(
            poet_name=F("poet__surname"),
            status_code_title=F("status_code__title"),
        )
        .values("lyric", "poet_name", "status_code_title", "status_code")
        .distinct("status_code")
        .order_by("status_code__code")
    )

    def list(self, request, *args, **kwargs):
        status_code_cards = self.get_queryset()
        repo_contributors = get_repo_contributors()
        return Response(
            data={
                "cards": status_code_cards,
                "contributors": repo_contributors,
            },
            status=http_status.HTTP_200_OK,
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
        poems_queryset = Poem.objects.filter(status_code=instance.code)
        poems = PoemSerializer(poems_queryset, many=True).data
        return Response(
            data={"status_code": serializer.data, "poems": poems},
            status=http_status.HTTP_200_OK,
        )
