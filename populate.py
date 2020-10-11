# we need to create a Django environment

import os

#os.environ.setdefault('DJANGO_SETTINGS_MODULE','PROJECT_NAME.settings)

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project17.settings')

# accessing features of django

import django

django.setup()

# actual poplation process will be started

from app.models import *

import random

from faker import Faker

f1=Faker()

topics=['Skating','Swimming','Dieting','Cooking']


def Add_Topics():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]#Cooking
    t.save()
    return t


def Add_Webpages(webpagename,url):
    topic=Add_Topics()#cooking
    w=Webpage.objects.get_or_create(topic_name=topic,name=webpagename,url=url)[0]
    w.save()# one webpage has been created
    return w

def Add_AccessRecords(webpagename,url,date):
    name=Add_Webpages(webpagename,url)#webpage
    a=Access_Records.objects.get_or_create(name=name,date=date)[0]
    a.save()
    

def Add_data(n):
    for i in range(n):
        webpagename=f1.first_name()
        url=f1.url()
        date=f1.date()

        Add_AccessRecords(webpagename,url,date)




if __name__=='__main__':
    n=int(input('enter number of rows to be inserted'))
    print('population has been started')
    Add_data(n)
    print('population has been Done successfully')














