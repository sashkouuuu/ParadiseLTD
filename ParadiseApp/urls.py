from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from ParadiseApp.views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create_roll', create_roll, name='create_roll'),
    url(r'^rolls', rolls, name='rolls')
]