from django.db import models

# Create your models here.

class Car(models.Model):
    car_type = models.CharField(max_length=200,null=False)
    registration = models.CharField(max_length=5)
    is_Booked = models.BooleanField(default=False)

class SeftyFeature(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    feature = models.CharField(max_length=200,)
    

class UserProfile(models.Model):
    user_name = models.CharField(max_length=200,null=False)
    contact = models.IntegerField(null=False)
    Email = models.EmailField()
