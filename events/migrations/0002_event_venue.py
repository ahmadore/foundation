# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-06 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='Agaie', max_length=30),
        ),
    ]
