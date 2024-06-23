# urls (mychat)

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('select_chat/', select_chat, name='select_chat'),
    path('chat/<int:chat_id>/', chat_details, name='chat_details'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('user_list/', user_list, name='user_list'),

]