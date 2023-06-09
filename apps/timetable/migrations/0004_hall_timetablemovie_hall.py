# Generated by Django 4.1 on 2022-09-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_timetablemovie_date_movie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hall', models.CharField(max_length=255, verbose_name='Название зала')),
            ],
        ),
        migrations.AddField(
            model_name='timetablemovie',
            name='hall',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie_hall', to='timetable.hall'),
            preserve_default=False,
        ),
    ]
