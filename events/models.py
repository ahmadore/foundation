from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=30, default='Agaie')
    image = models.ImageField(upload_to='static/img/event')
    
    def __str__(self):
        return "%s" %self.title

class EventGallery(models.Model):
    event = models.ForeignKey(Event, related_name='event_gallery')
    pics = models.ImageField(upload_to='static/img/event')
    description = models.CharField(max_length=50, null=True, blank=True)