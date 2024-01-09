# from django.urls import reverse_lazy
# from two_factor.urls import urlpatterns as tf_urls
# from django_otp.admin import OTPAdminSite
# from two_factor.views import LoginView
# import django_two_factor_auth
from pathlib import Path
import socket
import os

env_path = '.env'

try:
    from decouple import config, Csv
    SECRET_KEY = config("SECRET_KEY")
except:
    from dotenv import load_dotenv, set_key
    # Create the .env file if it doesn't exist
    if not os.path.exists(env_path):
        with open(env_path, 'w'):
            pass

    # Load the .env file
    load_dotenv(dotenv_path=env_path)

    # Set environment variables
    set_key(env_path, "SECRET_KEY", "django-insecure-_@8c=m2aimoga43jzw#h3w4%t)4+s(@guy1&s_v08h_)yjl-o1")
    set_key(env_path, "CELERY_BROKER_URL", "redis://:A45H2sg23hd2hdjhAG211hkyJKJ89@localhost:6379/0")
    set_key(env_path, "CELERY_RESULT_BACKEND", "redis://:A45H2sg23hd2hdjhAG211hkyJKJ89@localhost:6379/0")
    set_key(env_path, "REDIS_HOST", "redis")
    set_key(env_path, "REDIS_BAKCEND", "redis://192.68.55:6379")
    set_key(env_path, "OPENAI_API_KEY", "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")
    set_key(env_path, "TOMORROWIO_API_KEY", "AuOjEmIx61jlSiJayrYoMV5TEQ9uA3OK")
    set_key(env_path, "MAPBOX_ACCESS_TOKEN", "pk.eyJ1IjoibmF0aGFuLXBlcnJpZXIyMyIsImEiOiJjbG8ybW9pYnowOTRiMnZsZWZ6NHFhb2diIn0.NDD8iEfYO1t9kg6q_vkVzQ")
    set_key(env_path, "OPENEATHERMAP_API_KEY", "2d5323a42384860f12456db107631a5a")
    set_key(env_path, "EMAIL_HOST_USER", "contact.webgenieai@gmail.com")
    set_key(env_path, "EMAIL_HOST_PASSWORD", "tlwzdvpfotedwjdi")
    set_key(env_path, "DJANGO_SETTINGS_MODULE", "weather_app.settings")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

#** SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

PORT = '8000'

#** SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [socket.gethostbyname(socket.gethostname()), '127.0.0.1', 'localhost', 'host.docker.internal', 'ouguiya-wooden.runblade.host', '192.168.68.67', '192.168.0.178', '192.168.68.64']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    # "axes",
    
    "weather_app.backend.chatbot",
        
    "weather_app",
    
    "django_browser_reload",
    # Local apps
    
    "weather_app.backend.atc_site",
    
    "weather_app.unitTests",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django_otp.middleware.OTPMiddleware',  # Required for django_two_factor_auth
    "allauth.account.middleware.AccountMiddleware",
    # "axes.middleware.AxesMiddleware",
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    # 'axes.backends.AxesBackend',
    # 'axes.backends.AxesStandaloneBackend',  
)

ROOT_URLCONF = "weather_app.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'weather_app/frontend/templates/')],
        'APP_DIRS': True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',  # Required for allauth
                'django.contrib.auth.context_processors.auth',  # Required for django_two_factor_auth
            ],
        },
    },
]

print("BASE_DIR:", BASE_DIR)
print("TEMPLATES DIR:", os.path.join(BASE_DIR, 'weather_app/frontend/templates/'))

WSGI_APPLICATION = "weather_app.wsgi.application"
ASGI_APPLICATION = 'weather_app.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "HOST": "localhost",
        "PORT": PORT,
    }
}

# Add the following to your AUTHENTICATION_BACKENDS setting
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

APPEND_SLASH=False

SITE_ID = 1

# celery
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("REDIS_BACKEND")

# Redis Cache
# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": config("REDIS_BACKEND"),
    },
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Django Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [config("REDIS_BACKEND")],
        },
    },
}

# Chatterbot
CHATTERBOT = {
    "name": "User Support Bot",
    "logic_adapters": [
        "chatterbot.logic.BestMatch",
    ],
}

#Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'weather_app/frontend/static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

print("STATIC_ROOT:", STATIC_ROOT)