import string
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

svr_username="wangxq"
svr_password="123456"
userid = "8888"
data=""
@csrf_exempt
def index(request):
      if request.method == 'POST':          
            #return HttpResponse(request.POST)
            for key, value in request.POST.items():
                global data
                if not data:
                    data += key + "=" + value
                else:
                    data += "&" + key + "=" + value
      data += "\r\n"
      return HttpResponse(data)

authdata=""
@csrf_exempt
def auth(request):
      res={}
      if request.method == 'POST':
            req_username = request.POST['username']
            req_password = request.POST['password']
            print(req_username)
            print(req_password)
            if req_username == svr_username and req_password == svr_password:
               res = {"isSuccess":"1","code":"200","msg":"认证成功","resp":{"userid":"8888"}}
            else:
                res = {"isSuccess":"0","code":"500","msg":"认证失败","resp":{}}
      return JsonResponse(res,safe=False)
      
@csrf_exempt
def heartbeat(request,userid):
      res={}
      if request.method == 'PUT':
            if( "8888" == userid ):
                  res = {"isSuccess":"1","code":"200","msg":"成功","resp":{"userid":"8888"}}
            else:
                res = {"isSuccess":"0","code":"500","msg":"失败","resp":{}}
      return JsonResponse(res,safe=False)

      
