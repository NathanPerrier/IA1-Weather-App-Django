from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .bot.main import chat_completion_request

@csrf_exempt
def chat(request):
    user_message = request.POST.get('message')
    print('user_message:', user_message)
    return JsonResponse({'message':chat_completion_request([{"role": "user", "content": user_message}])})