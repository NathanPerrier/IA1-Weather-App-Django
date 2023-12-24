from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .chatbot.bot.main import chat_completion_request

def index(request):
    context = {'is_authenticated': request.user.is_authenticated}
    print(chat_completion_request("Hello"))
    print(chat_completion_request("What is the weather like today?"))
    return render(request, 'landing.html', context)