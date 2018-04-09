from django.shortcuts import render
from .models import Event, EventGallery

# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request, 'foundation/events.html', {'events': events, 'title':'Events'})

def detail(request, pk):
    event = Event.objects.get(id=pk)
    pictures = EventGallery.objects.filter(event__id=pk)
    return render(request, 'foundation/event_detail.html', {'event':event, 'pictures':pictures, 'title':'Event Detail'})