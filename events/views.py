from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator
def events_page(request):
    if request.method == "POST" :
        event_title = request.POST.get("event-search")
        data = Event.objects.filter(title__icontains = event_title)
    data = Event.objects.order_by("-event_date")
    paginator = Paginator(data , 6)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    return render(request , "events/events.html" , {"active_page" : "events" , "paginator" : paginator.page_range , "this_page" : this_page})
def single_event_page(request , slug):
    data = Event.objects.get(slug = slug)
    return render(request , "events/single-event.html" , {"event" : data , "active_page" : "events"})
