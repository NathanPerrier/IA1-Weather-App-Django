import os
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from django.conf import settings
from .chatbot.bot.data import BotData
from django.core.cache import cache
from .main import *
from ..models import CustomUser, CustomUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import logout
from django.shortcuts import redirect

# def get_user_ip(request):
#     ip, is_routable = get_client_ip(request)
#     if ip is not None:
#         BotData.objects.create(ip_address=ip)
#     else: pass

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUserManager().authenticate(email=email, password=password) #! always returns none ???
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # Redirect to a success page.
            return index(request)
        else:
            # Return an 'invalid login' error message.
            return login_page(request, error='Invalid Login')
    else:
        # Render the login form.
        return login_page(request)
    

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        if password == request.POST['password2']:
            if CustomUser.objects.filter(email=email).exists() == False:
                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
                # Specify the backend and log the user in
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return index(request)
            return register_page(request, error='Email already in use')
        return register_page(request, error='Passwords do not match')
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
    