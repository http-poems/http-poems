"""http_poems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the `include()` function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.poems.client_views import (
    RandomPoemRetrieveClientView,
    StatusCodeBasedPoemListClientView,
)
from apps.poems.views import (
    RandomPoemRetrieveAPIView,
    StatusCodeBasedPoemListAPIView,
)
from apps.status_codes.views.client import (
    HomePageView,
    StatusCodeRetrieveClientView,
)

urlpatterns = [
    path(
        "",
        HomePageView.as_view(),
        name="status-code-list-template",
    ),
    path(
        "<int:code>",
        StatusCodeRetrieveClientView.as_view(),
        name="status-code-retrieve-template",
    ),
    path("admin/", admin.site.urls),
    path("poems/", include("apps.poems.client_urls"), name="poems-client"),
    path("poets/", include("apps.poets.client_urls"), name="poets-client"),
    path(
        "<int:code>/random",
        RandomPoemRetrieveClientView.as_view(),
        name="random-poem-retrieve-client",
    ),
    path(
        "<int:code>/poems",
        StatusCodeBasedPoemListClientView.as_view(),
        name="status-code-poems-list-client",
    ),
    path(
        "api/",
        include(
            [
                path("poems/", include("apps.poems.urls"), name="poems"),
                path("poets/", include("apps.poets.urls"), name="poets"),
                path(
                    "status-codes/",
                    include("apps.status_codes.urls"),
                    name="status_codes",
                ),
                path(
                    "<int:code>",
                    RandomPoemRetrieveAPIView.as_view(),
                    name="random-poem-retrieve",
                ),
                path(
                    "<int:code>/poems",
                    StatusCodeBasedPoemListAPIView.as_view(),
                    name="status-code-poems-list",
                ),
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
