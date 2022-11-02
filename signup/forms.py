from dataclasses import field
from tkinter.tix import Tree
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormSignUp(UserCreationForm):
    class Meta: 
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

