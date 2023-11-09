from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import User
from .models import Chat,Message

@login_required
def index(request):
    users = User.objects.all()
    context = {"users":users}
    return render(request, "core/index.html", context)

