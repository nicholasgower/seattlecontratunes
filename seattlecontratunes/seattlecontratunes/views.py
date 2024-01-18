from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.template import loader
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.conf import settings

from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

def index(request):

    #return HTTPResponse("Test")
    return redirect("song_directory:index")    


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request):
    file= (settings.BASE_DIR / "static" / "favicon.ico").open("rb")
    return FileResponse(file)