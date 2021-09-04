from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class EditProfileForm(ModelForm):

    class Meta:


        model = User
        fields = (
        		  
                 'email',
                 'first_name',
                 'last_name'
                )


