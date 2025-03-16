"""
Django settings for laborers project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# from mongoengine import connect

# MONGODB_ATLAS_URI = "mongodb://payease-2025:UOmiJs8K72zFBEo9@payease-shard-00-00.cnbe3.mongodb.net:27017,payease-shard-00-01.cnbe3.mongodb.net:27017,payease-shard-00-02.cnbe3.mongodb.net:27017/payease?replicaSet=atlas-cluster-0&authSource=admin"
# # MONGODB_ATLAS_URI = "mongodb+srv://payease-2025:UOmiJs8K72zFBEo9@payease-shard-00-00.cnbe3.mongodb.net/payease?retryWrites=true&w=majority"


# # MONGODB_ATLAS_URI = "mongodb+srv://payease-2025:UOmiJs8K72zFBEo9@payease-shard-00-00.cnbe3.mongodb.net/"
# # MONGODB_ATLAS_URI = "mongodb+srv://payease-2025>:UOmiJs8K72zFBEo9@payease.cnbe3.mongodb.net/"



# connect(db="payease", host=MONGODB_ATLAS_URI)
import os


SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')




from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lomln!+z#pg&fybrrvpq+qw^9gfi0ktbh)g4rl9_mlm26m8_dt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payease']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'laborers.urls'
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  
],
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

WSGI_APPLICATION = 'laborers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

import pymysql 

pymysql.install_as_MySQLdb()

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', 
#         'NAME': BASE_DIR / "db.sqlite3", 
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',  # Change to your database name
        'USER': 'payease',  # Your MySQL username
        'PASSWORD': '1998Dagi#t',  # Your MySQL password
        'HOST': 'localhost',  # Use '127.0.0.1' if needed
        'PORT': '3307',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "static/"),

]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
