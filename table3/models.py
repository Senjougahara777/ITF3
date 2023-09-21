from django.db import models

# Create your models here.

#formerly tna conducted
class TNA(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name = "tna",blank = True)
    serial_no = models.IntegerField()
    tnac = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)

