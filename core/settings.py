# import os
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# # SECRET_KEY = 'django-insecure-#a1b2c3d4e5f6g7h8i9j0k-lmnopqrstuvwxyz12345678'
# # DEBUG = True
# # ALLOWED_HOSTS = []

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'marketplace',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'core.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'core.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# AUTH_USER_MODEL = 'marketplace.User'

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = 'static/'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # import os
# # from pathlib import Path

# # BASE_DIR = Path(__file__).resolve().parent.parent

# # Change this to a strong random string - keep it secret!
# SECRET_KEY = 'asd123ASD_'

# # # IMPORTANT: Set DEBUG to False for production
# # DEBUG = False

# # Add your PythonAnywhere domain to ALLOWED_HOSTS
# ALLOWED_HOSTS = ['cybergate.pythonanywhere.com', 'www.cybergate.pythonanywhere.com']

# # # ... (keep the rest of INSTALLED_APPS, MIDDLEWARE, etc. as before)

# # # Update the database to use MySQL (PythonAnywhere provides MySQL)
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.mysql',
# #         'NAME': 'cybergate$default',  # PythonAnywhere database naming convention
# #         'USER': 'cybergate',
# #         'PASSWORD': 'asd123ASD_',
# #         'HOST': 'cybergate.mysql.pythonanywhere-services.com',
# #         'PORT': '3306',
# #     }
# # }

# # Static files configuration
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Media files configuration
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # Security settings for production
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = False  # PythonAnywhere handles SSL differently


# # import os
# # from pathlib import Path

# # BASE_DIR = Path(__file__).resolve().parent.parent

# # Change this to a strong random string - keep it secret!
# SECRET_KEY = 'asd123ASD_'

# # IMPORTANT: Set DEBUG to False for production
# DEBUG = False

# # Add your PythonAnywhere domain to ALLOWED_HOSTS
# ALLOWED_HOSTS = ['cybergate.pythonanywhere.com', 'localhost', '127.0.0.1']

# # Keep the rest of INSTALLED_APPS, MIDDLEWARE, etc. as before

# # Use SQLite database (free and works perfectly on PythonAnywhere)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # Static files configuration
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Media files configuration
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # Security settings for production
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True


import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-change-this-to-a-random-string-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add your PythonAnywhere domain here
ALLOWED_HOSTS = ['cybergate.pythonanywhere.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'marketplace',               # <-- This line must be present
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database – using SQLite for the free PythonAnywhere plan
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Custom user model
AUTH_USER_MODEL = 'marketplace.User'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (user uploaded images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = False   # PythonAnywhere already handles HTTPS