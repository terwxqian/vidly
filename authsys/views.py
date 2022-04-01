import string
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

svr_username="wangxq"
svr_password="123456"
res="{}"
@csrf_exempt
def index(request):
      if request.method == 'POST':          
           req_username = request.POST['username']
           req_password = request.POST['password']
           if req_username ==  svr_password and req_password == svr_password:
               res = "{'isSuccess':'1','code':'200','msg':'认证成功'，'resp':{8888}}"
            
      return HttpResponse(res)

authdata=""
@csrf_exempt
def auth(request):
      if request.method == 'POST':
            req_username = request.POST['username']
            req_password = request.POST['password']
            if req_username ==  svr_password and req_password == svr_password:
               res = "{'isSuccess':'1','code':'200','msg':'认证成功'，'resp':{8888}}"
            
      return JsonResponse(res)
      
@csrf_exempt
def heartbeat(request,userid):
      if request.method == 'PUT':
        return HttpResponse(userid)

      
