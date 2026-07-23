from django.shortcuts import render, redirect
from .models import Complaint

def submit_complaint(request):

    if request.method == "POST":
        print("POST RECEIVED")

        complaint = Complaint.objects.create(
            name=request.POST.get("name"),
            mobile=request.POST.get("mobile"),
            ward=request.POST.get("ward"),
            category=request.POST.get("category"),
            description=request.POST.get("description"),
            location=request.POST.get("location"),
            image=request.FILES.get("image"),
        )

        print("Complaint Saved:", complaint.id)

        return render(
    request,
    "complaints/complaint_successfully.html",
    {"complaint": complaint}
)

    return render(request, "complaints/submit_complaint.html")