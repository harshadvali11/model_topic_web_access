from django.shortcuts import render

# Create your views here.

from app.models import *



def display_topic(request):
    topics=Topic.objects.all()#['Danceobject','Skatingobject']
    return render(request,'display_topic.html',context={'topics':topics})