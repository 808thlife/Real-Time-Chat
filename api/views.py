from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from core.models import Message
import accounts

@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serializer = serializers.MessageSerializer(messages, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_users(request):
    pass