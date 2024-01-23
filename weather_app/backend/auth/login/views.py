from django.contrib.auth import authenticate, login
from ....models import CustomUserManager
from ...main import login_page, index

def login(request, error=None):
    if request.method == 'POST':
        user = CustomUserManager().authenticate(email=request.POST['email'], password=request.POST['password']) 
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return index(request)
        return login_page(request, error='Invalid Login')
    return login_page(request)