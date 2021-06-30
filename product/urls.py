from django.contrib import admin
from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path("productadd/", views.create_product, name="productadd"),
    path("productread/", views.show_product, name="productread"),
    path("deleteuser/<int:id>/", views.delete_product, name="deleteproduct"),
    path("<int:id>/", views.update_product, name="updateproduct"),
]
