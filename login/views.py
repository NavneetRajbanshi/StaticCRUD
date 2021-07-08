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


def login_user(request):
    if request.user.is_authenticated:
        print("authenticated")
        return HttpResponseRedirect("user/userread")
    if request.method == "POST":
        fm = LoginForm(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data.get("email")
            password = fm.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if not user.is_email_verified:
                messages.error(request, "Email is not verifed")
                return HttpResponseRedirect("/")
            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    "Login successful",
                )
                return HttpResponseRedirect("user/userread")
    fm = LoginForm()
    return render(request, "login.html", {"form": fm})
