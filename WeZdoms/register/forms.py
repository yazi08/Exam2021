from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Mudrosty


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'password1', 'password2']

    # your_name = forms.CharField(label='Your name', max_length=100)



class AddMudrostyForm(forms.ModelForm):

    class Meta:

        model = Mudrosty
        fields = '__all__'
