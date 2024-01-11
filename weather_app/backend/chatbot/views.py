from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .bot.main import Chatbot
from .models import Message

from .bot.__init__ import GPT_MODEL

try:
    Message.objects.all().delete()
    Message.objects.create(role='system', content='You Are a helpful weather assistant that has access to almost all weather data. you are to answer purely weather based questions. try include figures in your reposnse to justify yor reasoning', model=GPT_MODEL)
except: pass

@require_POST
@csrf_exempt
def chat(request):
    user_message = request.POST.get('message')
    previous_messages = Message.objects.all().order_by('timestamp')
    Message.objects.create(role='user', content=user_message, model=previous_messages.last().model)
    previous_messages = Message.objects.all().order_by('timestamp')
    
    # Format previous messages
    formatted_messages = [{'role': msg.role, 'content': msg.content} for msg in previous_messages]
    print('###############################################################################################')
    print('formatted_messages:', formatted_messages)
    print('###############################################################################################')

    bot_response = Chatbot(previous_messages.last().model).chat_completion_request(formatted_messages)
    Message.objects.create(role='assistant', content=bot_response, model=previous_messages.last().model)
    return JsonResponse({'message': bot_response})

@require_POST
@csrf_exempt
def change_model(request):
    Message.objects.create(role='system', content=f'You are now using the {request.POST.get("model")} model', model=request.POST.get('model'))
    return JsonResponse({'success': True})