from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            messages.success(
                request,
                f"Welcome {user.username}!"
            )

            return redirect("/")


        else:

            messages.error(
                request,
                "❌ Invalid Username or Password"
            )


    return render(request, "accounts/login.html")


def register_page(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password Match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("accounts:register")
        # Password Length
        if len(password) < 6:
         messages.error(request, "Password must be at least 6 characters.")
         return redirect("accounts:register")
        #uppercase
        if not any(char.isupper() for char in password):
         messages.error(request, "Password must contain at least one uppercase letter.")
         return redirect("accounts:register")
        #lowercase
        if not any(char.islower() for char in password):
         messages.error(request, "Password must contain at least one lowercase letter.")
         return redirect("accounts:register")
        #number
        if not any(char.isdigit() for char in password):
         messages.error(request, "Password must contain at least one number.")
         return redirect("accounts:register")

        # Username Exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("accounts:register")

        # Email Exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("accounts:register")

        # Create User
        print("Creating user...")
        
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        print("User created successfully")

        messages.success(request, "Account created successfully. Please login.")
        return redirect("accounts:login")

    return render(request, "accounts/register.html")



def logout_page(request):

    logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("accounts:login")

def check_username(request):

    username = request.GET.get("username", "").strip()

    if not username:
        return JsonResponse({
            "available": False,
            "message": ""
        })

    exists = User.objects.filter(username=username).exists()

    if exists:

        return JsonResponse({
            "available": False,
            "message": " Username already taken"
        })

    return JsonResponse({
        "available": True,
        "message": " Username available"
    })
def check_email(request):

    email = request.GET.get("email", "").strip()

    if not email:
        return JsonResponse({
            "available": False,
            "message": ""
        })

    exists = User.objects.filter(email=email).exists()

    if exists:

        return JsonResponse({
            "available": False,
            "message": "❌ Email already registered"
        })

    return JsonResponse({
        "available": True,
        "message": "✅ Email available"
    })
    