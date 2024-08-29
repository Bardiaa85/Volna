from django.shortcuts import render
from django.shortcuts import redirect
from artists.models import Artist
from releases.models import Release
from events.models import Event
from news.models import Article
from account.models import Profile
from .models import SliderShow , AboutUsText , RulesText
def apply_profile(request):
    if request.user.is_authenticated :
        user = request.user
        return Profile.objects.get(related_user = user).full_name
    else :
        return None   
import random
def home_page(request):
    user_full_name = apply_profile(request)
    artists = list(Artist.objects.all())
    slider_show = list(SliderShow.objects.all())[-1] if len(SliderShow.objects.all()) != 0 else None
    artists = random.sample(artists , 9)
    newest_releases1 = Release.objects.order_by("-release_date")[0 : 12]
    newest_releases2 = Release.objects.order_by("-release_date")[0 : 5]
    most_viewed_releases = Release.objects.order_by("-views")[0 : 5]
    most_commented_releases = list(Release.objects.all())
    most_commented_releases.sort(key = lambda release : release.len_comments() , reverse = True)
    most_commented_releases = most_commented_releases[0 : 5]
    events = Event.objects.order_by("-event_date")[0 : 4]
    news = Article.objects.order_by("-article_date")[0 : 3]
    return render(request , "home/home.html" , {"active_page" : "main_page" , "artists" : artists , "newest_releases1" : newest_releases1 , "newest_releases2" : newest_releases2 , "most_viewed_releases" : most_viewed_releases , "events" : events , "news" : news , "user_full_name" : user_full_name , "most_commented_releases" : most_commented_releases, "slider_show" : slider_show})
def about_page(request):
    user_full_name = apply_profile(request)
    about_us_text = list(AboutUsText.objects.all())[-1] if len(AboutUsText.objects.all()) != 0 else None
    return render(request , "home/about.html" , {"active_page" : "main_page" , "user_full_name" : user_full_name , "about_us_text" : about_us_text})
def search_page(request):
    user_full_name = apply_profile(request)
    if request.method == "POST":
        title = request.POST.get("all-search")
        artists = Artist.objects.filter(nickname__icontains = title)
        releases = Release.objects.filter(title__icontains = title)
        if len(list(artists)) == 0 and len(list(releases)) == 0 :
            noresult = True
        else :
            noresult = False
        return render(request , "home/search.html" , {"artists" : artists , "releases" : releases , "active_page" : "main_page" , "no_result" : noresult , "user_full_name" : user_full_name})
    else :
        return redirect("home:home_page")
def rules_page(request):
    user_full_name = apply_profile(request)
    rules_text = list(RulesText.objects.all())[-1] if len(RulesText.objects.all()) != 0 else None
    return render(request , "home/rules.html" , {"active_page" : "main_page" , "user_full_name" : user_full_name , "rules_text" : rules_text})