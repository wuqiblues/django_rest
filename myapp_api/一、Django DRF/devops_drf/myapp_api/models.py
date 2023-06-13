from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()