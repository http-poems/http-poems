from django.urls import path

from apps.poets.client_views import (
    PoetListClientView,
    PoetRetrieveClientView,
)

urlpatterns = [
    path("", PoetListClientView.as_view(), name="poet-list-template"),
    path(
        "<str:id>",
        PoetRetrieveClientView.as_view(),
        name="poet-retrieve-client-view",
    ),
]
