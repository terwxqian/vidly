from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.


def index(request):
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)
    movies = Movie.objects.all()

    return render(request, 'index.html', {'movies': movies})
