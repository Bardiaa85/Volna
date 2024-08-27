from django.shortcuts import render
from .forms import ContactUsMessageModelForm
from home.views import apply_profile
def contact_us_page(request):
    user_full_name = apply_profile(request)
    if request.method == "POST" :
        form = ContactUsMessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        else :
            return render(request , "contact/contact.html" , {"form" : form , "active_page" : "main_page" , "yser_full_name" : user_full_name})
    return render(request , "contact/contact.html" , {"form" : ContactUsMessageModelForm , "active_page" : "main_page" , "user_full_name" : user_full_name})
    
