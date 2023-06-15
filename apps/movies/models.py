from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from apps.categories.models import Category

# Create your models here.
class Movie(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Названия фильма"
    )
    description = models.TextField(
        verbose_name="Описание фильма"
    )
    release_date = models.DateField(
        verbose_name="Дата выхода фильма"
    )
    poster = models.ImageField(
        upload_to = "posters/",
        verbose_name="Постер для фильма"
    )
    duration = models.CharField(
        max_length=255, 
        verbose_name="Длительность фильма",
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Рейтинг фильма от пользователей"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="movie_category",
        verbose_name="Категории фильма"
    )
    trailer_url = models.URLField(
        verbose_name="Ссылка на трейлер"
    )
    time = models.CharField(
        verbose_name="Время",
        max_length=5,
    )
    hall = models.CharField(
        max_length=20,
        verbose_name="Зал",
    )
    price = models.CharField(
        max_length=10,
        verbose_name="Цена"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class MovieImage(models.Model):
    post = models.ForeignKey(
        Movie, 
        on_delete=models.CASCADE, 
        related_name="movie_post",
        verbose_name="Пост"
    )
    image = models.ImageField(
        upload_to = "movie_images/",
        verbose_name="Скриншоты к фильму"
    )

    def __str__(self):
        return f"{self.post.title}"

    class Meta:
        verbose_name = "Фотография к фильму"
        verbose_name_plural = "Фотографии к фильмам"

class CastMovie(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE, 
        related_name="movie_cast"
    )
    image = models.ImageField(
        upload_to = "cast_image/",
        verbose_name="Фотография"
    )
    first_name = models.CharField(
        max_length=100, 
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия"
    )
    person = models.CharField(
        max_length=100,
        verbose_name="Кем является"
    )
    movie_person = models.CharField(
        max_length=100,
        verbose_name="Роль"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class MovieReviews(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="review_movie",
        verbose_name="Фильм которому оставляется отзыв"
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name="Полное имя"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок отзыва"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание отзыва"
    )
    image = models.ImageField(
        upload_to = "reviewer_image/",
        verbose_name="Фотография клиента"
    )
    created = models.DateTimeField(
        auto_now_add = True,
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"