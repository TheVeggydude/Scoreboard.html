# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0005_assignment_available'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assignment',
            new_name='Exercise',
        ),
    ]