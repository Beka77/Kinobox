from django.contrib import admin
from apps.movies.models import Movie, MovieImage, CastMovie, MovieReviews

# Register your models here.
class MovieImageAdmin(admin.TabularInline):
    model = MovieImage
    extra = 3 

class CastMovie(admin.TabularInline):
    model = CastMovie
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieImageAdmin, CastMovie]
    

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieReviews)