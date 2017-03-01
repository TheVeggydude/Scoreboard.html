from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=10000)
    members = models.ManyToManyField('auth.User', related_name='members', blank=True)
    score = models.IntegerField(default=0)
    beers = models.IntegerField(default=0)

    def __str__(self):
        return self.name
