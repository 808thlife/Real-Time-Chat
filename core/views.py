from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import User
from .models import Room,Message

@login_required
def index(request):
    context = {}
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
    context = {}
    return render(request, "core/room.html")