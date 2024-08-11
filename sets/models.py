from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    rolled=models.IntegerField()
    address=models.CharField(max_length=60)
    course=models.CharField(max_length=50)
    