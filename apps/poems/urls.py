from apps.poems.views import (
    PoemListAPIView,
    PoemRetrieveAPIView,
    StatusCodeBasedPoemListAPIView,
)

from django.urls import path

urlpatterns = [
    path("", PoemListAPIView.as_view(), name=""),
    path("<str:uid>", PoemRetrieveAPIView.as_view(), name=""),
]
