# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import os

SECRET_KEY = "Please do not spew DeprecationWarnings"

# Haystack settings for running tests.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'haystack_tests.db',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'haystack',
    'tests.core',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ]
        },
    },
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'tests.core.urls'

HAYSTACK_ROUTERS = ['haystack.routers.DefaultRouter']

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack_elasticsearch.elasticsearch.ElasticsearchSearchEngine',
        'URL': os.environ.get('TEST_ELASTICSEARCH_1_URL', 'http://localhost:9200/'),
        'INDEX_NAME': 'test_default',
        'INCLUDE_SPELLING': True,
    },
}

if os.getenv('VERSION_ES') == ">=2.0.0,<3.0.0":
    HAYSTACK_CONNECTIONS['default'] = {
        'ENGINE': 'haystack_elasticsearch.elasticsearch2.Elasticsearch2SearchEngine',
        'URL': '127.0.0.1:9200/',
        'INDEX_NAME': 'test_default',
        'INCLUDE_SPELLING': True,
    }
elif os.getenv('VERSION_ES') == ">=5.0.0,<6.0.0":
    HAYSTACK_CONNECTIONS['default'] = {
        'ENGINE': 'haystack_elasticsearch.elasticsearch5.Elasticsearch5SearchEngine',
        'URL': '127.0.0.1:9200/',
        'INDEX_NAME': 'test_default',
        'INCLUDE_SPELLING': True,
    }
