# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-01 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='beers',
            field=models.IntegerField(default=0),
        ),
    ]