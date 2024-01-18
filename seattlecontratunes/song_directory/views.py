from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Song, Medley, Report, SetList, SetListEntry
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.http import FileResponse
from django.db import connection
from .forms import SongForm, ReportForm 
from django.conf import settings
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User

from pyRealParser import Tune as iRealTune
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
    
    #Add current page and next page to context
    context["page"]=page
    context["next_page"]=page+1
    #print(context)
    return render(request,template_name,context)
def SongListForeverScroll(request):
    return ForeverScrollView(request,Song,"Song_list",quantity=100)
    
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
       #print(context["object"].abc.replace("\n","\\n"))
       context["debug"]=False
       #print(context)
       
       #Using Windows-style line breaks will break escapejs filter.
       #So we must replace Windows line breaks("\r\n") with Unix line breaks("\n")
       context["object"].abc=context["object"].abc.replace("\r\n","\n")
       context["object"].uploader_name = User.objects.get(id=context["object"].uploader_id) # add extra field to the context
       
       
       
       return context
   
def iRealView(request):
    iReal=request.GET.get("iReal")
    """ Displays the contents of an iRealPro url."""
    tune=iRealTune.parse_ireal_url(iReal)[0]
    context={"tune":tune}
    template="song_directory/iReal_view.html"
    
    return render(request,template,context)
"""   
def displayUserInfo(request):
    user=request.GET("user")
    
    song_count=Song.objects.filter(uploader=user.id).count()
    SetList_count=SetList.objects.filter(uploader=user.id).count()
    
    context={"song_count":song_count,"user"SetList_count}
    return HttpResponse(str(context))      
"""
class UserDetails(generic.DetailView):
    template_name="song_directory/user_info_small.fragment.html"
    model=User
    slug_url_kwarg='other_user'
    slug_field="username"
    context_object_name="other_user"
    #song_count=Song.objects.filter(uploader=user.id).count()
    #SetList_count=SetList.objects.filter(uploader=user.id).count()
    
    def get_context_data(self, **kwargs):
       context = super(UserDetails, self).get_context_data(**kwargs) # get the default context data
       context["object"].song_count = Song.objects.filter(uploader=context["object"].pk).filter(availability="public").count()
       context["object"].medley_count = Medley.objects.filter(uploader=context["object"].pk).filter(availability="public").count()
       print(context["object"].song_count)
       print(context["object"])
       for field in context["object"]._meta.get_fields():
           print(field.name)
           
       #context["object"].uploader_name = User.objects.get(id=context["object"].uploader_id) # add extra field to the context
       #context={"song_count":song_count,"user":SetList_count}
       return context
class UserDetailsPage(UserDetails):
    template_name="song_directory/user_info.html"
    
def getSongAbc(request,url_code):
    
    song_object=get_object_or_404(Song, url_code=url_code)
    #print(song_object)
    filename="{}.abc".format(song_object.name)
    
    #Using Windows-style line breaks will break escapejs filter.
    #So we must replace Windows line breaks("\r\n") with Unix line breaks("\n")
    abc=song_object.abc.replace("\r\n","\n")
    response = HttpResponse(abc, content_type="text/plain")
    response["content-Disposition"]='attachment; filename={0}'.format(filename)
    return response

def ViewText(request,text):
    template="song_directory/generic_text_display.html"
    context={"text":text}
    response=render(request,template,context)
    return response

def about_view(request):
    return render(request,"song_directory/text_content/about.html")    

def ask_for_song(request):
    """Delievers Song Submission Form to user if they have the correct permission."""
    if request.user.is_authenticated or request.user.has_perm("song_directory.add_song"):
        if request.method == "POST":
            form =SongForm(request.POST)
            if form.is_valid():
                new_song=Song(name=form["name"].value(),abc=form["abc"].value(),description=form["description"].value(),uploader=request.user)
                new_song.save()
                print(form)
                
                return redirect("song_directory:song_view",slug=Song.objects.get(pk=new_song.pk).url_code)
        else:
            context={}
    
            with open(settings.BASE_DIR / "abctools" / "tune_templates" / "new_tune.abc",'r') as file:
                tune_autofill=file.read()
                user=str(request.user)
                context["tune_autofill"]=tune_autofill.format(user=user)
            
            context["form"]=SongForm()
        return render(request,"abctools/abctools_contratunes.html",context)
    else:
        return redirect("account_login")


def confirm_submission(request):
    return render(request,"song_directory/confirm_submission.html")

def report_fragment(request):
    return render(request,"song_directory/report_form_snippet.html")
        
def ask_for_report(request):
    """Delievers Report Submission Form to user."""
    if True:
        if request.method == "POST":
            form =ReportForm(request.POST)
            if form.is_valid():
                new_report=Report()
                
                    
                new_report.name=form["name"].value()
                new_report.url=form["url"].value()
                new_report.reason=form["reason"].value()
                new_report.elaboration=form["elaboration"].value()
                new_report.email=form["email"].value()
                new_report.uploader=request.user
                #new_song=Song(name=form["name"].value(),abc=form["abc"].value(),description=form["description"].value(),uploader=request.user)
                #new_song.save()
                new_report.save()
                print(form)
                
                return redirect("song_directory:index")
        else:
            form = ReportForm()
        return render(request,"song_directory/report_form.html",{"form":form})
    else:
        return redirect("account_login")

        
