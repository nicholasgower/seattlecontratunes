
#% url 'song_directory:medley_id' medley.id %


from . import views
from django.urls import path, include
import uuid
from functools import partial
md5_song_directory=uuid.UUID("dac9630aec642a428cd73f4be0a03569")

aboutText="Test"


app_name = "song_directory"
urlpatterns = [
    
    path("", views.Index, name="index"),
    path("medley/", views.MedleyView.as_view(), name="medley"),
    path("medley/view/<slug:slug>", views.MedleyIndexView.as_view(), name="medley_view"),
    path("htmx/medley/view_more",views.MedleyListForeverScroll,name="medley_view_page"),
    path("tune/", views.SongListView.as_view(), name="song_list"),
    
    #path("song/",views.SongView.as_view(),name="song"),
    #path("song/<int:pk>",views.SongView.as_view(),name="song_view"),
    #path("song/<int:pk>/download/abc",views.getSongAbc,name="song_abc_download"),
    path("tune/view/<slug:slug>",views.SongView.as_view(),name="song_view"),
    path("htmx/tune/view_more",views.SongListForeverScroll,name="song_view_page"),
    path("tune/view/<slug:url_code>/download/abc",views.getSongAbc,name="song_abc_download"),
    path("tune/search",views.SongSearchView.as_view(),name="song_search"),
    path("tune/upload",views.ask_for_song,name="song_upload"),
    
    #path("song/<int:pk>/",views.getSongAbc,name="song_print"), #Currently unused
    #path("about/",partial(views.ViewText,text=aboutText),name="about"),
    path("about/",views.about_view,name="about"),
    
    path("report",views.ask_for_report,name="report_form"),
    
    path("htmx/user/@<slug:other_user>",views.UserDetails.as_view(),name="user_details_small_fragment"),
    path("user/<slug:other_user>",views.UserDetailsPage.as_view()),
    path("user/@<slug:other_user>",views.UserDetailsPage.as_view(),name="user_details"),
    
    path("iReal",views.iRealView,name="iReal_View"),
    
    path("htmx/report_fragment",views.report_fragment,name="report_form_fragment"),
    
    path("htmx/confirm_submission",views.confirm_submission,name="submit_clicked"),
    
    
]