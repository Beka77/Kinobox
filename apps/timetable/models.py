from tabnanny import verbose
from django.db import models
from apps.movies.models import Movie

# Create your models here.
class TimeTable(models.Model):
    date = models.DateField(
        verbose_name="Дата"
    )
    date_slug = models.SlugField(
        max_length=50,
        verbose_name="Slug для даты"
    )

    def __str__(self):
        return f"Дата фильма {self.date} slug {self.date_slug}"
    
    class Meta:
        verbose_name = "Дата фильма"
        verbose_name_plural = "Даты фильмов"

class Hall(models.Model):
    name_hall = models.CharField(
        max_length=255,
        verbose_name="Название зала"
    )

    def __str__(self):
        return self.name_hall

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

class TimeTableMovie(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movie_table",
        verbose_name="Фильм"
    )
    date_movie = models.ForeignKey(
        TimeTable,
        on_delete=models.CASCADE,
        related_name="time_table_movie", 
        verbose_name="Дата фильма"
    )

    hall = models.ForeignKey(
        Hall, 
        on_delete=models.CASCADE, 
        related_name="movie_hall"
    )

    def __str__(self):
        return f"{self.movie}"

    class Meta:
        verbose_name = "Расписание фильма"
        verbose_name_plural = "Расписание фильмов"

class TimeMovie(models.Model):
    movie = models.ForeignKey(
        TimeTableMovie,
        on_delete=models.CASCADE,
        related_name="time_table_movie"
    )
    time_movie = models.TimeField(
        verbose_name="Время фильма"
    )
    def __str__(self):
        return f"{self.time_movie}"

    class Meta:
        verbose_name = "Время фильма"
        verbose_name_plural = "Время фильмов"
