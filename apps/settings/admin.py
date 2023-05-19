from django.contrib import admin
from apps.settings.models import Settings, Advert, CinemaNews, AboutUs, Contact

# Register your models here.
admin.site.register(Settings)
admin.site.register(Advert)
admin.site.register(CinemaNews)
admin.site.register(AboutUs)
admin.site.register(Contact)