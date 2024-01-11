from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .bot.main import Chatbot
from .models import Message

Message.objects.all().delete()
Message.objects.create(role='system', content='You Are a helpful weather assistant that has access to almost all weather data. you are to answer purely weather based questions. try include figures in your reposnse to justify yor reasoning')

@require_POST
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
    
    bot_response = Chatbot().chat_completion_request(formatted_messages)
    Message.objects.create(role='assistant', content=bot_response)
    return JsonResponse({'message': bot_response})

@require_POST
@csrf_exempt
def get_model(request):
    model = request.POST.get('model')
    Chatbot(model_type=model)
    Message.objects.create(role='system', content=f'You are now using the {model} model')
    return JsonResponse({'success': True})