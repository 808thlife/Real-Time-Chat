from django.db import models

from accounts.models import User

from .utils import get_random_string

import hashlib


# Create your models here.

class Link(models.Model):
    linkTo = models.URLField(max_length=200)

class Room(models.Model):
    hash = models.CharField(max_length = 64, unique = True, default = None, null = True, blank = True)
    title = models.CharField(max_length = 256)
    users = models.ManyToManyField(User, related_name = "rooms")
    link = models.ForeignKey(Link, related_name = "link", on_delete = models.PROTECT, null = True, blank = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.hash is None:
            raw_hash = get_random_string()
            encoded_raw_hash = raw_hash.encode()
            self.hash = hashlib.sha256(encoded_raw_hash).hexdigest()
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Message(models.Model):
    room = models.ForeignKey(Room, related_name = "room" ,on_delete = models.CASCADE)
    sender = models.ForeignKey(User, related_name= "sent", on_delete = models.CASCADE)
    text = models.CharField(max_length=  256)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message in {self.room}"
