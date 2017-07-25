# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    tname=models.CharField(max_length=250)
    recent_writter=models.CharField(max_length=250)

    def __str__(self):
        return self.tname

class Poems(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    ptitle=models.CharField(max_length=250)
    file_type=models.CharField(max_length=250)
    
    def __str__(self):
        return self.ptitle
    
