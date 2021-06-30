from django.contrib import admin
from django.urls import path
from . import views

app_name = "category"
urlpatterns = [
    path("categoryadd/", views.add_category, name="categoryadd"),
    path("categoryread/", views.show_category, name="categoryread"),
    path(
        "deletecategory/<int:id>", views.delete_category, name="deletecategory"
    ),
    path("<int:id>", views.update_category, name="updatecategory"),
]
