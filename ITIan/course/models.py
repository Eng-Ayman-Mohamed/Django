from django.db import models

# Create your models here.

class course(models.Model):
    name=models.CharField(max_length=20,db_index=True)
    instructor=models.CharField(max_length=20) 
    weight=models.IntegerField()
    startDate=models.DateField(blank=True,null=True)
    endDate=models.DateField(blank=True, null=True)
    createdAt=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name