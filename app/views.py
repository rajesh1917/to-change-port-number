from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Address(request):
    return HttpResponse('<h1> port number changed to 8000</h1>')

def address(request):
    return HttpResponse('<h1> port number changed to 8001</h1>')