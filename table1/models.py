from django.db import models
from django.utils import timezone

# Create your models here.
class BasicForm(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name = 'basicform',blank = True)
    name = models.CharField(max_length=255,blank =True)
    Department = models.CharField(max_length = 255,blank =True)
    Directors_name = models.CharField(max_length = 255,blank =True)
    Team_leader = models.CharField(max_length = 255,blank =True)
    Number_of_TDOS_Department = models.IntegerField(default = 0)
    Month_of_Report = models.CharField(max_length=50,default=timezone.now(),blank = True)
    Division = models.CharField(max_length = 255,blank =True)
    Number_of_TDOS_Team = models.IntegerField(default = 0)
    Deignation = models.CharField(max_length = 255,blank =True)
    date = models.CharField(max_length=50,blank=True,default =timezone.now())
    
    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)

    def __str__(self) -> str:
        return self.Directors_name

