import imp
from django.urls import URLPattern

from django.urls import path
from . import views

# api/auth
# api/heartbeat/[userid]

app_name = 'authsys'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/auth', views.auth, name='auth'),
    path('api/heartbeat/<userid>', views.heartbeat, name='heatbeat'),
    #url(r'^/api/auth/$', views.MyView.as_view(), name='my-view'),
]