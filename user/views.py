from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class UserAdd(TemplateView):
    template_name = "useradd.html"


class UserView(TemplateView):
    template_name = "userread.html"
