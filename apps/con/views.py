from django.shortcuts import render,HttpResponse,render_to_response,RequestContext,get_object_or_404
from django.core.urlresolvers import reverse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from models import Dinar, Item
from serializers import DinarSerializer,ItemSerializer
from datetime import datetime as dt
from django.utils import timezone,dateparse
from django.conf import settings
from django.utils.timezone import activate
from django.views.decorators.csrf import csrf_exempt
activate(settings.TIME_ZONE)
import dateutil.parser

# Create your views here.
def Index(request):
    return render(request,"con/index.html")

def Detail(request,id):
    pk=int(id)
    return render(request,"con/detail.html",{"id":pk})


@csrf_exempt
def AddDin(request):
    added =False
    message=[]
    errors =[]
    if request.method == "POST":
        post = json.loads(request.body.decode('utf-8'))
        print(post)
        lname=post["listname"]
        azan = post["enddate"]
        if not lname:
            errors.append({"message":"enter a name"})
        if not azan:
            errors.append({"message":"enter a valid date"})
        if not errors:
            lfim=timezone.make_aware(dateparse.parse_datetime(azan+" 00:00:00"), timezone.get_current_timezone())
            din= Dinar.objects.create(name=lname,fim=lfim)
            din.save()
            added=True
            message.append({"message":"Your list have been created"})
            print(lfim)
        else:
            message.append({"message":"Error when creating a list"})
    print(message)
    resp = {"added":added,"message":message,"errors":errors}
    return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))

@csrf_exempt
def AddItem(request,pk):
    print(pk)
    message=[]
    errors =[]
    added = False
    item = Item(dinar=Dinar.objects.get(pk=int(pk)))
    if request.method =="POST":
        post = json.loads(request.body.decode('utf-8'))
        print(post)
        pname   = post["itemName"]
        pnombre = post["itemNumb"]
        pprice  = post["itemPrice"]
        pisExcep = post["isExept"]
        
        if not pname:
            errors.append({"message":"enter a product name"})
        if not pnombre:
            errors.append({"message":"enter a number of buyed product "})
        if not pprice:
            errors.append({"message":"enter a product price"})
        if not errors:
            item.name = pname
            item.price = float(pprice)
            item.nombre = int(pnombre)
            item.isException = bool(pisExcep)
            item.save()
            added = True
            message.append({"message":"item saved"})
    resp = {"added":added,"message":message,"errors":errors}
    return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))


@api_view(['GET','POST'])
def dinar_list(request, format=None):
    """list all Dinar """
    if request.method=='GET':
        dinares = Dinar.objects.all()
        serializer = DinarSerializer(dinares, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def dinar_detail(request, pk, format=None):
    """retrieve dinar details with itens"""

    try:
        dinar = Dinar.objects.get(pk=pk)
    except Dinar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DinarSerializer(dinar)
        return Response(serializer.data)


class DinarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dinar.objects.all()
    serializer_class = DinarSerializer

"""
class PeriodViewSet(viewsets.ModelViewSet):

    #API endpoint that allows groups to be viewed or edited.

    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
"""
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def DinarList(request):
    din = Dinar.objects.all()
    dina = []
    valid = timezone.now()
    fal = lambda dat,dta:dat>dta
    for d in din:

        dina.append({"pk":str(d.pk),"name":d.name,"inicial":d.inicial.strftime('%d-%m-%y'),"fim":d.fim.strftime('%d-%m-%y'),"isActive":fal(d.fim,valid),"nItem":str(d.item_set.all().count()),"total":str(sum([a.price*a.nombre for a in d.item_set.all()]))})
    
    data = json.dumps(dina)
    return HttpResponse(status=200, content_type='application/json',content=data)



def DinarItem(request):
    din = Dinar.objects.all()
    dina = []
    valid = timezone.now()
    fal = lambda dat,dta:dat>dta
    for d in din:
        dina.append({"pk":d.pk,"name":d.name,"inicial":d.inicial.strftime('%d-%m-%y'),"fim":d.fim.strftime('%d-%m-%y'),"isActive":fal(d.fim,valid),"nItem":d.item_set.all().count(),"total":str(sum([a.price for a in d.item_set.all()])),"itens":[{"pk":ite.pk,"name":ite.name,"price":str(ite.price),"isExcept":ite.isException} for ite in d.item_set.all()]})
    #print(dina)
    data = json.dumps(dina)
    return HttpResponse(data)

def DinDetail(request,id):
    pk =int(id)
    din = Dinar.objects.get(pk=pk)
    dinIt = din.item_set.all()
    dinItem=[]
    #"date"ite.date.strftime('%d-%m-%y'),"time":ite.add_time.strptime('%H:%M:%S'),
    for ite in dinIt:
        dinItem.append({"pk":ite.pk,"name":ite.name,"price":str(ite.price),"nbr":str(ite.nombre),"isExcept":ite.isException,"date":ite.date.strftime('%d-%m-%y'),"time":ite.date.strftime('%H:%M:%S'),"total":str(ite.price*ite.nombre)})
    data = json.dumps(dinItem)
    return HttpResponse(data)

def DinExcept(request,id):
    pk =int(id)
    din = Dinar.objects.get(pk=pk)
    dinIt = din.item_set.all()
    dinItem=[]
    #"date"ite.date.strftime('%d-%m-%y'),"time":ite.add_time.strptime('%H:%M:%S'),
    for ite in dinIt:
        if ite.isException:
            dinItem.append({"pk":ite.pk,"name":ite.name,"price":str(ite.price),"nbr":str(ite.nombre),"isExcept":ite.isException,"date":ite.date.strftime('%d-%m-%y'),"time":ite.date.strftime('%H:%M:%S'),"total":str(ite.price*ite.nombre)})
    data = json.dumps(dinItem)
    return HttpResponse(data)

@csrf_exempt
def DeleteList(request,id):
    pk =int(id)
    if request.method=="DELETE":
        get_object_or_404(Dinar, pk=pk).delete()
    return HttpResponse({"done":"done"})

@csrf_exempt
def DeleteItem(request,id):
    pk =int(id)
    if request.method=="DELETE":
        get_object_or_404(Item, pk=pk).delete()
    return HttpResponse({"done":"done"})

