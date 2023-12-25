from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .chatbot.bot.main import chat_completion_request
from .chatbot.bot.data import BotData

def index(request):
    BotData().get_user_ip(request)
    context = {'is_authenticated': request.user.is_authenticated}
    BotData().get_daily_weather_forecast(request.session)
    # print('prompt 1:', chat_completion_request([{"role": "user", "content": "How are you?"}]))
    # print(chat_completion_request([{"role": "user", "content": "What's the weather like in San Francisco?"}]))
    return render(request, 'landing.html', context)