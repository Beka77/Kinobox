from django.contrib import admin
from apps.timetable.models import TimeTable, TimeTableMovie, Hall, TimeMovie

# Register your models here.
class TimeTableMovieAdmin(admin.TabularInline):
    model = TimeTableMovie
    extra = 1

class TimeMovieAdmin(admin.TabularInline):
    model = TimeMovie
    extra = 1

class TimeTableAdmin(admin.ModelAdmin):
    inlines = [TimeTableMovieAdmin]
    prepopulated_fields = {"date_slug" : ("date", )}
    list_display = ('date', 'date_slug')

class TimeTableMovieAdmin(admin.ModelAdmin):
    inlines = [TimeMovieAdmin]
    list_display = ('movie', 'date_movie', 'hall')

admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(TimeTableMovie, TimeTableMovieAdmin)
admin.site.register(Hall)
admin.site.register(TimeMovie)