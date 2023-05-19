# Generated by Django 4.1 on 2022-08-31 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Названия фильма')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('release_date', models.DateField(verbose_name='Дата выхода фильма')),
                ('poster', models.ImageField(upload_to='posters/', verbose_name='Постер для фильма')),
                ('duration', models.CharField(max_length=255, verbose_name='Длительность фильма')),
                ('rating', models.PositiveSmallIntegerField(verbose_name='Рейтинг фильма от пользователей')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_category', to='categories.category', verbose_name='Категории фильма')),
            ],
        ),
    ]
