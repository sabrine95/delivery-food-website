from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model

from django.contrib.auth.forms import UserCreationForm

from home.models import Customer


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'password1', 'password2')


class Info(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('name', 'email')


class LoginForm(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

















# class RegisterForm(UserCreationForm):

#     prenom_client = forms.CharField(max_length=100)
#     nom_client = forms.CharField(max_length=100)
#     telephone_client = forms.CharField(max_length=8)
#     rue_client = forms.CharField(max_length=100)
#     ville_client = forms.CharField(max_length=100)

#     class Meta:
#         model = User
#         fields = [
#             'username', 'password1', 'password2', 'email',
#             'prenom_client', 'nom_client', 'telephone_client', 'rue_client', 'ville_client',
        # ]


# class Registrationform(forms.ModelForm):
#     mdp_client=forms.CharField(max_length=100,widget=forms.PasswordInput)

# class RegisterForm(Registrationform):
#     class Meta:
#         model = Client
#         fields=[
#             'prenom_client', 'nom_client', 'telephone_client', 'email_client', 'mdp_client', 'rue_client', 'ville_client'
#         ]

# class LoginForm(Registrationform):
#     class Meta:
#         model =Client
#         fields=['email_client','mdp_client']
