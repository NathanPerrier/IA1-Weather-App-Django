from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from decouple import config

from .chatbot.bot.main import chat_completion_request
from .chatbot.bot.data import BotData

from .chatbot.models import Message

from .weatherIcon.main import GetWeatherIcon
from .location.main import GetLocation
from .locationImage.images import GetImagesFromLocation
from .weatherDescription.main import GetWeatherDescription

@csrf_protect
def index(request):
    # GetImagesFromLocation().downloadimages()  #! fix
    return render(request, 'landing.html', {'is_authenticated': request.user.is_authenticated, 'icon': GetWeatherIcon().get_weather_icon(), 'location': GetLocation().get_location(), 'weather_desc': GetWeatherDescription(GetLocation().get_location()).get_weather_description()})

def radar(request):
    return render(request, 'radar.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'location': GetLocation().get_location()}) #'google_maps_api_key': config("GOOGLE_MAPS_API_KEY")

def routes(request):
    return render(request, 'routes.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN')})

def search(request):
    return render(request, 'search.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'is_authenticated': request.user.is_authenticated})

@csrf_protect
def login_page(request, error=''):
    return render(request, 'login.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'error': error}) #'google_maps_api_key': config("GOOGLE_MAPS_API_KEY")

@csrf_protect
def register_page(request, error=''):
    return render(request, 'register.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'error': error}) #'google_maps_api_key': config("GOOGLE_MAPS_API_KEY")

@csrf_protect
def forgot_password_page(request, error=''):
    return render(request, 'forgot_password.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'error': error})