from django.contrib.auth import login as loginRequest
from ....models import CustomUserManager
from ...main import login_page, index

def loginView(request, error=None):
    if request.method == 'POST':
        user = CustomUserManager().authenticate(email=request.POST['email'], password=request.POST['password']) 
        if user is not None:
            loginRequest(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return index(request)
        return login_page(request, error='Invalid Login')
    return login_page(request)