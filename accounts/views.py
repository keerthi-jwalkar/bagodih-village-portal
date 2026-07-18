from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


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

            return redirect("/")

        else:

            messages.error(request, "Invalid Username or Password")

            return redirect("login")

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
            return redirect("register")
        # Password Length
        if len(password) < 6:
         messages.error(request, "Password must be at least 6 characters.")
         return redirect("register")
        #uppercase
        if not any(char.isupper() for char in password):
         messages.error(request, "Password must contain at least one uppercase letter.")
         return redirect("register")
        #lowercase
        if not any(char.islower() for char in password):
         messages.error(request, "Password must contain at least one lowercase letter.")
         return redirect("register")
        #number
        if not any(char.isdigit() for char in password):
         messages.error(request, "Password must contain at least one number.")
         return redirect("register")
        
        # Username Exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # Email Exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

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
        return redirect("login")

    return render(request, "accounts/register.html")



def logout_page(request):

    logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("login")
