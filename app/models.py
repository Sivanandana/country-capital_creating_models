from django.db import models

# Create your models here.
class Country(models.Model):
    cname=models.CharField(max_length=100)
    no=models.IntegerField()
class Capital(models.Model):
    cname=models.ForeignKey(Country,on_delete=models.CASCADE)
    no=models.IntegerField()
    cp_name=models.CharField(max_length=100)
    population=models.IntegerField()
