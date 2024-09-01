from django.shortcuts import render
from .forms import ContactUsMessageModelForm
from home.views import apply_profile
from home.models import Logo , FooterInfo , BrowserTabInfo
def contact_us_page(request):
    user_full_name = apply_profile(request)
    logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
    footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
    tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
    if request.method == "POST" :
        form = ContactUsMessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        else :
            return render(request , "contact/contact.html" , {"form" : form , "active_page" : "main_page" , "yser_full_name" : user_full_name , "footer_info" : footer_info , "logo" : logo , "tab_info" : tab_info})
    return render(request , "contact/contact.html" , {"form" : ContactUsMessageModelForm , "active_page" : "main_page" , "user_full_name" : user_full_name , "footer_info" : footer_info , "logo" : logo , "tab_info" : tab_info})
    
