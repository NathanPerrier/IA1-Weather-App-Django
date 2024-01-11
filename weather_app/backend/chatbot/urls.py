from django.urls import path
from .views import chat, change_model

urlpatterns = [
    path("chat/", chat, name="chat"),
    path("chat/change_model/", change_model, name="change_model")
]