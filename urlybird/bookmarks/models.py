from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Worm(models.Model):
    flink = models.TextField(max_length=2000)  # full url
    slink = models.CharField(max_length=200)  # short url
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    winfo = models.CharField(max_length=255)


class Click(models.Models):
    user = models.ForeignKey(User, null=True, blank=True)
    worm = models.ForeignKey(Worm)
    timestamp = models.DateTimeField()
