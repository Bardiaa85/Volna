from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('sign-up/' , views.sign_up_page , name = 'sign_up_page'),
    path('sign-in/' , views.sign_in_page , name = 'sign_in_page'),
    path('email-activation/<str:username>' , views.email_activation_page , name = 'email_activation_page'),
    path('log-out/' , views.log_out_page , name = "log_out_page"),
    path('profile/' , views.profile_page , name = "profile_page")
]