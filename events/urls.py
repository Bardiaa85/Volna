from django.urls import path
from . import views
app_name = 'events'
urlpatterns = [
    path('' , views.events_page , name = 'events_page'),
    path('<slug:slug>' , views.single_event_page , name = "single_event_page")
]