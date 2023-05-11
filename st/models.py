from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=50,null=True,default=None)
    roll=models.CharField(max_length=50,null=True,default=None)
    cgpa = models.FloatField(null=True,default=None)
    advisor =models.CharField(max_length=50,null=True,default=None)
    username=models.CharField(max_length=500,null=True,default=None)

    password=models.CharField(max_length=500,null=True,default=None)
    