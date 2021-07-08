from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("adduser/", views.create_user, name="useradd"),
    path("userread/", views.viewUser, name="userread"),
    path("deleteuser/<int:id>/", views.delete_user, name="deletedata"),
    path("<int:id>/", views.update_user, name="updateuser"),
]
