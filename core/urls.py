from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name ="index"),
    path("create/", views.create_room, name = "create_room"),
    path("room/<str:hash>/", views.room, name = "room"),
    path("join/", views.join_room, name = "join"),
    path("leave/<str:hash>", views.leave_room, name = "leave")
]
