from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login", views.loginView, name ="loginView"),
    path("register", views.registerView, name ="registerView"),
    path("loginform", views.loginForm, name = "login"),
    path("registerform", views.registerForm, name ="register")

]
