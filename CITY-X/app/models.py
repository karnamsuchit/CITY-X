from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Reg_Guide(models.Model):
    aadhar_num = models.CharField(max_length=10)  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    description = models.TextField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)  
    gender = models.CharField(max_length=100)
    place_loc = models.CharField(max_length=100)
    price = models.IntegerField()
    age = models.CharField(max_length=2)  
    experience_years = models.PositiveIntegerField() 
    certificate = models.ImageField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


