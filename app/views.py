from django.shortcuts import render

# Create your views here.

from app.models import *

from django.db.models import Q

from django.http import HttpResponse



def display_topic(request):
    topics=Topic.objects.all()#['Danceobject','Skatingobject']
    #topics=Topic.objects.filter(topic_name='Skating')
    return render(request,'display_topic.html',context={'topics':topics})


def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='Skating')
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.filter(topic_name='Skating').order_by('name')
    #webpages=Webpage.objects.filter(topic_name='Skating').order_by('-name')
    #webpages=Webpage.objects.all()[::-1]
    #webpages=Webpage.objects.exclude(topic_name='Skating')
    #webpages=Webpage.objects.filter(name__startswith='M')
    #webpages=Webpage.objects.filter(name__endswith='w')
    #webpages=Webpage.objects.filter(name__contains='s')
    #webpages=Webpage.objects.filter(Q(name__contains='s') & Q(name__startswith='a'))
    #webpages=Webpage.objects.filter(Q(name__contains='s') | Q(name__startswith='a'))
    #webpages=Webpage.objects.filter(Q(name__contains='s'))

    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access(request):
    #access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date__gt='1984-12-18')
    #access=Access_Records.objects.filter(date__gte='1984-12-18')
    #access=Access_Records.objects.filter(date__lte='1984-12-18')
    #access=Access_Records.objects.filter(date__month='12')
    #access=Access_Records.objects.filter(date__year='1984')
    access=Access_Records.objects.filter(date__day__lt='18')
    
    
    
    return render(request,'display_access.html',context={'access':access})



def delete_webpage(request):
    Webpage.objects.filter(name='Allison').delete()
    #return HttpResponse('one record has been deleted successfully')
    #Webpage.objects.all().delete()
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})
    

def update_webpage(request):
    #Webpage.objects.filter(name='Kelly').update(name='Dhoni',url='https://dhoni.com')
    #Webpage.objects.filter(topic_name='Dieting').update(name='Kohli')
    #Webpage.objects.filter(name='Kohli').update(topic_name='Cricket')
    t=Topic.objects.get_or_create(topic_name="Skating")[0]
    Webpage.objects.update_or_create(name='raina',defaults={'topic_name':t,'url':'http://raina.com'})
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})



def web_form(request):
    if request.method=="POST":
        #print(request.POST)
        topic=request.POST['topic']


        webpages=Webpage.objects.filter(topic_name=topic)
        return render(request,'display_webpage.html',context={'webpages':webpages})

    return render(request,'web_form.html')


def create_topic(request):
    if request.method=='POST':
        topic=request.POST.get('topic')
        Topic.objects.get_or_create(topic_name=topic)[0]
        topics=Topic.objects.all()
        return render(request,'display_topic.html',context={'topics':topics})

    return render(request,'create_topic.html')


def create_webpage(request):
    topics=Topic.objects.all()
    if request.method=="POST":
        top=request.POST['top']
        name=request.POST['name']
        url=request.POST['url']

        t=Topic.objects.get_or_create(topic_name=top)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()

        webpages=Webpage.objects.all()
        return render(request,'display_webpage.html',context={'webpages':webpages})
        
    return render(request,'create_webpage.html',context={'topics':topics})



















