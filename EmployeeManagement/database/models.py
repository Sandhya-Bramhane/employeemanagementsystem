from django.db import models

# Create your models here.

class empregister(models.Model):
    empoid = models.IntegerField(default=1)
    name = models.CharField(max_length=40)
    birthdate = models.CharField(default=27-6-2003,max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    jobtitle = models.CharField(max_length=50)
    department = models.CharField(max_length=40)