# urls (mychat)

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('select_chat/', views.select_chat, name='select_chat'),
    path('chat/<int:chat_id>/', views.chat_details, name='chat_details'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),


]