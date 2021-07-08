from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView

from django.shortcuts import render
from .models import User
from user.forms import UserForm


from .forms import LoginForm, RegisterForm

# Create your views here.


class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"

    def form_valid(self, form):
        print("the correct user the inside")
        request = self.request

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:

            return HttpResponseRedirect("user/userread")


def register(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "register.html", context)


def create_user(request):
    if request.method == "POST":
        fm = UserForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            print(fm.cleaned_data)
            return HttpResponseRedirect("/user/userread")
        else:
            print("the form is not valid")

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
