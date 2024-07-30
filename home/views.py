from django.shortcuts import render
from artists.models import Artist
import random
def home_page(request):
    data = list(Artist.objects.all())
    data = random.sample(data , 9)
    return render(request , "home/home.html" , {"active_page" : "main_page" , "artists" : data})
