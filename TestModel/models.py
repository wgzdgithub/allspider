from django.db import models


class Test(models.Model):
    rank = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    star = models.CharField(max_length=200)
    num = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
# Create your models here.
