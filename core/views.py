from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import User
from .models import Room,Message

@login_required
def index(request):
    currentUser = request.user
    rooms = currentUser.rooms.all()
    context = {"rooms":rooms}
    return render(request, "core/index.html", context)

@login_required
def create_room(request):
    if request.method == "POST":
        title = request.POST["title"]
        room = Room(title = title)
        room.save()
        room.users.add(request.user)
        return HttpResponseRedirect(reverse("core:room", kwargs = {"hash" : room.hash}))
    return render(request, "core/create-room.html")

@login_required
def room(request, hash):
    room = Room.objects.get(hash = hash)
    room_messages = room.messages.all()
    context = {"room":room, "messages":room_messages}
    return render(request, "core/room.html", context)

@login_required
def join_room(request):
    hash = request.GET["room-hash"]
    room = Room.objects.get(hash = hash)

    if not request.user in room.users.all():
        room.users.add(request.user)
        room.save()
        return HttpResponseRedirect(reverse("core:room", kwargs = {"hash":room.hash}))
    
    return HttpResponseRedirect(reverse("core:room", kwargs = {"hash":room.hash}))

@login_required
def leave_room(request, hash):
    room = Room.objects.get(hash = hash)
    room.users.remove(request.user)
    return HttpResponseRedirect(reverse("core:index"))