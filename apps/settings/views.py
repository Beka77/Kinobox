from django.shortcuts import render, redirect
from apps.settings.models import Settings, CinemaNews, AboutUs, Contact
from apps.movies.models import Movie
from django.core.mail import send_mail


# Create your views here.
def index(request):
    try:
        setting = Settings.objects.latest("id")
    except:
        return redirect("no_settings")
    movies = Movie.objects.all()
    news = CinemaNews.objects.all().order_by("-created")
    context = {
        "setting": setting,
        "movies": movies,
        "news": news,
    }
    return render(request, "index-2.html", context)


def news_detail(request, id):
    setting = Settings.objects.latest("id")
    news = CinemaNews.objects.get(id=id)
    context = {
        "setting": setting,
        "news": news,
    }
    return render(request, "event-details.html", context)


def about_us(request):
    about = AboutUs.objects.latest("id")
    setting = Settings.objects.latest("id")
    context = {
        "about": about,
        "setting": setting,
    }
    return render(request, "about.html", context)


def contact(request):
    setting = Settings.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )
        send_mail(
            # title:
            f"{setting.title}",
            # message:
            f"{name} спасибо за ваше сообщение. В скором времени мы вам ответим. Ваше сообщение: {message}",
            # from:
            "noreply@somehost.local",
            # to:
            [email],
        )
        return redirect("thank_you")
    context = {
        "setting": setting,
    }
    return render(request, "contact.html", context)


def events(request):
    setting = Settings.objects.latest("id")
    context = {
        "setting": setting
    }
    return render(request, "events.html", context)

def event_speaker(request):
    setting = Settings.objects.latest("id")
    context = {
        "setting" : setting
    }
    return render(request, "event-speaker.html", context)

def event_ticket(request):
    setting = Settings.objects.latest("id")
    context = {
        "setting" : setting
    }
    return render(request, "event-ticket.html", context)

def event_checkout(request):
    setting = Settings.objects.latest("id")
    context = {
        "setting" : setting
    }
    return render(request, "event-checkout.html", context)

def error(request):
    return render(request, "404.html")


def no_settings(request):
    return render(request, "no_settings.html")


def user_not_found(request):
    return render(request, "user_not_found.html")


def thank_you(request):
    return render(request, "thank_you.html")


def register_error(request):
    return render(request, "register_error.html")
