from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "mobile",
        "ward",
        "category",
        "status",
        "created_at",
    )

    list_filter = (
        "category",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "mobile",
        "ward",
    )

    list_per_page = 10

    ordering = ("-created_at",)