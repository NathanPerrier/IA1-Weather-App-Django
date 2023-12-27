from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .bot.main import chat_completion_request
from .model import Message

@csrf_exempt
def chat(request):
    user_message = request.POST.get('message')
    Message.objects.create(role='user', content=user_message)
    bot_response = chat_completion_request([{"role": "user", "content": user_message}])
    print('user_message:', user_message)
    return JsonResponse({'message': bot_response})