from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=50,null=True,default=None)
    roll=models.CharField(max_length=50,null=True,default=None)
    cgpa = models.FloatField(null=True,default=None)
    advisor =models.CharField(max_length=50,null=True,default=None)
    username=models.CharField(max_length=500,null=True,default=None)
    password=models.CharField(max_length=500,null=True,default=None)
    cgpa1 = models.FloatField(null=True,default=-1)
    cgpa2 = models.FloatField(null=True,default=-1)
    cgpa3 = models.FloatField(null=True,default=-1)
    cgpa4 = models.FloatField(null=True,default=-1)
    cgpa5 = models.FloatField(null=True,default=-1)
    cgpa6 = models.FloatField(null=True,default=-1)
    cgpa7 = models.FloatField(null=True,default=-1)
    cgpa8 = models.FloatField(null=True,default=-1)
    
    def __str__(self):
        return self.name
    
class teachers(models.Model):
    user_name=models.CharField(max_length=50,null=True,default=None)
    teachers_id=models.CharField(max_length=50,null=True,default=None)
    fullname=models.CharField(max_length=50,null=True,default=None)
    password=models.CharField(max_length=50,null=True,default=None)
    department=models.CharField(max_length=500,null=True,default=None)
    
    def __str__(self):
        return self.fullname