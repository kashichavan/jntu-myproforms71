from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    photo=models.ImageField(upload_to='media/')
