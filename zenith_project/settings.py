"""
ZENITH - Django Project Settings
=================================
This file contains all the configuration for our Django project.
Think of it as the control panel for the whole application.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# This is just for development - never share this in real production
SECRET_KEY = 'django-insecure-zenith-bca-project-2024-secret-key-change-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
# These are the apps Django will load when it starts
INSTALLED_APPS = [
    'django.contrib.admin',          # Django's built-in admin panel
    'django.contrib.auth',           # Handles user login/logout/register
    'django.contrib.contenttypes',   # Required by Django internally
    'django.contrib.sessions',       # Manages user sessions (keeps you logged in)
    'django.contrib.messages',       # Flash messages (success, error alerts)
    'django.contrib.staticfiles',    # Manages CSS, JS, image files
    'zenith',                        # Our main application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',         # CSRF protection - prevents form attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zenith_project.urls'

# Template configuration - tells Django where to find HTML files
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,   # Look for templates inside each app's 'templates' folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',       # Makes 'user' available in all templates
                'django.contrib.messages.context_processors.messages', # Makes messages available in all templates
            ],
        },
    },
]

WSGI_APPLICATION = 'zenith_project.wsgi.application'

# Database - we're using SQLite which is a simple file-based database
# Perfect for college projects - no installation needed!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Creates a file called db.sqlite3 in project root
    }
}

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'   # Set to Indian Standard Time
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Media files (user uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# After login, redirect here
LOGIN_REDIRECT_URL = '/dashboard/'
# After logout, redirect here
LOGOUT_REDIRECT_URL = '/login/'
# If a user tries to access a page without login, send them here
LOGIN_URL = '/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
