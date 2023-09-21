from django.db import models

# Create your models here.
class Section(models.Model):
    user = models.ForeignKey("accounts.User", related_name = "section", on_delete=models.CASCADE,blank = True)
    name = models.CharField(max_length=50)
    monthly = models.CharField(max_length=50)
    cum = models.CharField(max_length=50)
    achieve_per = models.IntegerField()
    remark = models.CharField(max_length=50)

    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)