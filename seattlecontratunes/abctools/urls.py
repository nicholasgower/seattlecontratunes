from django.contrib import admin
from django.urls import path, include
from . import views


app_name="abctools"

urlpatterns = [
    path("",views.index,name="index"),
    path("abctools",views.abctools,name="editor"),
    path("credits",views.credits,name="credits"),
    path("support",views.support,name="support"),
    path("tipjars",views.tipjars,name="tipjars"),
    path("tunesources",views.tunesources,name="tunesources"),
    path("userguide",views.userguide,name="userguide"),
]
    
