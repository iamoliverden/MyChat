# views.py

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


from .models import Profile, Chat, Message
from .serializers import ProfileSerializer, ChatSerializer, MessageSerializer



class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet,
                     mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ChatViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet,
                     mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@login_required
def chat(request):
    if request.method == 'POST':
        chat_name = request.POST.get('chat_name')
        chat = Chat.objects.create(chat_name=chat_name, chat_admin=request.user)
        chat.chat_members.add(request.user)
        return redirect('chat')
    else:
        chats = Chat.objects.all()
        return render(request, 'chat.html', {'chats': chats})

@login_required
def join_chat(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    chat.chat_members.add(request.user)
    return redirect('chat')
"""
@login_required
def chat(request):
    return render(request, 'chat.html')
"""

def logout_view(request):
    logout(request)
    return redirect('/')
