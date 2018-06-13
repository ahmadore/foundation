from __future__ import unicode_literals

from django.db import models

EVENT_TYPE = (
    ('E', 'Event'),
    ('A', 'Award')
    )


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=40)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPE, default='E')
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=30, default='Agaie')
    image = models.ImageField(upload_to='img/event')
    
    def __str__(self):
        return "%s" %self.title

class EventGallery(models.Model):
    event = models.ForeignKey(Event, related_name='event_gallery')
    pics = models.ImageField(upload_to='img/event')
    description = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return "%s" %self.pics.name
