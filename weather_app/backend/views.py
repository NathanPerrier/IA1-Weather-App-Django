import os
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from django.conf import settings
from .chatbot.bot.data import BotData
from django.core.cache import cache
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout

from .main import *
from ..models import CustomUser, CustomUserManager
from .auth.views import *

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

@require_POST
def get_user_location(request):
    if request.method == 'POST':
        print(request.POST['latitude'], request.POST['longitude'])
        cache.set('latitude', request.POST['latitude'])
        cache.set('longitude', request.POST['longitude'])
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    