from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Song, Medley
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.


class MedleyView(generic.ListView):
    template_name = "song_directory/medley.html"
    context_object_name = "Medley_list"
    
    def get_queryset(self):
        """Return 100 randomly chosen medlies"""
        return Medley.objects.filter()[:100]
    
def Index(request):
    #return redirect("medley/")
    return render(request,"song_directory/index.html")


        
class MedleyIndexView(generic.DetailView):
    model=Medley
    template_name = "song_directory/medley_view.html"
    context_object_name = "medley"
    
    def get_queryset(self):
        """Return five randomly chosen medlies"""
        return Medley.objects.filter() #.order_by("-id")[:5]
    
#def     