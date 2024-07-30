from django.urls import path
from . import views
app_name = 'artists'
urlpatterns = [
    path('' , views.artists_page , name = 'artists_page'),
]