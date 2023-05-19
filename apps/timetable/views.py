from django.shortcuts import render
from apps.settings.models import Settings
from apps.timetable.models import TimeTable
from apps.settings.models import Advert

# Create your views here.
def index_timetable(request, date_slug):
    setting = Settings.objects.latest('id')
    time_table = TimeTable.objects.get(date_slug = date_slug)
    time_tables = TimeTable.objects.all()
    adverts = Advert.objects.all().order_by("?")[:1]
    context = {
        'setting' : setting,
        'time_table' : time_table,
        'time_tables' : time_tables,
        'adverts' : adverts,
    }
    return render(request, 'movie-ticket-plan.html', context)