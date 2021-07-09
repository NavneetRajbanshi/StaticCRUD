from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import (
    force_bytes,
    force_str,
    force_text,
    DjangoUnicodeDecodeError,
)
from .utils import generate_token
from django.conf import settings
from django.core.mail import EmailMessage

from django.shortcuts import redirect, render


from .forms import LoginForm, RegisterForm, User

# Create your views here.


def send_activation_email(user, request):

    current_site = get_current_site(request)
    email_subject = "Activate Your Account"
    email_body = render_to_string(
        "activation.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.id)),
            "token": generate_token.make_token(user),
        },
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_FROM_USER,
        to=[user.email],
    )
    email.send()


def login_user(request):
    print("hello")
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


class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"

    def form_valid(self, form):
        request = self.request
        current_user = request.user
        print(current_user)
        if request.user.is_authenticated:

            return HttpResponseRedirect("user/userread")
        else:
            if form.is_valid():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=email, password=password)

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("user/userread")


def register(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                print("user created")
                return redirect("login")

        else:
            messages.info(request, "password not matching..")
        return redirect("register")

    else:
        return render(request, "register.html")


def logout_user(request):
    logout(request)

    return HttpResponseRedirect("/")


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.active = True
        user.save()
        messages.success(request, "Email Verified. Please sign in to continue")
        return redirect(reverse("login.html"))
    else:
        return render(request, "activation-failed.html", {"user": user})


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.html"
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@example.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="password_reset.html",
        context={"password_reset_form": password_reset_form},
    )
