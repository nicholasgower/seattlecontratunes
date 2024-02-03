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
import requests
from urllib.request import urlopen
from django.core.exceptions import ValidationError
from django.core.files import File
import os


from django.contrib.auth.models import User

from datetime import datetime



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
    #return render(request,"song_directory/index.html")
    return redirect("song_directory:song_list")


        
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
    
        



#def SongSearch(request):
#    search=request.GET.get("search")
#    template_name="song_directory/list_view.html"
#    
#    return render(request,template_name,context=)


    

#Displays song as sheet music, and provides users with tools to change the music's appearance.    
class SongView(generic.DetailView):
    model=Song
    slug_url_kwarg='slug'
    slug_field="url_code"
    template_name = "song_directory/song_view.html"
    context_object_name = "song"
    
     
    def get_context_data(self, **kwargs):
       context = super(SongView, self).get_context_data(**kwargs) # get the default context data
       #print(context["object"].abc.replace("\n","\\n"))
       context["debug"]=False
       
       
       #Using Windows-style line breaks will break escapejs filter.
       #So we must replace Windows line breaks("\r\n") with Unix line breaks("\n")
       context["object"].abc=context["object"].abc.replace("\r\n","\n")
       context["object"].uploader_name = User.objects.get(id=context["object"].uploader_id) # add extra field to the context
       context["user_uploaded_song"]= str(context["object"].uploader_name)==str(self.request.user)
       print(context["object"].uploader_name)
       print(str(self.request.user))
       print(context)
       return context

def viewExternalSong(request):
    url=request.GET.get("url")
    try:
        # Download the file from the given URL
        response = urlopen(url)
        file_content = response.read().decode('utf-8')

        # Check if the file content is of text type
        if not file_content.startswith(('')):
            raise ValidationError("Invalid file type. Only text files are allowed.")

        # Create a Django File object from the downloaded content
        #file_name = os.path.basename(url)
        #django_file = File(file_content, name=file_name)
    except Exception as e:
        # Handle exceptions accordingly
        return HttpResponse(f"Error: {str(e)}", status=400)
    


    return render(request,"song_directory/song_view.html",{"song_code":file_content,"external":True,"debug":"False","url":url})

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

def TextView(request,text):
    template="song_directory/generic_text_display.html"
    context={"text":text}
    response=render(request,template,context)
    return response


def license_view(request):
    import sys
    print(sys.path)
    with open("song_directory/constants/LICENSE.txt","r") as file:
        license_text=file.read()
    return TextView(request,license_text)

def about_view(request):
    return render(request,"song_directory/text_content/about.html")    

def ask_for_song(request):
    """Delievers Song Submission Form to user."""
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
    
def edit_song(request,url_code):
    """Delivers Song Submission Form to user to edit an existing song"""
    this_song=Song.objects.get(url_code=url_code)
    
    #print(this_song)
    if (request.user==this_song.uploader) and (request.user.is_authenticated or request.user.has_perm("song_directory.add_song")):
        if request.method == "POST":
            print(this_song)
            
            form =SongEditForm(request.POST)
            #print("form",form)
            if form.is_valid():
                this_song.abc=form["abc"].value()
                this_song.description=form["description"].value()
                this_song.availability=form["availability"].value()
                this_song.edited_time=datetime.now()
                this_song.save()
                
                return redirect("song_directory:song_view",slug=Song.objects.get(pk=this_song.pk).url_code)
            else:
                pass
        else:
            context={}
            context["edit_mode"]=True
            #context["tune_autofill"]=this_song.abc
            context["song"]=this_song
            context["tune_title"]=this_song.name
            
            
            context["form"]=SongEditForm()
            return render(request,"abctools/abctools_contratunes.html",context)
    else:
        response=render(request,"song_directory/errors/unauthorized.html")
        response.status_code=403 # 403 forbidden
        return response
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

