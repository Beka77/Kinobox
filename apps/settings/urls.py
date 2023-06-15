from django.urls import path
from . import views
from apps.movies.views import movie_detail
from apps.timetable.views import index_timetable


urlpatterns = [
    path("", views.index, name="index"),
    path("movie/<int:id>", movie_detail, name="movie_detail"),
    path("timetable/<str:date_slug>", index_timetable, name="index_timetable"),
    path("about_us/", views.about_us, name="about_us"),
    path("news/<int:id>", views.news_detail, name="news_detail"),
    path("contact/", views.contact, name="contact"),
    path("no_settings/", views.no_settings, name="no_settings"),
    path("thank_you/", views.thank_you, name="thank_you"),
    path("user_not_found/", views.user_not_found, name="user_not_found"),
    path("register_error/", views.register_error, name="register_error"),
    path("error/", views.error, name="error"),
    path("events/", views.events, name="events"),
    path("event_speaker/", views.event_speaker, name="event_speaker"),
    path("event_ticket/", views.event_ticket, name="event_ticket"),
    path("event_checkout/", views.event_checkout, name="event_checkout"),
    path("app_download/", views.app_download, name="app_download"),
    path("calendar/", views.calendar, name="calendar"),
]
