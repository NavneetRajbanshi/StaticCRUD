from django.contrib.messages.constants import SUCCESS
from django.http.response import HttpResponse, HttpResponseRedirect
from user.forms import UserForm
from django.shortcuts import render
from django.contrib import messages


from .models import User

# Create your views here.


def create_user(request):

    if request.method == "POST":
        print("this is the post request")
        fm = UserForm(request.POST, request.FILES)
        print(fm["image"])
        if fm.is_valid():
            nm = fm.changed_data["name"]
            em = fm.changed_data["email"]
            ad = fm.changed_data["address"]
            pw = fm.changed_data["password"]
            reg = User(name=nm, email=em, address=ad, password=pw)
            reg.save()

        else:
            print("the form is not valid")

    else:
        fm = UserForm()
        print("this is the get request")
    return render(request, "useradd.html", {"forms": fm})


def viewUser(request):
    data = User.objects.all()
    return render(request, "userread.html", {"datas": data})


def delete_user(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        print(data)
        print("hello")
        data.delete()
        messages.success(request, "New user has been created")

    return HttpResponseRedirect("/user/userread")


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
