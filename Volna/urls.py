from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls')),
    path('artists/' , include('artists.urls')),
    path('releases/' , include('releases.urls')),
    path('events/' , include('events.urls')),
    path('contact/' , include('contact.urls')),
    path('news/' , include('news.urls')),
    path('account/' , include('account.urls')),
    path('favorites/' , include('favorites.urls')),
    path('comments/' , include('comments.urls')),
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)