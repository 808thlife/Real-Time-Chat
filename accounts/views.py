from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import User
# Create your views here.

def loginView(request):
    return render(request, "accounts/login.html")

def registerView(request):
    return render(request, "accounts/register.html")

def loginForm(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print("sdfsdf")
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("core:index"))
        messages.error(request, "Invalid login")
        return render(request, "accounts/login.html")

def registerForm(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirmpassword"]

        if password != confirm_password:
            messages.error(request, "Passwords don't match!")
            return render(request, "accounts/register.html")
        
        user = authenticate(username = username, password = password)
        if user is not None:
            messages.error(request, "User already exists!")
            return render(request, "accounts/register.html")
        else:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse("core:index"))
        
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:loginView"))