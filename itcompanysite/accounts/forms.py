from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.forms import CharField
from django.forms import PasswordInput
from django import forms

User = get_user_model()
class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
