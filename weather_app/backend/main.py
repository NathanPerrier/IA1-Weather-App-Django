from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .chatbot.bot.main import chat_completion_request
from .chatbot.bot.data import BotData

def index(request):
    BotData().get_user_ip(request)
    context = {'is_authenticated': request.user.is_authenticated}
    #print(BotData().get_daily_weather_forecast())
    print('--------------------------------------------------------------------------------------------------------------------')
    print('prompt 1:', chat_completion_request([{"role": "user", "content": "How are you?"}]))
    print('--------------------------------------------------------------------------------------------------------------------')
    print(chat_completion_request([{"role": "user", "content": "What's the expected rainfall like in Brisbane, AUS over the next few days?"}]))
    return render(request, 'landing.html', context)