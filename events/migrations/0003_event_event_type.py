# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-08 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180602_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('E', 'Event'), ('A', 'Award')], default='E', max_length=1),
        ),
    ]