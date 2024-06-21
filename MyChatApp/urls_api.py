# urls_api.py (api)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]
