from django.shortcuts import render
from .models import Release
from events.models import Event
from django.core.paginator import Paginator
from account.models import Profile
from home.views import apply_profile
import random
def releases_page(request):
   user_full_name = apply_profile(request)
   data = Release.objects.all()
   events = Event.objects.order_by("-event_date")[0 : 2]
   newest_releases = Release.objects.order_by("-release_date")[0 : 5]
   if request.method == "POST" :
        release_title = request.POST.get("release-search")
        data = Release.objects.filter(title__icontains = release_title)
   paginator = Paginator(data , 30)
   page_number = request.GET.get("page")
   this_page = paginator.get_page(page_number)
   this_page_content = list(this_page)
   random.shuffle(this_page_content)
   return render(request , "releases/releases.html" , {"paginator" : paginator.page_range , "active_page" : "releases" , "this_page" : this_page , "this_page_content" : this_page_content , "newest_releases" : newest_releases , "events" : events , "user_full_name" : user_full_name})
def single_release_page(request , slug):
    if request.user.is_authenticated == False :
        return render(request , "shared/login-required.html" , {"active_page" : "releases"})
    profile = Profile.objects.get(related_user = request.user)
    user_full_name = apply_profile(request)
    data = Release.objects.get(slug = slug)
    favorites_list = profile.favorites_list.all()
    if data in favorites_list:
        in_favorites_list = True
    else :
        in_favorites_list = False
    data.views = data.views + 1
    data.save()
    return render(request , "releases/single-release.html" , {"release" : data , "active_page" : "releases" , "user_full_name" : user_full_name , "in_favorites_list" : in_favorites_list})