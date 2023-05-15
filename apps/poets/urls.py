from django.urls import path

from apps.poets.views import PoetListAPIView, PoetRetrieveAPIView

urlpatterns = [
    path("", PoetListAPIView.as_view(), name="poet-list"),
    path("<str:id>", PoetRetrieveAPIView.as_view(), name="poet-retrieve"),
]
