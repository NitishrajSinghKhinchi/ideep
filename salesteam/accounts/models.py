from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from datetime import datetime

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    """we can create Phonenumber Fields with the help of third party package But t have used Charfields"""
    mobile_no= models.CharField(blank=True,max_length=15,unique=True)
    email = models.EmailField(blank=True,unique=True)
    Age = models.PositiveIntegerField(blank=True,null=True)
    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.mobile_no

class Working(models.Model):
    area_visited = models.CharField(max_length=500)
    total_person = models.PositiveIntegerField()
    number_of_leads = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=datetime.now())


GENDER = (('male','Male'), ('female','Female'), ('other','Other'))
class Client(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER,blank=True)
    family_member=models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=datetime.now())