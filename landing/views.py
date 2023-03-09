from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(req):
    return HttpResponse('<h1>Title</h1><div><p><a href="/news">News</a></p><p><a href="/register">person</a></p></div>')
