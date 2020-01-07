from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


class Date(models.Model):
    text = models.CharField(max_length=50)
    day = models.DecimalField(default=0, decimal_places=0,max_digits=3)
    month = models.CharField(max_length=5)
    year = models.DecimalField(default=0, decimal_places=0,max_digits=4)
    hour = models.DecimalField(default=0, decimal_places=0, max_digits=2)
    minute = models.DecimalField(default=0, decimal_places=0,max_digits=2)
    second = models.DecimalField(default=0, decimal_places=0,max_digits=2)

    def __str__(self):
        return self.text

class Photo(models.Model):
    name = models.CharField(max_length=50)
    photo = cloudinary.models.CloudinaryField('image')

    def __str__(self):
        return self.name