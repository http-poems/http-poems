from django.urls import path

from apps.poems.views import (
    PoemListAPIView,
    PoemRetrieveAPIView,
)

urlpatterns = [
    path("", PoemListAPIView.as_view(), name=""),
    path("<str:uid>", PoemRetrieveAPIView.as_view(), name=""),
]
