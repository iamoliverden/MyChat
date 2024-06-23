# serializers.py

from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'image', 'nickname', 'personal_information']


class ChatSerializer(serializers.ModelSerializer):
    chat_admins = serializers.SlugRelatedField(slug_field='nickname', many=True, queryset=Profile.objects.all())
    chat_members = serializers.SlugRelatedField(slug_field='nickname', many=True, queryset=Profile.objects.all())

    class Meta:
        model = Chat
        fields = ['id', 'chat_name', 'chat_admins', 'chat_members', 'one_on_one']

    def validate(self, data):
        if data.get('one_on_one'):
            if len(data.get('chat_admins')) > 1 or len(data.get('chat_members')) > 2:
                raise serializers.ValidationError("In a one-on-one chat, there can only be one admin and one member.")
        return data

    def create(self, validated_data):
        chat_admins = validated_data.pop('chat_admins')
        chat_members = validated_data.pop('chat_members')
        chat = Chat.objects.create(**validated_data)
        chat.chat_admins.set(chat_admins)
        chat.chat_members.set(chat_members)
        return chat

    def update(self, instance, validated_data):
        chat_admins = validated_data.pop('chat_admins')
        chat_members = validated_data.pop('chat_members')
        instance = super().update(instance, validated_data)
        instance.chat_admins.set(chat_admins)
        instance.chat_members.set(chat_members)
        return instance


class MessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(read_only=True)
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'author', 'body', 'created']
