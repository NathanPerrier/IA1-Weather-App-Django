import os
from django.http import StreamingHttpResponse
from django.conf import settings

def stream_video_atc_site(request, video_path):
    video_path = os.path.join(settings.BASE_DIR, 'weather_app\\frontend\\static\\atc_site\\videos', video_path)
    def play_video(video_path):
        with open(video_path, 'rb') as video:
            for chunk in iter(lambda: video.read(4096), b""):
                yield chunk

    response = StreamingHttpResponse(play_video(video_path))
    response['Content-Type'] = 'video/mp4'
    return response