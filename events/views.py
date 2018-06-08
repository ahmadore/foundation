from django.shortcuts import render
from .models import Event, EventGallery

# Create your views here.
def index(request):
    event_type =  request.GET.get('type')
    events = Event.objects.filter(event_type=event_type)
    return render(request, 'foundation/events.html', {'events': events, 'title':'Events'})

def detail(request, pk):
    event = Event.objects.get(id=pk)
    pictures = EventGallery.objects.filter(event__id=pk)
    return render(request, 'foundation/event_detail.html', {'event':event, 'pictures':pictures, 'title':'Event Detail'})