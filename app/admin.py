# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Topic, Poems
from django.contrib import admin

# Register your models here.
admin.site.register(Topic)
admin.site.register(Poems)

