from django.core.exceptions import ValidationError
from django.db.models.fields import CharField
from .models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "address", "password", "image"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter name",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter Your address here",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Email",
                    "style": "width:36ch",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter Your Password",
                }
            ),
        }

   