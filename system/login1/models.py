

from typing import AbstractSet
from django.contrib import messages
from django.db import models 

from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.CharField(max_length=2000)

class ITCategory(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    subcategory=models.CharField(max_length=200)
    category=models.ForeignKey(ITCategory, on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.subcategory




  

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=8,blank=False,null=False)
    is_superuser= models.BooleanField(default=False, verbose_name='superuser status')
   
    



class Productdb(models.Model):
    id = models.AutoField(primary_key=True)
    pid=models.CharField(max_length=250)
    category=models.ForeignKey(ITCategory, on_delete=models.CASCADE,default='')
    subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE,default='')
    product_name=models.CharField(max_length=120)
    product_brand=models.CharField(max_length=120)
    serial_no=models.CharField(max_length=32)
    model_no=models.CharField(max_length=18)
    description=models.CharField(max_length=2000)

    def __str__(self):
        return self.category
    def __str__(self):
        return self.subcategory

   

