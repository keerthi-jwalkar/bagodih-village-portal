from django.shortcuts import render, redirect
from .models import Complaint, ComplaintImage


def submit_complaint(request):

    if request.method == "POST":

        complaint = Complaint.objects.create(

            name=request.POST.get("name"),
            mobile=request.POST.get("mobile"),
            ward=request.POST.get("ward"),
            category=request.POST.get("category"),
            description=request.POST.get("description"),
            location=request.POST.get("location"),
        )

        # Multiple Images Save
        images = request.FILES.getlist("images")

        for image in images:
            ComplaintImage.objects.create(
                complaint=complaint,
                image=image,
            )

        return render(
            request,
            "complaints/complaint_successfully.html",
            {
                "complaint": complaint
            }
        )

    return render(
        request,
        "complaints/submit_complaint.html"
    )