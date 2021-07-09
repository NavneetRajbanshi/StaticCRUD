from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "login"
urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path(
        "activate-user/<uidb64>/<token>", views.activate_user, name="activate"
    ),
]
