from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('' , views.contact_us_page , name = 'contact_us_page'),
]