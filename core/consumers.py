import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from accounts.models import User
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print("connected")
        # room_hash = self.scope["url_route"]["kwargs"]["room_hash"]
        self.room_name = self.scope["url_route"]["kwargs"]["room_hash"]
        self.room_group_name = 'chat%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # chat_room = Room.objects.get(hash = hash)
        # print(chat_room)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        room_hash = text_data_json['room_hash']

        await self.save_message(username, room_hash, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":message,
                "username":username,
                "room_hash":room_hash        
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room_hash = event['room_hash']

        
        await self.send(text_data = json.dumps({
            "message":message,
            "username":username,
            "room_hash":room_hash   
        }))

    @sync_to_async
    def save_message(self,username, room_hash ,message):
        user = User.objects.get(username = username)
        room = Room.objects.get(hash = room_hash)

        f = Message(sender = user, room = room, text = message)
        f.save()