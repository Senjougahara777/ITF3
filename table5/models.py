from django.db import models
from django.utils import timezone

# Create your models here.
class STP(models.Model):
    user = models.ForeignKey("accounts.User", related_name = "stp", on_delete=models.CASCADE,blank = True)
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False,default = timezone.now())
    no_org = models.IntegerField()
    no_part = models.IntegerField()
    course_fee = models.IntegerField()
    ammount = models.IntegerField()

    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)

    def __str__(self) -> str:
        return self.name

