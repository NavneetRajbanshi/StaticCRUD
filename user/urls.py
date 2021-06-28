from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("", views.UserAdd.as_view(), name="useradd"),
    path("userread/", views.UserView.as_view(), name="userread"),
]