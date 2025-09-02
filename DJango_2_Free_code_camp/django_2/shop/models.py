from django.db import models

from django.shortcuts import render


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    summery = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name