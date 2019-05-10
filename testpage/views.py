from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):
    print(request.COOKIES['sad'])
    result = {"status": "错误", "data": request.POST['id'], "city": "北京"}
    response = HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    response.set_cookie('my_cookie', 'cookie value', max_age=1000)

    return response
def test(request):
    result = {"status":0,"data": request.POST['test'],'msg':'请求成功'}
    response = HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    response.set_cookie('my_cookie','cookieasd', max_age=1000)
    return response

