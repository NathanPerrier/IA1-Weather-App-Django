from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def index(request):
    context = {'is_authenticated': request.user.is_authenticated}
    return render(request, 'landing.html', context)