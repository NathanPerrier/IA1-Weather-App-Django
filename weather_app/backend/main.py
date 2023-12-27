from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .chatbot.bot.main import chat_completion_request
from .chatbot.bot.data import BotData

from .chatbot.model import Message
def index(request):
    BotData().get_user_ip(request)
    context = {'is_authenticated': request.user.is_authenticated}
    Message.objects.all().delete()
    Message.objects.create(role='system', content='You Are a helpful weather assistant that has access to almost all weather data. you are to answer purely weather based questions. try include figures in your reposnse to justify yor reasoning')
    #print(BotData().get_daily_weather_forecast())
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('prompt: "what is the current weather like near me?')
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('AI:', chat_completion_request([{"role": "user", "content": "what is the current weather like near me?"}]))
    # print('--------------------------------------------------------------------------------------------------------------------')
    
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('prompt: "what is the snow expectansy like in canada over the next few days?')
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('AI:', chat_completion_request([{"role": "user", "content": "what is the snow expectansy like in canada over the next few days?"}]))
    # print('--------------------------------------------------------------------------------------------------------------------')
    
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('prompt: How safe is the air in Hong Kong?')
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('AI:', chat_completion_request([{"role": "user", "content": "How safe is the air in Hong Kong?"}]))
    # print('--------------------------------------------------------------------------------------------------------------------')
    
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('prompt: What is the fire risk of Darwin over the coming week?')
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('AI:', chat_completion_request([{"role": "user", "content": "What is the fire risk of Darwin over the coming week?"}]))
    # print('--------------------------------------------------------------------------------------------------------------------')
    
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('prompt: What time is sunset today in Chuwar?')
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('AI:', chat_completion_request([{"role": "user", "content": "What time is sunset today in Chuwar?"}]))
    # print('--------------------------------------------------------------------------------------------------------------------')
    
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('prompt: what is the weather like today?')
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('AI:', chat_completion_request([{"role": "user", "content": "what is the weather like today?"}]))
    # print('--------------------------------------------------------------------------------------------------------------------')
    
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('prompt: how has the weather been near me the past few days?')
    # print('--------------------------------------------------------------------------------------------------------------------')
    # print('AI:', chat_completion_request([{"role": "user", "content": "how has the weather been near me the past few days?"}]))
    # print('--------------------------------------------------------------------------------------------------------------------')
    
    # print(chat_completion_request([{"role": "user", "content": "What's the expected rainfall like in Brisbane, AUS over the next few days?"}]))
    return render(request, 'landing.html', context)