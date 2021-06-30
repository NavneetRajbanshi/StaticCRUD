from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    vendor = models.CharField(max_length=40)
