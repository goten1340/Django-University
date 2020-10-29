from django.db import models


# Create your model
#class djangoClasses:
 #   Title = "Django University"
  #  Course = 1
   # Instructor Name = "Logan Hill"
   # Duration = 12.35
from django.db.models import Model


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.FloatField(max_length=60)