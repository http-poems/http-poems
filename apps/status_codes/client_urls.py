from django.urls import path

from apps.status_codes.client_views import (
    StatusCodeListClientView,
    StatusCodeRetrieveClientView,
)

urlpatterns = [
    path(
        "",
        StatusCodeListClientView.as_view(),
        name="status-code-list-template",
    ),
    path(
        "<int:code>",
        StatusCodeRetrieveClientView.as_view(),
        name="status-code-retrieve-template",
    ),
]
