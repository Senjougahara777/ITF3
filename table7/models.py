from django.db import models

# Create your models here.
class STP2(models.Model):
    user = models.ForeignKey("accounts.User", related_name = "stp2", on_delete=models.CASCADE,blank = True)
    name = models.CharField(max_length=50)
    ttpi = models.CharField( max_length=50)
    date = models.CharField( max_length=50)
    no_org = models.IntegerField()
    no_part = models.IntegerField()
    course_fee = models.IntegerField()
    ammount = models.IntegerField()

    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)