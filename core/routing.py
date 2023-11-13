from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/<str:room_hash>/', consumers.ChatConsumer.as_asgi())
]