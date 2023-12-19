from django.contrib import admin

# Register your models here.

from .models import Song, Medley


for item in [Song, Medley]:
    
    admin.site.register(item)
