import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        room_hash = self.scope["url_route"]["kwargs"]["room_hash"]
        #self.room_group_name = self.scope["url"]["kwargs"]["hash"]

        self.send(text_data = json.dumps({
            'type':'room_hash',
             'hash': room_hash
        }))

        chat_room = Room.objects.get(hash = hash)
        print(chat_room)
        self.accept({
            'type': 'websocket.accept'
        })

    def disconnect(self):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print("Message is "+message)