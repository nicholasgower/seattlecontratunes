
#% url 'song_directory:medley_id' medley.id %


from . import views
from django.urls import path, include
import uuid

md5_song_directory=uuid.UUID("dac9630aec642a428cd73f4be0a03569")




app_name = "song_directory"
urlpatterns = [
    path("", views.Index, name="main"),
    path("medley/", views.MedleyView.as_view(), name="medley"),
    path("medley/<int:pk>", views.MedleyIndexView.as_view(), name="medley_view"),
    path("song/", views.SongListView.as_view(), name="song_list"),
    #path("song/",views.SongView.as_view(),name="song"),
    path("song/<int:pk>",views.SongView.as_view(),name="song_view"),
    #path("song/<int:pk>/download/abc",views.getSongAbc,name="song_abc_download"),
]