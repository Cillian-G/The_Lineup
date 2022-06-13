from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Day(models.Model):
    date = models.DateField
    notes = models.TextField(default='No notes today, happy surfing! :)')
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['date']


class Beach(models.Model):
    name = models.CharField(max_length=50)
    facing = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    notes = models.TextField()



