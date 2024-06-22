# views.py

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import logout

from django.db.models import Q

from .models import Profile, Chat, Message
from .serializers import ProfileSerializer, ChatSerializer, MessageSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile
from .forms import *



class ProfileViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet,
                     mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ChatViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(chat_admins=[self.request.user])


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
        chat = Chat.objects.create(chat_name=chat_name)
        chat.chat_admins.add(request.user)
        chat.chat_members.add(request.user)
        return redirect('chat')
    else:
        chats = Chat.objects.filter(Q(chat_members=request.user) | Q(chat_admins=request.user)).distinct()
        return render(request, 'chat.html', {'chats': chats})



def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def select_chat(request):
    chats = Chat.objects.filter(Q(chat_members=request.user) | Q(chat_admins=request.user)).distinct()
    return render(request, 'select_chat.html', {'chats': chats})


from django.http import JsonResponse

@login_required
def chat_details(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    chat_members = chat.chat_members.all()
    chat_admins = chat.chat_admins.all()
    members_data = list(chat_members.values('nickname'))  # Get values as a list of dictionaries
    admins_data = list(chat_admins.values('nickname'))  # Get values as a list of dictionaries
    chat_type = "Private Chat" if chat.one_on_one else "Group Chat"
    context = {
        'chat_name': chat.chat_name,
        'chat_members': members_data,
        'chat_admins': admins_data,
        'chat_type': chat_type,
        'username': request.user.username,
    }
    return render(request, 'chat.html', context)

