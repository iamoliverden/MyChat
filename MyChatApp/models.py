# models.py

from django.db import models
import shortuuid
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    image = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)


class Chat(models.Model):
    chat = models.CharField(max_length=128, unique=True, default=shortuuid.uuid)
    chat_name = models.CharField(max_length=128, null=True, blank=True)
    chat_admin = models.ForeignKey(Profile, related_name='chat_admin', blank=True, null=True, on_delete=models.CASCADE)
    chat_members = models.ManyToManyField(Profile, related_name='chat_members', blank=True)
    is_private = models.BooleanField(default=False)


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_messages', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
