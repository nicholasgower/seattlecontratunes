from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ..models import Song, Medley, Report, SetList, SetListEntry
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.http import FileResponse
from django.db import connection
from ..forms import SongForm, SongEditForm, ReportForm 
from django.conf import settings
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User


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

class SongListViewPart(generic.ListView):
    template_name = "song_directory/list_view_fragment.html"
    
    context_object_name = "Song_list"
    title="Song"
    def get_queryset(self):
        
        if "page" not in self.kwargs.keys():    
            page=0
        else:
            page=self.kwargs['page']-1
        print(self.kwargs)
        quantity=5 #number of entries to load per segment
        
        return Song.objects.filter()[(quantity*page):(quantity*(page+1))]
    def get_context_data(self, **kwargs):
       context = super(SongListViewPart, self).get_context_data(**kwargs) # get the default context data
       #context['Title'] = "Song List"# add extra field to the context
       if "page" not in self.kwargs.keys():    
           context['page']=1 
       else:
           context['page']=self.kwargs['page']
       return context
        
def SongListViewFragment(request,model=Song):
    template_name = "song_directory/list_view_fragment.html"
    context={}
    if 'page' in request.GET:
        page=int(request.GET['page'])
    else:
        page=1
    #print(page)
    quantity=100 #number of entries to load per segment
    
    context["Song_list"]= model.objects.filter()[(quantity*(page-1)):(quantity*(page))]
    context["page"]=page
    context["next_page"]=page+1
    #print(context)
    if len(context["Song_list"])>0:
        return render(request,template_name,context)
    else:
        return HttpResponseRedirect("song_directory:index")
def ForeverScrollView(request,model,model_name,quantity=100):
    template_name = "song_directory/list_view_fragment.html"
    context={}
    if 'page' in request.GET:
        page=int(request.GET['page'])
    else:
        page=1
    #print(page)
    
    #Get entries 0-5 of list, or 6-10, or 11-15, etc.
    context[model_name]= model.objects.filter()[(quantity*(page-1)):(quantity*(page))]
    #context["uploader_name"]=context[model_name].user
    #Add current page and next page to context
    context["page"]=page
    context["next_page"]=page+1
    #print(context)
    return render(request,template_name,context)

def SongListForeverScroll(request):
    view=ForeverScrollView(request,Song,"Song_list",quantity=100)
    return view
    
def MedleyListForeverScroll(request):
    return ForeverScrollView(request,Medley,"Medley_list",quantity=100)
    
   
class SongSearchView(generic.ListView):
    template_name = "song_directory/list_view.html"
    
    context_object_name = "Song_search"
    title="Song_search"
    def get_search(self):
        return self.request.GET.get("search")
    def get_user_search(self):
        return self.request.GET.get("user")
    def get_queryset(self):
        search=self.get_search() #Get URL parameter
        if search !="":
            user_search=self.get_user_search()
            #print(search)
            out=Song.objects
            if search:
                out=out.filter(name__icontains=str(search))#[:100]
            if user_search:
                out=out.filter(uploader=User.objects.get(username=str(user_search)))
                
            
            #out=Song.objects.all()
            #print(out)
            #print(connection.queries)
            return out
        else:
            pass
    def get_context_data(self, **kwargs):
        context = super(SongSearchView, self).get_context_data(**kwargs) # get the default context data
       
        search=self.get_search()

        

       
       #tunes=Song.objects.
       
        context['Title'] = 'Search results for "{}"'.format(search)# add extra field to the context
        context["search"] = search
        return context   
