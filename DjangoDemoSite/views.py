from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string
from . import models
# Create your views here.

def demo_data(request):
    return HttpResponse("<h1>My Web site</h1>")
def mypage1(req):
    return HttpResponse("<h1>My Web site</h1>")


def index(request):
    return HttpResponse("""Hello, world. You're at the polls index.<p>
    
    <a href=works>Works</a><p>
    <a href=worksm>Works Model</a><p>
    <a href=api/data>API Demo</a><p>
    <a href=admin>Admin</a><p>
    """)


def works(request):
    title = 'Tinyapp'
    author = 'Vitor Freitas'
    html = render_to_string('works.html', {'title': title, 'author': author})
    return HttpResponse(html)

def workswithmodel(request):
    model = [models.WorkItem(),models.WorkItem(),models.WorkItem(),models.WorkItem()]
   # model.Title = "drink a beer"
    html = render_to_string('workswithmodel.html', {'model': model})
    return HttpResponse(html)

