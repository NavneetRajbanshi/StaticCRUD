from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("adduser/", views.create_user, name="useradd"),
    path("userread/", views.viewUser, name="userread"),
    path("deleteuser/<int:id>/", views.delete_user, name="deletedata"),
    path("<int:id>/", views.update_user, name="updateuser"),
]
