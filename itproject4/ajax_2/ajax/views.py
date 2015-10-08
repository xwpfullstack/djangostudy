from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return render(request, 'index.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))


def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')


def ajax_dict(request):
    name_dict = {'saywhat': 'I love python and Django', 'school': 'Itcastcpp'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')
