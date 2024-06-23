from datetime import timezone
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATUS_CHOICES = (
    ("Education", "Education"),
    ("Healthcare", "Healthcare"),
    ("Environment", "Environment"),
    ("Human Right", "Human Right"),
)
class NGO_info(models.Model):
    ngoid=models.AutoField(primary_key=True)
    name= models.CharField(max_length=90)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    address= models.CharField(max_length=100)
    password= models.CharField(max_length=20,null='False')
    confirm_password= models.CharField(max_length=20,null='False')
    mission= models.CharField(max_length=100,null='True')
    area= models.CharField(max_length=20, choices=STATUS_CHOICES)
class userinfo(models.Model):
    username= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=90)
    area= models.CharField(max_length=20, choices=STATUS_CHOICES)

class campaign(models.Model):
     name=models.CharField(max_length=100,null='False')
     description=models.TextField(max_length=100,null='False')
     goalamount=models.DecimalField(max_digits=10,decimal_places=2,null='False')
     sdate = models.DateField(auto_now_add=True,null='True')
     edate = models.DateField(null='False')
     cname=models.CharField(max_length=20,null='False')
     cemail=models.EmailField( null='False')
     cphone= models.CharField(max_length=10,null='False')
     ngoid=models.ForeignKey(NGO_info,on_delete=models.CASCADE,default=1)
     campaign_id=models.TextField(max_length=10,null='False')