# serializers.py

from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'image', 'nickname', 'info']


class ChatSerializer(serializers.ModelSerializer):
    chat_admin = ProfileSerializer(read_only=True)
    chat_members = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'chat', 'chat_name', 'chat_admin', 'chat_members', 'is_private']


class MessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(read_only=True)
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'author', 'body', 'created']
