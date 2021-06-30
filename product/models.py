from django.db import models

# Create your models here.


class Product(models.Model):
    productName = models.CharField(max_length=100)
    productQuantity = models.CharField(max_length=10)
    stock = models.IntegerField()
    price = models.FloatField(max_length=100)
    image = models.ImageField(upload_to="images/")
