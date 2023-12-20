from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Song, Medley
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.http import FileResponse

# Create your views here.


class MedleyView(generic.ListView):
    template_name = "song_directory/list_view.html"
    context_object_name = "Medley_list"
    
    def get_queryset(self):
        """Return 100 randomly chosen medlies"""
        return Medley.objects.filter()[:100]
    def get_context_data(self, **kwargs):
       context = super(MedleyView, self).get_context_data(**kwargs) # get the default context data
       context['Title'] = "Medley List"# add extra field to the contexts
       return context
    
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
    
class SongListView(generic.ListView):
    template_name = "song_directory/list_view.html"
    context_object_name = "Song_list"
    title="Song"
    def get_queryset(self):
        """Return 100 randomly chosen medlies"""
        return Song.objects.filter()[:100]
    def get_context_data(self, **kwargs):
       context = super(SongListView, self).get_context_data(**kwargs) # get the default context data
       context['Title'] = "Song List"# add extra field to the context
       return context
   
class SongView(generic.DetailView):
    model=Song
    template_name = "song_directory/song_view.html"
    context_object_name = "song"
    
    def get_queryset(self):
        """Return five randomly chosen medlies"""
        return Song.objects.filter() #.order_by("-id")[:5]   
    
def getSongAbc(request,pk):
    song_object=get_object_or_404(Song, pk=pk)
    #print(song_object)
    filename="{}.txt".format(song_object.name)
    response = HttpResponse(song_object.abc, content_type="text/plain")
    response["content-Disposition"]='attachment; filename={0}'.format(filename)
    return response
    
    
