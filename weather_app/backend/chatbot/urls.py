from django.urls import path
from .views import chat, change_model, get_directions, set_directions

urlpatterns = [
    path("chat/", chat, name="chat"),
    path("chat/change_model/", change_model, name="change_model"),
    path("chat/getCoordinates/", get_directions, name="get_directions"),
    path("chat/setRoute/", set_directions, name="set_directions")
]