"""
Django settings for mvp_landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from.email_info import *

# for gmail or google apps
EMAIL_USE_TLS       = EMAIL_USE_TLS
EMAIL_HOST          = EMAIL_HOST
EMAIL_HOST_USER     = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT          = EMAIL_PORT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = '/home/jva/mvp_landing/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oyacsv&sl5ml-lu^ll30pmh!0np1%&w#y4b7obir(wt_@-$^$f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'signups',    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mvp_landing.urls'

WSGI_APPLICATION = 'mvp_landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Template location

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static', 'templates'),
)

if DEBUG:    
    MEDIA_URL         = '/media/'
    STATIC_ROOT       = os.path.join(os.path.dirname(BASE_DIR), 'static', 'static-only')
    #'/home/jva/mvp_landing/static/static-only/'
    MEDIA_ROOT        = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media')
    #'/home/jva/mvp_landing/static/media/'
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), 'static', 'static'),
    )

    