from django.db import models

# Create your models here.
class teachers(models.Model):
    user_name=models.CharField(max_length=50,null=True,default=None)
    teachers_id=models.CharField(max_length=50,null=True,default=None)
    fullname=models.CharField(max_length=50,null=True,default=None)
    password=models.CharField(max_length=50,null=True,default=None)
    department=models.CharField(max_length=500,null=True,default=None)
    