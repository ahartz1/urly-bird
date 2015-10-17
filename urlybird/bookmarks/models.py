from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Worm(models.Model):
    flink = models.TextField(max_length=2000)  # full url
    slink = models.CharField(max_length=7)  # short url
    user = models.ForeignKey(User, null=True, blank=True)
    timestamp = models.DateTimeField()
    wtitle = models.CharField(max_length=100)
    winfo = models.CharField(max_length=255, null=True, blank=True)
    numclicks = models.PositiveIntegerField(null=True, blank=True)

    def save(self):
        try:
            self.numclicks = self.click_set.all().count()
        except:
            pass
        self.flink = self.flink.strip()
        super(Worm, self).save()


class Click(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    worm = models.ForeignKey(Worm)
    timestamp = models.DateTimeField()
