from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("", views.get_messages, name = "index"),
    path("send/", views.send_message, name ="send")
]
