from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class catdb(models.Model):
    CategoryName=models.CharField(max_length=90,null=True,blank=True)
    Description=models.CharField(max_length=90,null=True,blank=True)
    Image=models.ImageField(upload_to="categoryimages",null=True,blank=True)
class productdb(models.Model):
    CategoryName = models.CharField(max_length=90, null=True, blank=True)
    ProductName = models.CharField(max_length=90, null=True, blank=True)
    Description = models.CharField(max_length=90, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    ProductImage = models.ImageField(upload_to="productimages", null=True, blank=True)

def validate_future_date(value):
    if value <= timezone.now().date():
        raise ValidationError("Booking date must be in the future.")
class bookingdb(models.Model):
    Country=models.CharField(max_length=77,null=True,blank=True)
    Events=models.CharField(max_length=77,null=True,blank=True)
    Palace=models.CharField(max_length=77,null=True,blank=True)
    Contact=models.CharField(max_length=77,null=True,blank=True)
    Name=models.CharField(max_length=77,null=True,blank=True)
    Date=models.DateField(validators=[validate_future_date],null=True)
    Email=models.EmailField(max_length=77,null=True,blank=True)

class Eventdb(models.Model):
    Eventname=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="Eventimage",null=True,blank=True)
    image1=models.ImageField(upload_to="Eventimage",null=True,blank=True)
    image2=models.ImageField(upload_to="Eventimage",null=True,blank=True)
    image3=models.ImageField(upload_to="Eventimage",null=True,blank=True)
    image4=models.ImageField(upload_to="Eventimage",null=True,blank=True)
    image5=models.ImageField(upload_to="Eventimage",null=True,blank=True)
    image6=models.ImageField(upload_to="Eventimage",null=True,blank=True)

