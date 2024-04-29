from django.urls import path
from project.constants import ROOT
from project.views import playlists

app_name = "playlists"

urlpatterns = [
    path(ROOT, playlists.index, name="index"),
    path("<int:id>/", playlists.view, name="view"),
    path("create/", playlists.create, name="create"),
    path("<int:id>/edit/", playlists.edit, name="edit"),
    path("<int:id>/manage/", playlists.manage, name="manage"),
]