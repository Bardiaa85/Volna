from django.urls import path
from . import views
app_name = 'releases'
urlpatterns = [
    path('' , views.releases_page , name = 'releases_page'),
    path('<slug:slug>' , views.single_release_page , name = "single_release_page"),
]