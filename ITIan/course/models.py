from django.db import models

# Create your models here.

class course(models.Model):
    name=models.CharField(max_length=20)
    instructor=models.CharField(max_length=20) 
    weight=models.IntegerField()
    startDate=models.DateField()
    endDate=models.DateField()
    createdAt=models.DateField(auto_now_add=True)