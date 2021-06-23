from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class CategoryAdd(TemplateView):
    template_name = "categoryadd.html"


class CategoryView(TemplateView):
    template_name = "categoryread.html"
