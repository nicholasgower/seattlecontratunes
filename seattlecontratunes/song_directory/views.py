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
from django.db import connection

from django.contrib.auth.models import User
# Create your views here.


class MedleyView(generic.ListView):
    template_name = "song_directory/list_view.html"
    context_object_name = "Medley_list"
    
    def get_queryset(self):
        """Return 100 randomly chosen medlies"""
        return Medley.objects.filter()#[:100]
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
    
    slug_url_kwarg='slug'
    slug_field="url_code"
    
    def get_queryset(self):
        """Return five randomly chosen medlies"""
        return Medley.objects.filter() #.order_by("-id")[:5]
    def get_context_data(self, **kwargs):
       context = super(MedleyIndexView, self).get_context_data(**kwargs) # get the default context data
       context["tunes"]=[Medley.Tune1,Medley.Tune2,Medley.Tune3]
       print(context["tunes"])
       
       #context["Tune1_exists"]=len(Song.objects.filter(name__icontains=Song.objects.get(id=))
       context['Title'] = "Song List" # add extra field to the context
       return context
    
        
class SongListView(generic.ListView):
    template_name = "song_directory/list_view.html"
    
    context_object_name = "Song_list"
    title="Song"
    def get_queryset(self):
        """Return 100  medleys"""
        return Song.objects.filter()#[:100]
    def get_context_data(self, **kwargs):
       context = super(SongListView, self).get_context_data(**kwargs) # get the default context data
       context['Title'] = "Song List"# add extra field to the context
       return context
   
   
class SongSearchView(generic.ListView):
    template_name = "song_directory/list_view.html"
    
    context_object_name = "Song_search"
    title="Song_search"
    def get_search(self):
        return self.request.GET.get("search")
    def get_queryset(self):
        search=self.get_search() #Get URL parameter
        #print(search)
        if search:
            out=Song.objects.filter(name__icontains=str(search))#[:100]
        else:
            out = Song.objects.none()
        #out=Song.objects.all()
        #print(out)
        #print(connection.queries)
        return out
    def get_context_data(self, **kwargs):
       context = super(SongSearchView, self).get_context_data(**kwargs) # get the default context data
       
       search=self.get_search()
       
       #tunes=Song.objects.
       
       context['Title'] = 'Search results for "{}"'.format(search)# add extra field to the context
       context["search"] = search
       return context   



#def SongSearch(request):
#    search=request.GET.get("search")
#    template_name="song_directory/list_view.html"
#    
#    return render(request,template_name,context=)



class SongView(generic.DetailView):
    model=Song
    slug_url_kwarg='slug'
    slug_field="url_code"
    template_name = "song_directory/song_view.html"
    context_object_name = "song"
    
    def get_queryset(self):
        """Return five randomly chosen medlies"""
        return Song.objects.filter() #.order_by("-id")[:5]   
    def get_context_data(self, **kwargs):
       context = super(SongView, self).get_context_data(**kwargs) # get the default context data
       #print(context)
       context["object"].uploader_name = User.objects.get(id=context["object"].uploader_id) # add extra field to the context
       
       
       
       return context
       
    
   
def getSongAbc(request,url_code):
    
    song_object=get_object_or_404(Song, url_code=url_code)
    #print(song_object)
    filename="{}.abc".format(song_object.name)
    response = HttpResponse(song_object.abc, content_type="text/plain")
    response["content-Disposition"]='attachment; filename={0}'.format(filename)
    return response

def ViewText(request,text):
    template="song_directory/generic_text_display.html"
    context={"text":text}
    response=render(request,template,context)
    return response
    
    
