from django.shortcuts import render
from .models import Artist
from django.core.paginator import Paginator
from home.views import apply_profile
import random
def artists_page(request):
    user_full_name = apply_profile(request)   
    data = Artist.objects.all()
    if request.method == "POST" :
        artist_nickname = request.POST.get("artist-search")
        data = Artist.objects.filter(nickname__icontains = artist_nickname)
    paginator = Paginator(data , 18)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    this_page_content = list(this_page)
    random.shuffle(this_page_content)
    return render(request , "artists/artists.html" , {"this_page_content" : this_page_content , "this_page" : this_page , "paginator" : paginator.page_range , "active_page" : "artists" , "user_full_name" : user_full_name})
def single_artist_page(request , slug) :
    user_full_name = apply_profile(request)
    data = Artist.objects.get(slug = slug)
    releases = data.release_set.all()
    return render(request , "artists/single-artist.html" , {"artist" : data , "related_releases" : releases , "active_page" : "artists" , "user_full_name" : user_full_name})
