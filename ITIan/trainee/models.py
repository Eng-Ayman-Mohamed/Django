from django.db import models
from course.models import course
# Create your models here.

class trainee(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    numOfMonths=models.IntegerField()
    track=models.TextField()
    createdAt=models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='profile_images',default='default.png' , blank=True, null=True)
    course=models.ForeignKey(course, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName