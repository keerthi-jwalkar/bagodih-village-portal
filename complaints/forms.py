from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            "name",
            "mobile",
            "ward",
            "category",
            "location",
            "description",
            "image",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }),

            "mobile": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter mobile number"
            }),

            "ward": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter ward number"
            }),

            "category": forms.Select(attrs={
                "class": "form-control"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter complaint location"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe your complaint..."
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }