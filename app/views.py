from django.shortcuts import render


# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


def Topic_display(request):
    QSTO=Topic.objects.all()
    QSTO.objects.all().order_by('-topic_name')

    d={'QSTO':QSTO}


    return render(request,'Topic_display.html',d)
    

def Webpage_display(request):
    QSWO=Webpage.objects.filter(pk=3)
    QSWO=Webpage.objects.filter(topic_name='Cricket')
    QSWO=Webpage.objects.exclude(topic_name='Cricket')
    
    QSWO=Webpage.objects.all()[2:5:1]
    
    QSWO=Webpage.objects.all()[5:6:]
    
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
    QSWO=Webpage.objects.all().order_by(Length('name'))

    QSWO=Webpage.objects.all().order_by(Length('name').desc())




    #QSWO=Webpage.objects.all().order_by('topic_name') # ascending order
    #QSWO=Webpage.objects.all().order_by('name') # ascending order
    #QSWO=Webpage.objects.filter().order_by('-topic_name') # desending order
    #QSWO=Webpage.objects.all().order_by(Length('name').desc()) # length ascending order
  
    #QSWO=Webpage.objects.filter(name__startswith='s')

    #QSWO=Webpage.objects.all()
    #QSWO=Webpage.objects.filter(name__endswith='o')
    #QSWO=Webpage.objects.exclude(name__startswith='s')
    #QSWO=Webpage.objects.filter(url__endswith='com')
    #QSWO=Webpage.objects.filter(name__contains='s')
    #QSWO=Webpage.objects.filter(Q(topic_name='cricket') and Q(url__endswith='com'))
    #QSWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(url__endswith='com'))
    #QSWO=Webpage.objects.filter(Q(name__contains='r')&Q(url__endswith='com'))

    QSWO=Webpage.objects.filter(Q(topic_name='Cricket')|Q(name__contains='r'))


    
   

    d={'QSWO':QSWO}
    return render(request,'Webpage_display.html',d)
    

def AccessRecord_display(request):
                                     
    QSARO=AccessRecord.objects.all()
    QSARO=AccessRecord.objects.filter(date='2022-10-10')
    QSARO=AccessRecord.objects.filter(date__year='2023')
    QSARO=AccessRecord.objects.filter(date__day='24')
    QSARO=AccessRecord.objects.filter(date__month='8')
    QSARO=AccessRecord.objects.filter(date__gte='2022-10-10')
    QSARO=AccessRecord.objects.filter(date__lte='2001-01-01')
    QSARO=AccessRecord.objects.filter(author__in=('di','VK'))
    QSARO=AccessRecord.objects.filter(author__regex='s')
 








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































    




