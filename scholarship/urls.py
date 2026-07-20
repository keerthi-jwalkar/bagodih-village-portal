from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "scholarships/",
        views.scholarship_list,
        name="scholarship_list",
    ),

    path(
        "scholarships/apply/<int:scholarship_id>/",
        views.scholarship_apply,
        name="scholarship_apply",
    ),
]