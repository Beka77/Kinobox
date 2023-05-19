from django.shortcuts import render
from apps.movies.models import Movie
from apps.settings.models import Settings, Advert

# Create your views here.
def movie_detail(request, id):
    movie = Movie.objects.get(id = id)
    setting = Settings.objects.latest('id')
    adverts = Advert.objects.all().order_by("?")[:1]
    context = {
        'movie' : movie,
        'setting' : setting,
        'adverts' : adverts,
    }
    return render(request, 'movie-details-2.html', context)