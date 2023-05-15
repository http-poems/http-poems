from django.urls import path

from apps.poems.client_views import (
    PoemListClientView,
    PoemRetrieveClientView,
)

urlpatterns = [
    path("", PoemListClientView.as_view(), name=""),
    path("<str:uid>", PoemRetrieveClientView.as_view(), name=""),
]
