# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from reddit import models


# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Vote)
