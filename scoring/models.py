from django.db import models

# Create your models here.
class Employee(models.Model):
    includeAt= models.CharField(max_length=50)
    employeedId= models.IntegerField(unique=True)
    employerId= models.IntegerField(unique=True)


