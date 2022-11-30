from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "auth_app/login.html")

def signup(request):
    return render(request, "auth_app/signup.html")

def forgotPassword(request):
    return render(request, "auth_app/forgot_password.html")

def resetPassword(request):
    return render(request, "auth_app/reset_password.html")
