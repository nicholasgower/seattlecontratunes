
#% url 'song_directory:medley_id' medley.id %


from . import views
from django.urls import path, include


app_name = "song_directory"
urlpatterns = [
    path("", views.Index, name="medley_redirect"),
    path("medley/", views.MedleyView.as_view(), name="medley"),
    path("medley/<int:pk>", views.MedleyIndexView.as_view(), name="medley_view"),
    #path("song/",views.SongView.as_view(),name="song"),
    #path("song/<int:pk>",views.SongView.as_view(),name="song"),
]