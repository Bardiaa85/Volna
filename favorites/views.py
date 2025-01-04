from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from account.models import Profile
from releases.models import Release
from home.views import apply_profile
from django.core.paginator import Paginator
from home.models import Logo , FooterInfo , BrowserTabInfo
def favorites_page(request):
    logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
    footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
    tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
    if request.user.is_authenticated == False :
        return render(request , "shared/login-required.html" , {"active_page" : "favorites" , "logo" : logo , "footer_info" : footer_info , "tab_info" : tab_info})
    user_full_name = apply_profile(request)
    profile = Profile.objects.get(related_user = request.user)
    favorites_list = profile.favorites_list.order_by("-id")
    paginator = Paginator(favorites_list , 30)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    if len(favorites_list) == 0 :
        no_list = True
    else : 
        no_list = False
    return render(request , "favorites/favorites.html" , {"active_page" : "favorites" , "user_full_name" : user_full_name , "this_page" : this_page , "paginator" : paginator.page_range , "no_list" : no_list , "logo" : logo , "footer_info" : footer_info , "tab_info" : tab_info})
def add_to_favorites(request , slug):
    release = Release.objects.get(slug = slug)
    profile = Profile.objects.get(related_user = request.user)
    profile.favorites_list.add(release)
    data = {"status" : "success" , "message" : "Data saved successfully"}
    return JsonResponse(data)
def delete_from_favorites(request , slug):
    release = Release.objects.get(slug = slug)
    profile = Profile.objects.get(related_user = request.user)
    profile.favorites_list.remove(release)
    data = {"status" : "success" , "message" : "Data saved successfully"}
    return JsonResponse(data)