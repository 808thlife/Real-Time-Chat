from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from core.models import Message
import accounts


#APIs FOR MESSAGES

@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serializer = serializers.MessageSerializer(messages, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_messages_chat(request, id):
    pass

@api_view(['POST'])
def send_message(request):
    serializer = serializers.MessageSerializer(data = request.data) 
    if serializer.is_valid():
        print(serializer.errors)
        serializer.save()
        return Response("Successfully saved!")
    print(serializer.errors)
    return Response("Something went wrong")