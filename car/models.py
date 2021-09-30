from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Car(models.Model):
    make = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    image_one = models.CharField(max_length=256)
    image_two = models.CharField(max_length=256)
    image_three = models.CharField(max_length=256)
    showroom = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)