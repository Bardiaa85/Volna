from django.shortcuts import render
from .models import Release
from events.models import Event
from django.core.paginator import Paginator
from account.models import Profile
from home.views import apply_profile
from home.models import Logo , FooterInfo , BrowserTabInfo
import random
def releases_page(request):
   user_full_name = apply_profile(request)
   logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
   footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
   tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
   data = Release.objects.order_by("-id")
   events = Event.objects.order_by("-event_date")[0 : 2]
   newest_releases = Release.objects.order_by("-release_date")[0 : 5]
   if request.method == "POST" :
        release_title = request.POST.get("release-search")
        data = Release.objects.filter(title__icontains = release_title)
   paginator = Paginator(data , 42)
   page_number = request.GET.get("page")
   this_page = paginator.get_page(page_number)
   this_page_content = list(this_page)
   random.shuffle(this_page_content)
   return render(request , "releases/releases.html" , {"paginator" : paginator.page_range , "active_page" : "releases" , "this_page" : this_page , "this_page_content" : this_page_content , "newest_releases" : newest_releases , "events" : events , "user_full_name" : user_full_name , "logo" : logo , "footer_info" : footer_info , "tab_info" : tab_info})
def single_release_page(request , slug):
    logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
    footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
    tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
    if request.user.is_authenticated == False :
        return render(request , "shared/login-required.html" , {"active_page" : "releases" , "logo" : logo , "footer_info" : footer_info , "tab_info" : tab_info})
    profile = Profile.objects.get(related_user = request.user)
    user_full_name = apply_profile(request)
    data = Release.objects.get(slug = slug)
    profile.listening_history.add(data)
    profile.save()
    favorites_list = profile.favorites_list.all()
    comments_list = data.comment_set.order_by("-comment_date")
    if data in favorites_list:
        in_favorites_list = True
    else :
        in_favorites_list = False
    data.views = data.views + 1
    data.save()    
    return render(request , "releases/single-release.html" , {"release" : data , "active_page" : "releases" , "user_full_name" : user_full_name , "in_favorites_list" : in_favorites_list , "comments_list" : comments_list , "footer_info" : footer_info , "logo" : logo , "tab_info" : tab_info})