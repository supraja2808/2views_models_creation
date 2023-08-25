from django.shortcuts import render


# Create your views here.
from app.models import *

def Topic_display(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}

    return render(request,'Topic_display.html',d)
    

def Webpage_display(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}

    return render(request,'Webpage_display.html',d)
    

def AccessRecord_display(request):
    QSARO=AccessRecord.objects.all()
    d={'QSARO':QSARO}

    return render(request,'AccessRecord_display.html',d)


def Insert_Topic(request):
    tn=input('enter topic_name :')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}

    return render(request,'Topic_display.html',d)

def Insert_Webpage(request):
    tn=input('enter topic_name :')
    TO=Topic.objects.get(topic_name=tn)
    n=input('enter name :')
    u=input('enter url :')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}

    return render(request,'Webpage_display.html',d)
    


def Insert_AR(request):
    pk=input('enter pk :')
    WO=Webpage.objects.get(pk=pk)
    d=input('enter date :')
    a=input('enter author :')
    e=input('enter email :')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a,email=e)[0]
    AO.save()
    QSARO=AccessRecord.objects.all()
    d={'QSARO':QSARO}

    return render(request,'AccessRecord_display.html',d)































    




