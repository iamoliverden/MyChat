# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    image = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    personal_information = models.TextField(null=True, blank=True)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "Anonymous User"


class Chat(models.Model):
    chat_name = models.CharField(max_length=128, null=True, blank=True)
    chat_admins = models.ManyToManyField(Profile, related_name='chat_admins', blank=True)
    chat_members = models.ManyToManyField(Profile, related_name='chat_members', blank=True)
    one_on_one = models.BooleanField(default=False)


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_messages', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
