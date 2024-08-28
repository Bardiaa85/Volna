from django.shortcuts import render
from django.shortcuts import redirect
from account.models import Profile
from releases.models import Release
from home.views import apply_profile
from django.core.paginator import Paginator
def favorites_page(request):
    if request.user.is_authenticated == False :
        return render(request , "shared/login-required.html" , {"active_page" : "favorites"})
    user_full_name = apply_profile(request)
    profile = Profile.objects.get(related_user = request.user)
    favorites_list = profile.favorites_list.all()
    paginator = Paginator(favorites_list , 30)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    if len(favorites_list) == 0 :
        no_list = True
    else : 
        no_list = False
    return render(request , "favorites/favorites.html" , {"active_page" : "favorites" , "user_full_name" : user_full_name , "this_page" : this_page , "paginator" : paginator.page_range , "no_list" : no_list})
def add_to_favorites(request , slug):
    release = Release.objects.get(slug = slug)
    profile = Profile.objects.get(related_user = request.user)
    profile.favorites_list.add(release)
    return redirect("releases:single_release_page" , slug = slug)
def delete_from_favorites(request , slug):
    release = Release.objects.get(slug = slug)
    profile = Profile.objects.get(related_user = request.user)
    profile.favorites_list.remove(release)
    return redirect("releases:single_release_page" , slug = slug)