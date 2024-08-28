from django.urls import path
from . import views
app_name = 'favorites'
urlpatterns = [
    path('' , views.favorites_page , name = 'favorites_page'),
    path('add-to-favorites/<slug:slug>' , views.add_to_favorites , name = 'add_to_favorites'),
    path('delete-from-favorites/<slug:slug>' , views.delete_from_favorites , name = 'delete_from_favorites')
]