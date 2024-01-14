from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from decouple import config
from datetime import datetime
import pytz


from .chatbot.bot.data import BotData

from .chatbot.models import Message

from .weatherIcon.main import GetWeatherIcon
from .location.main import GetLocation
from .weather.main import RetrieveWeather
from .locationImage.Dalle3.main import GenerateLocationImage
from .weatherDescription.main import GetWeatherDescription

@csrf_protect
def index(request):
    location = GetLocation().get_location()
    model = RetrieveWeather(location.zip)
    # GetImagesFromLocation().downloadimages()  #! fix
    return render(request, 'landing.html', {'is_authenticated': request.user.is_authenticated, 'location': location, 'image': GenerateLocationImage(location).get_image(), 'forecast_daily': model.Forecast(model.request).get_daily(), 'forecast_hourly': model.Forecast(model.request).get_hourly(), 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'tomorrowio_api_key': config("TOMORROWIO_API_KEY")})  #* removed 'icon': GetWeatherIcon().get_weather_icon(), 'weather_desc': GetWeatherDescription(GetLocation().get_location()).get_weather_description()

def radar(request):
    return render(request, 'radar.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'location': GetLocation().get_location(), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN')}) #'google_maps_api_key': config("GOOGLE_MAPS_API_KEY")

def routes(request):
    return render(request, 'routes.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'location': GetLocation().get_location(), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN')})

def search(request):
    return render(request, 'search.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'location': GetLocation().get_location(), 'is_authenticated': request.user.is_authenticated})

@csrf_protect
def login_page(request, error=''):
    return render(request, 'login.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'location': GetLocation().get_location(), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'error': error}) #'google_maps_api_key': config("GOOGLE_MAPS_API_KEY")

@csrf_protect
def register_page(request, error=''):
    return render(request, 'register.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'location': GetLocation().get_location(), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'error': error}) #'google_maps_api_key': config("GOOGLE_MAPS_API_KEY")

@csrf_protect
def forgot_password_page(request, error=''):
    return render(request, 'forgot_password.html', {'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'location': GetLocation().get_location(), 'is_authenticated': request.user.is_authenticated, 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'error': error})