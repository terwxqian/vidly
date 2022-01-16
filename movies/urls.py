import imp
from django.urls import URLPattern


from django.urls import path
from . import views


# movies/
# moves/1/detail
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
