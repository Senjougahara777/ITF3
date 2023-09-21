from django.db import models

# Create your models here.
class DTPA(models.Model):
    NTAC = models.CharField(max_length=50,default = "")
    target = models.IntegerField(default = 100)
    monthly = models.CharField(max_length=50,default = "september")
    achieve_per = models.IntegerField(default = 0)
    remarks = models.CharField(max_length=50,default = "Good")

    NTPD = models.CharField(max_length=50,default = "")
    target2 = models.IntegerField(default = 100)
    monthly2 = models.CharField(max_length=50,default = "september")
    achieve_per2 = models.IntegerField(default = 0)
    remarks2 = models.CharField(max_length=50,default = "Good")
    
    NTPI = models.CharField(max_length=50,default = "")
    target3 = models.IntegerField(default = 100)
    monthly3 = models.CharField(max_length=50,default = "september")
    achieve_per3 = models.IntegerField(default = 0)
    remarks3 = models.CharField(max_length=50,default = "Good")
    
    NTPS = models.CharField(max_length=50,default = "")
    target4 = models.IntegerField(default = 100)
    monthly4 = models.CharField(max_length=50,default = "september")
    achieve_per4 = models.IntegerField(default = 0)
    remarks4 = models.CharField(max_length=50,default = "Good")
    
    AGTP = models.CharField(max_length=50,default = "")
    target5 = models.IntegerField(default = 100)
    monthly5 = models.CharField(max_length=50,default = "september")
    achieve_per5 = models.IntegerField(default = 0)
    remarks5 = models.CharField(max_length=50,default = "Good")
    
    user = models.ForeignKey("accounts.User", related_name = "dtpa", on_delete=models.CASCADE,blank = True)

    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)
   