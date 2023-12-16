from django.contrib import admin
from django.urls import include, path
from . import main
from .views import stream_video_atc_site

urlpatterns = [
    path("", main.index, name="atc_index"),
    path("erea", main.erea, name="erea"),
    path('stream_video/<str:video_path>/', stream_video_atc_site, name='stream_video_atc_site'),
]