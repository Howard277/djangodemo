# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)

class Role(models.Model):
    code=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)