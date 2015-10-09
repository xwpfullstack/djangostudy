from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def add(request):
    print request.GET['a']
    print request.GET['b']
    if request.is_ajax():
        a = request.GET['a']
        b = request.GET['b']
        c = int(a) + int(b)
        r = HttpResponse(str(c))
    return r
