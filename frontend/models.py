from django.db import models
from django.utils import timezone


# Create your models here.
class contactdb(models.Model):
    Name=models.CharField(max_length=70,null=True,blank=True)
    Email=models.CharField(max_length=70,null=True,blank=True)
    Message=models.CharField(max_length=70,null=True,blank=True)

class registerdb(models.Model):
    Name=models.CharField(max_length=70,null=True,blank=True)
    Email=models.CharField(max_length=70,null=True,blank=True,unique=True)
    Password=models.CharField(max_length=70,null=True,blank=True)

class cartdb(models.Model):
    Quantity=models.IntegerField(null=True,blank=True)
    Dishname=models.CharField(max_length=70,null=True,blank=True)
    Description=models.CharField(max_length=70,null=True,blank=True)
    Username=models.CharField(max_length=70,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)

