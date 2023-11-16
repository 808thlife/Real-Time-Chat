import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room

class ChatConsumer(WebsocketConsumer):
    async def connect(self):
        room_hash = self.scope["url_route"]["kwargs"]["room_hash"]
        room = Room.objects.get(hash = room_hash)
        self.room_name = room.title
        self.room_group_name = 'chat_%s' % self.room_name

        await self.send(text_data = json.dumps({
            'type':'room_hash',
            'hash': room_hash
        }))

        chat_room = Room.objects.get(hash = hash)
        print(chat_room)
        await self.accept({
            'type': 'websocket.accept'
        })

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

