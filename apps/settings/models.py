from tabnanny import verbose
from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to = "logo/"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на facebook аккаунт",
        blank = True, null = True,
    )
    twitter = models.URLField(
        verbose_name="Ссылка на twitter аккаунт",
        blank = True, null = True
    )
    pinterest = models.URLField(
        verbose_name="Ссылка на pinterest аккаунт",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на instagram аккаунт",
        blank = True, null = True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайтов"

class Advert(models.Model):
    image = models.ImageField(
        upload_to = "advert/",
        verbose_name="Фотография рекламы"
    )
    url_advert = models.URLField(
        verbose_name="Ссылка на рекламу"
    )

    def __str__(self):
        return f"{self.url_advert}"

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

class CinemaNews(models.Model):
    image = models.ImageField(
        upload_to = "news_images/",
        verbose_name="Фотография события"
    )
    title = models.CharField(
        max_length=255, 
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class AboutUs(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to = "about_us/"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        
        
        
class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя")
    email = models.EmailField(
        verbose_name="Почта"
    )
   
    message = models.CharField(
        max_length=255, 
        verbose_name="Сообщение"
    )
    
    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"