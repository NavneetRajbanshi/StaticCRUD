from django.contrib import admin
from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path("productadd/", views.ProductAdd.as_view(), name="productadd"),
    path("productread/", views.ProductView.as_view(), name="productread"),
]