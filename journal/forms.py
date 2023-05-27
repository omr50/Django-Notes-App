from tkinter import Widget
from django.forms import ModelForm

from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from . models import Notes

# import authentication form

from django import forms

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class NotePostForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        exclude = ['user']


class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        exclude = ['user']


class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']
