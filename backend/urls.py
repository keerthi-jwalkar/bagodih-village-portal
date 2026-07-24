from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),

    path("accounts/", include("accounts.urls")),

    path("scholarship/", include(("scholarship.urls", "scholarship"), namespace="scholarship")),
    path("complaints/",include("complaints.urls")),

]