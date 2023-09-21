from django.db import models
from django.contrib.auth.models import AbstractUser
from table1.models import BasicForm
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=50,default = "John Doe")
    avatar = models.ImageField(default = "default2.png",blank = True)
    username = models.CharField(max_length=50,unique = True)
    is_AreaManager = models.BooleanField(default = False,blank = True) 
    is_HOT = models.BooleanField(default = False,blank = True)
    is_CDN = models.BooleanField(default = False,blank = True)
    is_verified = models.BooleanField(default = False,blank = True)
    is_TDO = models.BooleanField(default = False,blank = True)


class Area_Manager(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)

class Director(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)

