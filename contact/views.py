from django.shortcuts import render
from .forms import ContactUsMessageModelForm
def contact_us_page(request):
    if request.method == "POST" :
        form = ContactUsMessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        else :
            return render(request , "contact/contact.html" , {"form" : form , "active_page" : "main_page"})
    return render(request , "contact/contact.html" , {"form" : ContactUsMessageModelForm , "active_page" : "main_page"})
    
