from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Ticket(models.Model):
    date = models.DateField()
    description = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name