from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from ParadiseApp.views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^delete_roll/(?P<roll_id>\d+)/$', delete_roll, name='delete_roll'),
    url(r'^rolls', rolls, name='rolls'),
    url(r'^overview', overview, name='overview'),
    url(r'^plans', plans, name='plans'),
    url(r'^plan/(?P<plan_id>\d+)/$', plan, name='plan'),
    url(r'^process/(?P<roll_id>\d+)/$', process, name='process'),
    url(r'^add_pack/(?P<roll_id>\d+)/$', add_pack, name='add_pack'),
    url(r'^delete_pack/(?P<pack_id>\d+)/(?P<roll_id>\d+)/$', delete_pack, name='delete_pack'),

]