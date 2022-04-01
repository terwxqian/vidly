import string
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

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
      if request.method == 'POST':
            for key, value in request.POST.items():
                global authdata
                if not authdata:
                    authdata += key + "=" + value
                else:
                    authdata += "&" + key + "=" + value
      authdata += "\r\n"
      return HttpResponse(authdata)
      
@csrf_exempt
def heartbeat(request,userid):
      if request.method == 'PUT':
        return HttpResponse(userid)

      
