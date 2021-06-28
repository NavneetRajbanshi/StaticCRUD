from django.core.exceptions import ValidationError
from django.db.models.fields import CharField
from .models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["name", "email", "address", "password", "image"]
        labels = {
            "name": "Enter Name",
            "password": "Enter Password",
            "email": "Enter Email",
            "image": "Enter your image",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter name",
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
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter Your address here",
                }
            ),
        }

    def clean_email(self):
        print("hello this is clean_email")
        email_passed = self.cleaned_data.get("email")
        email_req = "a@a.com"
        if not email_req in email_passed:
            print("raise the error")
            raise forms.ValidationError("the length is too short")
        return email_passed
