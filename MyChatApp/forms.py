# forms.py
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from django import forms


class ProfileForm(UserChangeForm):
    password = None
    username = forms.CharField(
        max_length=150,
        help_text="A-Z, a-z, 0-9, @/./+/-/_ (< 150 symbols)"
    )
    class Meta:
        model = Profile
        fields = ['username', 'nickname', 'first_name', 'last_name', 'email', 'image',  'personal_information']
