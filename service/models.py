from django.db import models

# Create your models here.


class Employee(models.Model):
    full_name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    mob_num=models.IntegerField()
    password=models.CharField(max_length=100)

