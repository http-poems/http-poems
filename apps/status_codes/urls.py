from django.urls import path

from apps.status_codes.views.api import (
    StatusCodeListAPIView,
    StatusCodeRetrieveAPIView,
)

urlpatterns = [
    path("", StatusCodeListAPIView.as_view(), name="status-code-list"),
    path(
        "<int:code>",
        StatusCodeRetrieveAPIView.as_view(),
        name="status-code-retrieve",
    ),
]
