from django.contrib.messages.constants import SUCCESS
from django.http.response import HttpResponse, HttpResponseRedirect
from user.forms import UserForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import User

# Create your views here.


@login_required(login_url="/")
def create_user(request):
    if request.method == "POST":
        fm = UserForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            print("the form is valid")
            return HttpResponseRedirect("/user/userread")
        else:
            print("the form is not valid")

    else:
        fm = UserForm()
        print("this is the get request")
    return render(request, "useradd.html", {"forms": fm})


@login_required(login_url="/")
def viewUser(request):
    data = User.objects.all()
    return render(request, "userread.html", {"datas": data})


@login_required(login_url="/")
def delete_user(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        print(data)
        print("hello")
        data.delete()
        messages.error(request, "The user has been deleted")

    return HttpResponseRedirect("/user/userread")


@login_required(login_url="/")
def update_user(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=data)
        if fm.is_valid():
            print("hello")
            fm.save()

            return HttpResponseRedirect("/user/userread")

    data = User.objects.get(pk=id)
    fm = UserForm(instance=data)

    return render(request, "updateuser.html", {"forms": fm})
