from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rollno = models.CharField(max_length=50, primary_key = True)
    user_department = models.CharField(max_length=50)
    user_hostel = models.CharField(max_length=50)
    user_contact = models.IntegerField()

class UserTrips(models.Model):
    customuser = models.ForeignKey(User,on_delete = models.CASCADE)
    source = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)
    trip_datetime = models.DateTimeField(default = timezone.now)
    matches = models.IntegerField(default = 0)
