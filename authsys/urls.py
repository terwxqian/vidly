import imp
from django.urls import URLPattern

from django.urls import path
from . import views

# /api/auth
# /api/heartbeat/[userid]

app_name = 'authsys'

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^/api/auth/$', views.MyView.as_view(), name='my-view'),
]