from django.db import models

from accounts.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, related_name= "sent", on_delete = models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received", on_delete = models.CASCADE)
    text = models.CharField(max_length=  256)
    img = models.ImageField(blank = True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message between {self.sender} and {self.receiver}"

class Chat(models.Model):
    user1 = models.ForeignKey(User, related_name="user1", on_delete= models.CASCADE)
    user2 = models.ForeignKey(User, related_name= "user2", on_delete= models.CASCADE)

    def __str__(self):
        return f"Chat between {self.user1} and {self.user2}"

