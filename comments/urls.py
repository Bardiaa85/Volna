from django.urls import path
from . import views
app_name = 'comments'
urlpatterns = [
    path('adding-comment/<slug:slug>' , views.adding_comment , name = 'adding_comment'),

]