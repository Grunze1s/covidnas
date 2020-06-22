"""Define the models to store gps data"""

from django.db import models
from covidnas.models import User

class Cluster(models.Model):
    longitude = models.FloatField(max_length=50)
    latitude = models.FloatField(max_length=50)
    radius = models.FloatField(max_length=50)
    label = models.IntegerField()

class GPSData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=50)
    longitude = models.FloatField(max_length=50)
    cluster = models.ForeignKey(Cluster, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField()


