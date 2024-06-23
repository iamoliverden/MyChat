# views.py

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import logout

from django.db.models import Q

from .models import *
from .serializers import ProfileSerializer, ChatSerializer, MessageSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Profile

from django.shortcuts import render, redirect
from .forms import ProfileForm


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




@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('select_chat')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


from django.db.models import Q

from django.db.models import Q
from django.shortcuts import render
from .models import Profile, Chat
from django.contrib.auth.decorators import login_required


@login_required
def user_list(request):
    all_users = Profile.objects.exclude(id=request.user.id).all()

    # Filter chats where either the logged-in user is a member or admin,
    # and where any of the other users in all_users are members or admins.
    common_chats = Chat.objects.filter(
        (Q(chat_members=request.user) | Q(chat_admins=request.user)) &
        (Q(chat_members__in=all_users) | Q(chat_admins__in=all_users))
    ).distinct()

    context = {
        'users': all_users,
        'common_chats': common_chats
    }

    return render(request, 'user_list.html', context)
