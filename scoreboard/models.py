from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Team(models.Model):
    members = models.ManyToManyField('auth.User', related_name='members', blank=True)
    score = models.IntegerField(default=0)
    beers = models.IntegerField(default=0)
