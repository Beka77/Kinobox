# Generated by Django 4.1 on 2022-09-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_castmovie_options_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок отзыва')),
                ('description', models.CharField(max_length=255, verbose_name='Описание отзыва')),
                ('image', models.ImageField(upload_to='reviewer_image/', verbose_name='Фотография клиента')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]