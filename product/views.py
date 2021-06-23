from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ProductAdd(TemplateView):
    template_name = "productadd.html"


class ProductView(TemplateView):
    template_name = "productread.html"
