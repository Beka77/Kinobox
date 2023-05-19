from django.urls import path
from apps.settings.views import (
    index,
    about_us,
    news_detail,
    contact,
    no_settings,
    error,
    thank_you,
    user_not_found,
    register_error,
    events,
)
from apps.movies.views import movie_detail
from apps.timetable.views import index_timetable


urlpatterns = [
    path("", index, name="index"),
    path("movie/<int:id>", movie_detail, name="movie_detail"),
    path("timetable/<str:date_slug>", index_timetable, name="index_timetable"),
    path("about_us/", about_us, name="about_us"),
    path("news/<int:id>", news_detail, name="news_detail"),
    path("contact/", contact, name="contact"),
    path("no_settings/", no_settings, name="no_settings"),
    path("thank_you/", thank_you, name="thank_you"),
    path("user_not_found/", user_not_found, name="user_not_found"),
    path("register_error/", register_error, name="register_error"),
    path("error/", error, name="error"),
    path("events/", events, name="events"),
]
