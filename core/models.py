# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True, null=True)
    sn = models.CharField(max_length=64)
    imei = models.CharField(max_length=64)
    os_version = models.CharField(max_length=32)
    last_heartbeat = models.IntegerField(null=True)
    stauts = models.CharField(max_length=32)