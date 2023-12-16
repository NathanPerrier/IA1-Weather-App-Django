import os
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.conf import settings


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'landing.html')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # Render the login form.
        return render(request, 'login.html')
    
    
def stream_video(request, video_path):
    video_path = os.path.join(settings.BASE_DIR, 'weather_app\\frontend\\static\\videos', video_path)
    def play_video(video_path):
        with open(video_path, 'rb') as video:
            for chunk in iter(lambda: video.read(4096), b""):
                yield chunk

    response = StreamingHttpResponse(play_video(video_path))
    response['Content-Type'] = 'video/mp4'
    return response