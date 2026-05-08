from django.db import models

# Create your models here.

class trainee(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    numOfMonths=models.IntegerField()
    track=models.TextField()
    createdAt=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstName