# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-06 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180406_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='static/img/event'),
        ),
    ]
