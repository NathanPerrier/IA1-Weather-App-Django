from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .chatbot.bot.main import chat_completion_request
from .chatbot.bot.data import BotData

def index(request):
    BotData().get_user_ip(request)
    context = {'is_authenticated': request.user.is_authenticated}
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
    
    print('--------------------------------------------------------------------------------------------------------------------')
    print('prompt: What is current weather like in Chuwar?')
    print('--------------------------------------------------------------------------------------------------------------------')
    print('AI:', chat_completion_request([{"role": "user", "content": "What is current weather like in Chuwar?"}]))
    print('--------------------------------------------------------------------------------------------------------------------')
    
    print('--------------------------------------------------------------------------------------------------------------------')
    print('prompt: What is the current air quality like in Anstead, what is the main pollutant?')
    print('--------------------------------------------------------------------------------------------------------------------')
    print('AI:', chat_completion_request([{"role": "user", "content": "What is air quality like in Anstead, what is the main pollutant?"}]))
    print('--------------------------------------------------------------------------------------------------------------------')
    # print(chat_completion_request([{"role": "user", "content": "What's the expected rainfall like in Brisbane, AUS over the next few days?"}]))
    return render(request, 'landing.html', context)