from django.urls import path

from apps.status_codes.views import StatusCodeListAPIView, StatusCodeRetrieveAPIView

urlpatterns = [
    path("", StatusCodeListAPIView.as_view(), name=""),
    path("<code>", StatusCodeRetrieveAPIView.as_view(), name=""),
]
