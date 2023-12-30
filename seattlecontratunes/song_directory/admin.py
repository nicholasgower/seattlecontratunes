from django.contrib import admin

# Register your models here.

from .models import Song, Medley, Report


for item in [Song, Medley,Report]:
    
    admin.site.register(item)
