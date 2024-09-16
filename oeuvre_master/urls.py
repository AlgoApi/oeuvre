from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from oeuvre_master.views import Home, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('telebot/$', include('telebot.urls')),
    path("update/", update, name="update")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)