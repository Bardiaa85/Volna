from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('' , views.home_page , name = 'home_page'),
    path('about/' , views.about_page , name = 'about_page'),
    path('search/' , views.search_page , name = 'search_page'),
    path('rules/' , views.rules_page , name = 'rules_page')
]