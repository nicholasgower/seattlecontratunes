from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import os
# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse("abctools:editor"))
def abctools(request):
    context={}
    
    with open(settings.BASE_DIR / "abctools" / "tune_templates" / "new_tune.abc",'r') as file:
        tune_autofill=file.read()
        user=str(request.user)
        context["tune_autofill"]=tune_autofill.format(user=user)
    print(context)
    return render(request,"abctools/abctools_contratunes.html",context=context)
def credits(request):
    return render(request,"abctools/credits.html")
def support(request):
    return render(request,"abctools/support.html")
def tipjars(request):
    return render(request,"abctools/tipjars.html")
def tunesources(request):
    return render(request,"abctools/tunesources.html")
def userguide(request):
    return render(request,"abctools/userguide.html")
