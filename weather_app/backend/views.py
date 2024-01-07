import os
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from django.conf import settings
from .chatbot.bot.data import BotData
from django.core.cache import cache
from .main import *
from ..models import CustomUser, CustomUserManager
from .auth.register.models import RegisterAuth
from django.contrib.auth import logout


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
    
def register_get_email_view(request, error=''):
    if request.method == 'POST':
        success, error = RegisterAuth.create_and_send_reset_code(request.POST['first_name'], request.POST['last_name'], request.POST['email'])
        return JsonResponse({'success': success, 'error': error})
    return register_page(request)

def register_get_code_view(request):    
    if request.method == 'POST':
        print(request.POST['email'], request.POST['code'])
        success, error = RegisterAuth.check_code_entry(request.POST['email'], request.POST['code'])
        return JsonResponse({'success': success, 'error': error})
    return register_page(request)

def register_set_password_view(request):
    if request.method == 'POST':
        user = CustomUser.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        print(user)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return index(request)
    return register_page(request)    

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

def get_user_location(request):
    if request.method == 'POST':
        print(request.POST['latitude'], request.POST['longitude'])
        cache.set('latitude', request.POST['latitude'])
        cache.set('longitude', request.POST['longitude'])
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    