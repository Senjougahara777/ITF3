from django.db import models

# Create your models here.
class BasicInfo(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name = "basicinfo",blank = True)
    name = models.CharField(max_length=255, blank = True)
    Area_Office = models.CharField(max_length=255, blank = True)
    category = models.CharField(max_length=255, blank = True)
    CCN = models.CharField(max_length=255, blank = True)
    NHT = models.IntegerField(default=0,blank = True)
    Designation = models.CharField(max_length=255, blank = True)
    NAM = models.CharField(max_length=255, blank = True)
    Designation1 = models.CharField(max_length=255, blank = True)
    Date = models.CharField(max_length=255, blank = True)
    Month_of_report = models.CharField(max_length=255, blank = True)

    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)

    def __str__(self):
        return self.name