from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/room/<str:hash>', consumers.ChatConsumer.as_asgi())
]