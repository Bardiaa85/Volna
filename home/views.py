from django.shortcuts import render
from django.shortcuts import redirect
from artists.models import Artist
from releases.models import Release
from events.models import Event
from news.models import Article
import random
def home_page(request):
    artists = list(Artist.objects.all())
    artists = random.sample(artists , 9)
    newest_releases1 = Release.objects.order_by("-release_date")[0 : 12]
    newest_releases2 = Release.objects.order_by("-release_date")[0 : 5]
    most_viewed_releases = Release.objects.order_by("-views")[0 : 5]
    events = Event.objects.order_by("-event_date")[0 : 4]
    news = Article.objects.order_by("-article_date")[0 : 3]
    return render(request , "home/home.html" , {"active_page" : "main_page" , "artists" : artists , "newest_releases1" : newest_releases1 , "newest_releases2" : newest_releases2 , "most_viewed_releases" : most_viewed_releases , "events" : events , "news" : news})
def about_page(request):
    return render(request , "home/about.html" , {"active_page" : "main_page"})
def search_page(request):
    if request.method == "POST":
        title = request.POST.get("all-search")
        artists = Artist.objects.filter(nickname__icontains = title)
        releases = Release.objects.filter(title__icontains = title)
        if len(list(artists)) == 0 and len(list(releases)) == 0 :
            noresult = True
        else :
            noresult = False
        return render(request , "home/search.html" , {"artists" : artists , "releases" : releases , "active_page" : "main_page" , "no_result" : noresult})
    else :
        return redirect("home:home_page")
