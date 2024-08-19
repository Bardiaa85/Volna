from django.shortcuts import render
from .models import Release
from django.core.paginator import Paginator
import random
def releases_page(request):
   data = Release.objects.all()
   newest_releases = Release.objects.order_by("-release_date")[0 : 5]
   if request.method == "POST" :
        release_title = request.POST.get("release-search")
        data = Release.objects.filter(title__icontains = release_title)
   paginator = Paginator(data , 30)
   page_number = request.GET.get("page")
   this_page = paginator.get_page(page_number)
   this_page_content = list(this_page)
   random.shuffle(this_page_content)
   return render(request , "releases/releases.html" , {"paginator" : paginator.page_range , "active_page" : "releases" , "this_page" : this_page , "this_page_content" : this_page_content , "newest_releases" : newest_releases})
def single_release_page(request , slug):
    data = Release.objects.get(slug = slug)
    data.views = data.views + 1
    data.save()
    return render(request , "releases/single-release.html" , {"release" : data , "active_page" : "releases"})