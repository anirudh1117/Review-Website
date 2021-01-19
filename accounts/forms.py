from django import forms
from .models import UserProfile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from . import check_username_or_email
import re


class RegistrationForm(forms.ModelForm):

    c_password = forms.CharField(max_length=20, min_length=8,
    widget=forms.PasswordInput(
        attrs={'class': 'form-control',
                'id': 'rpwd',
                'placeholder': 'Confirm Password',
                'required': True
                }))
    name = forms.CharField(max_length=50, min_length=3,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'id': 'name',
                'required': True
            }))
    username = forms.CharField(max_length=20, min_length=4,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'placeholder': 'UserName',
                'id': 'uname',
                'required': True
            }))
    email = forms.EmailField(min_length=5,
    widget=forms.EmailInput(
        attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
                'id': 'email',
                'required': True
            }))
    password = forms.CharField(max_length=20, min_length=8,
    widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'id': 'pwd',
                'placeholder': 'Enter Password',
                'required': True
            }))

    class Meta:
        model = UserProfile
        fields = [
            'phoneNo'
        ]
        widgets = {
            'phoneNo': forms.NumberInput(attrs={
                'class': 'form-control form-control3',
                'id': 'phoneno',
                'placeholder': 'Phone Number.'
            }),
        }

    def clean_password(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        c_password = cleaned_data.get("c_password")
        if password != c_password:
            raise forms.ValidationError(
            "Password Does not match."
        )

    def clean_username(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
            "Username Already Taken!!."
        )

    def clean_email(self):
        cleaned_data = super(RegistrationForm, self).clean()
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
            "Email Already Registered!!."
            )


class LoginForm(forms.Form):
    email = forms.CharField(
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'placeholder': 'E-mail or Username',
                'id': 'email_or_username',
                'required': True
            }))
    password = forms.CharField(max_length=20, min_length=8,
    widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'id': 'pwd',
                'placeholder': 'Enter Password',
                'required': True
            }))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email_or_username = cleaned_data.get("email")
        password = cleaned_data.get("password")
        email_or_username = check_username_or_email.check_username_or_email(email_or_username)
        if not email_or_username:
            raise forms.ValidationError(
                    "Email or Username is not registered!!"
            )
        else:
            user = auth.authenticate(
                    username=email_or_username, password=password)
            if user is None:
                raise forms.ValidationError(
                 "Username or password does not matched!!"
                )
