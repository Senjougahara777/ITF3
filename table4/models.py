from django.db import models

# Create your models here.
class TTPD(models.Model):
    user = models.ForeignKey("accounts.User", related_name = "ttpd", on_delete=models.CASCADE,blank = True)
    name = models.CharField(max_length=50)
    ttpd = models.CharField( max_length=50)
    submitted = models.BooleanField(default = False)
    remarks = models.TextField()

    verified_hot = models.BooleanField(default = False,blank = True)
    rejected = models.BooleanField(default = False,blank = True)
    verified_manager = models.BooleanField(default = False,blank = True)
    rejected2 = models.BooleanField(default = False,blank = True)
    approved = models.BooleanField(default = False,blank = True)

    def __str__(self) -> str:
        return self.name
