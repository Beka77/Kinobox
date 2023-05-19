# Generated by Django 4.1 on 2022-09-05 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_alter_timetablemovie_time_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetablemovie',
            name='date_movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='time_table_movie', to='timetable.timetable', verbose_name='Дата фильма'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetablemovie',
            name='time_movie',
            field=models.TimeField(verbose_name='Время фильма'),
        ),
    ]
