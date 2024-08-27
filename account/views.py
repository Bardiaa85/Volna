from django.shortcuts import render
from .forms import SignUpForm , SignInForm
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import login , logout
from django.conf import settings
from .models import Profile
from home.views import apply_profile
import random
def email_activation_code_maker():
    result = []
    for _ in range(5):
        result.append(str((random.randint(0 , 9))))
    return "".join(result)
def sign_up_page(request):
    if request.user.is_authenticated :
        return redirect("home:home_page")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get("email")
            new_user = User.objects.filter(email__iexact = user_email).exists()
            if new_user:
                form.add_error("email" , "ایمیل وارد شده معتبر نیست")
                return render(request , "account/signup.html" , {"active_page" : "main_page" , "form" : form}) 
            else : 
                user_full_name = request.POST.get("full_name")
                user_password = request.POST.get("password")
                new_user = User(email = user_email , password = user_password , is_active = False , username = user_email)    
                new_user.set_password(user_password)
                new_user.save()
                new_profile = Profile(username = new_user.username , related_user = new_user , full_name = user_full_name , email_activation_code = email_activation_code_maker())
                new_profile.save()
                html_message = render_to_string("email_templates/email-template.html" , context = {"email_activation_code" : new_profile.email_activation_code}) 
                plain_message = strip_tags(html_message)  
                send_mail(
                    subject = "فعالسازی حساب کاربری" ,
                    from_email = settings.EMAIL_HOST_USER ,
                    recipient_list = [new_user.email] ,
                    message = plain_message ,
                    html_message = html_message
                )             
                return redirect("account:email_activation_page" , username = new_user.username)
        else:
            return render(request , "account/signup.html" , {"active_page" : "main_page" , "form" : form})           
    return render(request , "account/signup.html" , {"active_page" : "main_page" , "form" : SignUpForm})
def email_activation_page(request , username):
    if request.user.is_authenticated :
        return redirect("home:home_page")
    if request.method == "POST":
        email_activation_code = Profile.objects.get(username = username).email_activation_code
        email_activation_code_input = request.POST.get("email-activation")
        if email_activation_code_input == email_activation_code :
            user = User.objects.get(username = username)
            user.is_active = True
            user.save()
            login(request , user)
            return redirect("home:home_page")
        else :
            return render(request , "account/email-activation.html" , {"active_page" : "main_page" , "error" : "کد وارد شده با کد ارسال شده مطابقت ندارد" , "username" : username})                   
    return render(request , "account/email-activation.html" , {"active_page" : "main_page" , "username" : username})
def sign_in_page(request):
    if request.user.is_authenticated :
        return redirect("home:home_page")
    if request.method == "POST" :
        form = SignInForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get("email")
            user = User.objects.filter(email__iexact = user_email).first()
            if user is not None:
                if user.is_active == False:
                    form.add_error("password" , "اکانت شما هنوز فعال نشده است")
                    return render(request , "account/signin.html" , {"active_page" : "main_page" , "form" : form})
                else:
                    user_password = request.POST.get("password")
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request , user)
                        return redirect('home:home_page')
                    else:
                        form.add_error("password" , "ایمیل یا رمز عبور شما نادرست است")
                        return render(request , "account/signin.html" , {"active_page" : "main_page" , "form" : form})
            else:
                form.add_error("password" , "ایمیل یا رمز عبور شما نادرست است")
                return render(request , "account/signin.html" , {"active_page" : "main_page" , "form" : form})
        else :
            return render(request , "account/signin.html" , {"active_page" : "main_page" , "form" : form})
    return render(request , "account/signin.html" , {"active_page" : "main_page" , "form" : SignInForm})
def log_out_page(request):
    if request.user.is_authenticated :
        logout(request)
        return redirect("home:home_page")
    return redirect("home:home_page")
def profile_page(request):
    if request.user.is_authenticated :
        user_full_name = apply_profile(request)
        user = request.user
        profile = Profile.objects.get(related_user = user)
        return render(request , "account/profile.html" , {"active_page" : "main_page" , "user_full_name" : user_full_name , "profile" : profile})
    else :
        return render(request , "shared/login-required.html" , {"active_page" : "main_page"})