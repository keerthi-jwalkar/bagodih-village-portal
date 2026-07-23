from django.db import models


class Complaint(models.Model):

    CATEGORY_CHOICES = [
        ("Road", "Road Issue"),
        ("Water", "Water Supply"),
        ("Electricity", "Electricity"),
        ("Cleanliness", "Cleanliness"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]

    name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    ward = models.CharField(max_length=50)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="complaints/",
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=200,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name} - {self.category}"