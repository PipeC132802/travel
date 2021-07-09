from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Places(models.Model):
    name = models.CharField(max_length=256)
    lng = models.FloatField(max_length=20)
    lat = models.FloatField(max_length=20)


class Images(models.Model):
    image = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    meta = models.TextField(blank=True, null=True)


class UserPlaces(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ManyToManyField(Images, blank=True)
    date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)  # 1 visited, 2 favorite, 3 I want
