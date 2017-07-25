# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic
from django.template import loader

# Create your views here.
def index(request):
    all_topics=Topic.objects.all()
    html=""
    for topic in all_topics:
        url="/app/"+str(topic.id)+'/'
        html += '<a href="' + url +'">'+topic.tname +'</a><br>'
    
    return HttpResponse(html)

def detail(request, topic_id):
    return HttpResponse("<h2>Details for topic id:" + str(topic_id) +"  </h2>")
