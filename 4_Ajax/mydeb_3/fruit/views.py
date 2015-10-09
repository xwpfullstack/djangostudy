# coding=utf-8
from django.shortcuts import render
from fruit.models import *
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


#csrf_exempt关闭csrf验证
@csrf_exempt
def index(request):
    plist = Person.objects.all()
    context_dict = {'context': plist}
    return render(request, 'fruit/index.html', context_dict)


@csrf_exempt
def add_indent(request, personid):
    try:
        user = Person.objects.get(id=personid)
    except Person.DoesNotExist:
        user = None
    ucase = Case.objects.all()
    context_dict = {'ucase': ucase, 'username': user}
    return render(request, 'fruit/add_indent.html', context_dict)


@csrf_exempt
def choice_goods(request):
    param = request.GET.get('a')
    if param != 404:
        data1 = serializers.serialize("json", Goods.objects.filter(case=param))
    else:
        data1 = {}
    return HttpResponse(data1)


@csrf_exempt
def goods_submit(request):
    if request.method == "POST" and request.is_ajax():
        userid = request.POST['userid']
        goods = request.POST['qgoods']
        count = request.POST['qcount']
        price = request.POST['qprice']
        goodsid = Goods.objects.get(name=goods)
        person = Person.objects.get(id=userid)
        goods = Goods.objects.get(id=goodsid.id)
        Indent.objects.create(person=person, goods=goods,
                              count=int(count), price=int(price))
    return HttpResponse("successful")
