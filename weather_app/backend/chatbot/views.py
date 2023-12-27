from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .bot.main import chat_completion_request
from .model import Message

@csrf_exempt
def chat(request):
    user_message = request.POST.get('message')
    Message.objects.create(role='user', content=user_message)
    previous_messages = Message.objects.all().order_by('timestamp')
    
    # Format previous messages
    formatted_messages = [{'role': msg.role, 'content': msg.content} for msg in previous_messages]
    print('###############################################################################################')
    print('formatted_messages:', formatted_messages)
    print('###############################################################################################')
    bot_response = chat_completion_request(formatted_messages)
    Message.objects.create(role='assistant', content=bot_response)
    print('user_message:', user_message)
    return JsonResponse({'message': bot_response})