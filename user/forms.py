from django import forms
from django.forms import fields
from .models import User


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "address", "email", "password"]
        error_messages = {
            "name": {"required": "please enter name"},
            "address": {"required": "please enter address"},
            "email": {"required": "please enter email"},
            "password": {"required": "please enter password"},
        }
        widgets = {
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Password",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Name",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter address",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter email",
                }
            ),
        }

    def clean_name(self):
        valname = self.cleaned_data["name"]
        if len(valname) < 4:
            raise forms.ValidationError(
                "your name shouln't be less than 5", code="invalid"
            )
        return valname
