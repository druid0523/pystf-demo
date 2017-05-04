from __future__ import absolute_import

from django.conf.urls import url

import demo.views as views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^heartbeat$', views.heartbeat_device),
    url(r'^devices$', views.list_device),
    url(r'^device/(?P<device_id>(\d)+)/connect$', views.connect_device),
]
