from os import stat
from django.contrib import admin
from django.urls import path
from BookApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.index, name='home'),
    path("View_Books", views.View_Books, name='View_Books'),
    path("Add_Books", views.Add_Books, name='Add_Books'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)