from django.urls import path, re_path
from .consumers import *

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', ChatConsumer.as_asgi())
]


