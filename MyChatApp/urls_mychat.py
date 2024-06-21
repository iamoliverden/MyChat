from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('join_chat/<int:chat_id>/', views.join_chat, name='join_chat_view'),

]
