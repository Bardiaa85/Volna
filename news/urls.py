from django.urls import path
from . import views
app_name = 'news'
urlpatterns = [
    path('' , views.news_page , name = 'news_page'),
    path('<slug:slug>' , views.single_article_page , name = "single_article_page")
]