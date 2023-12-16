from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'atc_site//index.html')

def erea(request):
    return render(request, 'atc_site//erea.html')

@require_POST
#@handle_newsletter
def handle_newsletter(request):
    return JsonResponse({'success': True, 'error': None}, status=200)

@require_POST
#@handle_contact_request
def handle_contact_request():
    return JsonResponse({'success': True, 'error': None}, status=200)