from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["productName", "productQuantity", "stock", "price", "image"]

        widgets = {
            "productName": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:24ch",
                    "placeholder": "Enter the product name",
                }
            ),
            "productQuantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "width:12ch",
                    "placeholder": "Enter the Product Quantity ",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "width:12ch",
                    "placeholder": "Enter the Stock",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "width:12ch",
                    "placeholder": "Enter the product Price",
                }
            ),
        }
