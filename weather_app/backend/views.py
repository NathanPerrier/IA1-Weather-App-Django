import os
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from django.conf import settings
from .chatbot.bot.data import BotData
from django.core.cache import cache
from decouple import config
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
import json

from .main import *
from ..models import CustomUser, CustomUserManager
from .auth.views import *
from .weather.main import RetrieveWeather


def login_view(request):
    if request.method == 'POST':
        user = CustomUserManager().authenticate(email=request.POST['email'], password=request.POST['password']) 
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return index(request)
        return login_page(request, error='Invalid Login')
    return login_page(request)
    

def register_view(request):
    return register_page(request)
    
def forgot_password_view(request):
    return forgot_password_page(request)

def logout_view(request):
    logout(request)
    return index(request)
    
def stream_video(request, video_path):
    video_path = os.path.join(settings.BASE_DIR, 'weather_app/frontend/static/videos', video_path)
    def play_video(video_path):
        with open(video_path, 'rb') as video:
            for chunk in iter(lambda: video.read(4096), b""):
                yield chunk

    response = StreamingHttpResponse(play_video(video_path))
    response['Content-Type'] = 'video/mp4'
    return response

def search_location(request, location):
    try:
        # if location['status'] == 'OK':
            print('location:', location)
            location=location.split(' ')[0]
            print('location:', location)
            model = RetrieveWeather(location)
            location = model.request.location()
            print('location:', location)
            locationDict = {'city': location['name'], 'timezone': location['timezone'], 'country': location['timezone'].split('/')[0], 'lat': location['latitude'], 'lon': location['longitude']}
            if location is not None:
                return render(request, 'landing.html', {'is_authenticated': request.user.is_authenticated, 'location': locationDict, 'image': GenerateLocationImage(city=location['name'], region=location['state'], country=location['timezone'].split('/')[0], lat=location['latitude'], lon=location['longitude']).get_image(), 'forecast_daily': model.Forecast(model.request).get_daily(), 'forecast_hourly': model.Forecast(model.request).get_hourly(), 'mapbox_access_token': config('MAPBOX_ACCESS_TOKEN'), 'tomorrowio_api_key': config("TOMORROWIO_API_KEY"), 'hervey_bay': (lambda model: model.Forecast(model.request).get_hourly())(RetrieveWeather('4655')), 'perth': (lambda model: model.Forecast(model.request).get_hourly())(RetrieveWeather('6000')), 'sydney': (lambda model: model.Forecast(model.request).get_hourly())(RetrieveWeather('2000')), 'gold_coast': (lambda model: model.Forecast(model.request).get_hourly())(RetrieveWeather('4217')), 'melbourne': (lambda model: model.Forecast(model.request).get_hourly())(RetrieveWeather('3000')), 'warning': model.Warnings(model.request).get_warnings()})
            return search(request, error='Invalid Location')
        # return search(request, error='Invalid Location')
    except Exception as e:
        print('error:', e)
        return search(request, error='Invalid Location')


    
@require_POST
def get_user_location(request):
    if request.method == 'POST':
        print(request.POST['latitude'], request.POST['longitude'])
        cache.set('latitude', request.POST['latitude'])
        cache.set('longitude', request.POST['longitude'])
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

