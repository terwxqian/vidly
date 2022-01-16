import imp
from django.urls import URLPattern

from django.urls import path
from . import views

# movies/
# moves/1/detail

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
