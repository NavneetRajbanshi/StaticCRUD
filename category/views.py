from django.http.response import HttpResponseRedirect
from category.models import Category
from category.forms import CategoryForms
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def add_category(request):
    if request.method == "POST":
        fm = CategoryForms(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/category/categoryread")
        else:
            print("the form is not validated")
    fm = CategoryForms()
    return render(request, "categoryadd.html", {"forms": fm})


def show_category(request):
    data = Category.objects.all()
    return render(request, "categoryread.html", {"datas": data})


def delete_category(request, id):
    if request.method == "POST":
        data = Category.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect("/category/categoryread")


def update_category(request, id):
    if request.method == "POST":
        data = Category.objects.get(pk=id)
        fm = CategoryForms(request.POST, instance=data)
        if fm.is_valid():
            print("hello")
            fm.save()
            return HttpResponseRedirect("/category/categoryread")
    data = Category.objects.get(pk=id)
    fm = CategoryForms(instance=data)

    return render(request, "updatecategory.html", {"forms": fm})