from django.db import models

# Create your models here.

class Student(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    college=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    student_id=models.IntegerField(primary_key=True,default=0)
    
