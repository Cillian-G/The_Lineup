from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Beach(models.Model):
    name = models.CharField(max_length=50)
    beach_image = CloudinaryField('image', default='placeholder')
    facing = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.name


class Session(models.Model):
    TIME_CHOICES = [
        ('06', '06.00'),
        ('07', '07.00'),
        ('08', '08.00'),
        ('09', '09.00'),
        ('10', '10.00'),
        ('11', '11.00'),
        ('12', '12.00'),
        ('13', '13.00'),
        ('14', '14.00'),
        ('15', '15.00'),
        ('16', '16.00'),
        ('17', '17.00'),
        ('18', '18.00'),
        ('19', '19.00'),
        ('20', '20.00'),
        ('21', '21.00'),
        ('22', '22.00'),
    ]
    
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE)
    time = models.CharField(
        max_length=2,
        choices=TIME_CHOICES)
    date = models.DateField(auto_now=False)
    surfer = models.ForeignKey(User, on_delete=models.CASCADE)
    
