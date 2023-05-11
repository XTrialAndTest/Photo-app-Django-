from django.db import models
from cloudinary.models import CloudinaryField


#  authentication

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.


class Photo(models.Model):
    CHOICE = (('photo', 'photo'), ('portrait', 'portrait'),
              ('artwork', 'artwork'),)
    title = models.CharField(max_length=200)
    photo = CloudinaryField("my_picture.jpg")
    description = models.CharField(max_length=200)
    tags = models.CharField(

        max_length=200, choices=CHOICE, default='photo')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
