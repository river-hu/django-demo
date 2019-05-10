from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
import json
# Create your views here.
def index(request):
    return HttpResponse('hello,pages,index')

def addBlog(request):
    name = request.POST['name']
    tag = request.POST['tag']
    b = Blog(name=name,tagline=tag)
    b.save()
    result = {'code':'1','data':b.id,'msg':'添加成功'}
    return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
