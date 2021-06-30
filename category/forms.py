from django import forms
from .models import Category


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "vendor"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:24ch",
                    "placeholder": "Enter the category name",
                }
            ),
            "vendor": forms.TextInput(
                attrs={"class": "form-control", "style": "width:24ch"}
            ),
        }
