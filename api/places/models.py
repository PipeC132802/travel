from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Places(models.Model):
    name = models.CharField(max_length=256)
    lon = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)


class Images(models.Model):
    def photo_path(instance, filename):
        filename = 'travel_{0}'.format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S%f"))
        return 'travellers/{0}'.format(filename + ".jpg")

    image = models.ImageField(upload_to=photo_path, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)


class UserPlaces(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ForeignKey(Images, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    status = models.IntegerField()  # 1 visited, 2 favorite, 3 I want
