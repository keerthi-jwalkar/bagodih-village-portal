from django.contrib import admin
from .models import Complaint, ComplaintImage


class ComplaintImageInline(admin.TabularInline):
    model = ComplaintImage
    extra = 1


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

    inlines = [ComplaintImageInline]


@admin.register(ComplaintImage)
class ComplaintImageAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "complaint",
        "image",
    )