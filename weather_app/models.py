from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import string
import random

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def authenticate(self, email, password):
        user = self.get_by_email(email)
        if user is not None and user.check_password(password):
            return user
        return None
    
    def normalize_email(self, email):
        return email.lower()
    
    def generate_code(self, length=6):
        """Generate a random numerical reset code of the given length."""
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length)) 
    
    def send_code(self, name, lname, user_email):
        # Create user but don't save to database yet
        user = CustomUser.objects.create_user(email=user_email, first_name=name, last_name=lname, username=user_email)
        user.set_unusable_password()
        user.save()

        # Generate code
        code = self.generate_code()

        # Save code to user and save user to database
        user.code = code
        user.save()

        # Send email to the admin
        context = {
            'name': 'New User',
            'email': user_email,
            'subject': 'Your Registration Code',
            'message': f'Hi {name}, here is your registration code: {code}',
        }
        email_body = render_to_string('atc_site/email.html', context)

        email = EmailMessage(
            'RainCheck - Registration Code',
            email_body,
            settings.EMAIL_HOST_USER,
            [user_email]
        )
        email.content_subtype = 'html'
        email.fail_silently = False
        email.send()
    
    def get_by_email(self, email):
        try:
            return self.get(email=email)  #! issue so defualts to none
        except:
            return None

    def get_by_id(self, id):
        try:
            return self.get(id=id)
        except:
            return None
        
    
    
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254, blank=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.email


    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name="customuser_groups",
        related_query_name="customuser",
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name="customuser_user_permissions",
        related_query_name="customuser",
        help_text='Specific permissions for this user.',
    )