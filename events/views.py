from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator
from home.views import apply_profile
from home.models import Logo , FooterInfo , BrowserTabInfo
def events_page(request):
    user_full_name = apply_profile(request)
    logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
    footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
    tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
    if request.method == "POST" :
        event_title = request.POST.get("event-search")
        data = Event.objects.filter(title__icontains = event_title)
    data = Event.objects.order_by("-event_date")
    paginator = Paginator(data , 6)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    return render(request , "events/events.html" , {"active_page" : "events" , "paginator" : paginator.page_range , "this_page" : this_page , "user_full_name" : user_full_name , "logo" : logo , "footer_info" : footer_info , "tab_info" : tab_info})
def single_event_page(request , slug):
    user_full_name = apply_profile(request)
    logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
    footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
    tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
    data = Event.objects.get(slug = slug)
    return render(request , "events/single-event.html" , {"event" : data , "active_page" : "events" , "user_full_name" : user_full_name , "logo" : logo , "footer_info" : footer_info , "tab_info" : tab_info})
