from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from product.form import ProductForm
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url="/")
def create_product(request):
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():

            fm.save()
            print(fm.cleaned_data)
            return HttpResponseRedirect("/product/productread")
        else:
            print("the form is not valid")
    fm = ProductForm()
    return render(request, "productadd.html", {"forms": fm})


@login_required(login_url="/")
def show_product(request):
    data = Product.objects.all()
    return render(request, "productread.html", {"datas": data})


@login_required(login_url="/")
def delete_product(request, id):
    if request.method == "POST":
        data = Product.objects.get(pk=id)
        print(data)
        print("hello")
        data.delete()
        return HttpResponseRedirect("/product/productread")


@login_required(login_url="/")
def update_product(request, id):
    if request.method == "POST":
        data = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, instance=data)
        if fm.is_valid():
            print("hello")
            name = fm.cleaned_data["name"]
            fm.save(name=name)
    data = Product.objects.get(pk=id)
    fm = ProductForm(instance=data)

    return render(request, "updateproduct.html", {"forms": fm})
