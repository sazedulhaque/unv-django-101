"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog import views
from core import views as auth_views

router = DefaultRouter()
router.register(r"blogs", views.BlogViewSet, basename="blog")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "",
        include("blog.urls"),
    ),
    path("api/", include(router.urls)),
    path("api/register/", auth_views.register_user, name="register"),
    path("api/login/", auth_views.login_user, name="login"),
    path("api/logout/", auth_views.logout_user, name="logout"),
]
