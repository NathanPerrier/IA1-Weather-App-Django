from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from decouple import config

from .chatbot.bot.main import chat_completion_request
from .chatbot.bot.data import BotData

# from .chatbot.models import Message

def index(request):
    BotData().get_user_ip(request)
    context = {'is_authenticated': request.user.is_authenticated}
    # Message.objects.all().delete()
    # Message.objects.create(role='system', content='You Are a helpful weather assistant that has access to almost all weather data. you are to answer purely weather based questions. try include figures in your reposnse to justify yor reasoning')
    return render(request, 'landing.html', context)

def radar(request):
    return render(request, 'radar.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN')}) #'google_maps_api_key': config("GOOGLE_MAPS_API_KEY")