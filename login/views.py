from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView

from django.shortcuts import render


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
