
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
    path("medley/<slug:slug>", views.MedleyIndexView.as_view(), name="medley_view"),
    path("song/", views.SongListView.as_view(), name="song_list"),
    #path("song/",views.SongView.as_view(),name="song"),
    #path("song/<int:pk>",views.SongView.as_view(),name="song_view"),
    #path("song/<int:pk>/download/abc",views.getSongAbc,name="song_abc_download"),
    path("song/view/<slug:slug>",views.SongView.as_view(),name="song_view"),
    path("song/view/<slug:url_code>/download/abc",views.getSongAbc,name="song_abc_download"),
    path("song/search",views.SongSearchView.as_view(),name="song_search"),
    #path("song/<int:pk>/",views.getSongAbc,name="song_print"), #Currently unused
    path("about/",partial(views.ViewText,text=aboutText),name="about"),
    path("song/upload",views.ask_for_song,name="song_upload"),
]