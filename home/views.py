from django.shortcuts import render
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