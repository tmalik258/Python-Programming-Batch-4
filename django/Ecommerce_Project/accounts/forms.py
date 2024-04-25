from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        # exclude = ['is_active', 'is_staff', 'is_superuser']
        labels = {
            'username': 'User-Name',
            # 'email': ''
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Username',
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control jks',
            'placeholder': 'Enter your First Name'
        })
        self.fields['first_name'].label = 'heyyy'
        self.fields['first_name'].help_text = 'helo'

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your Last Name'
        })


        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your Password'
        })
