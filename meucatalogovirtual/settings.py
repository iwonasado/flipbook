# -*- coding: utf-8 -*-
import os
import sys
from django.utils.translation import ugettext_lazy as _
gettext = lambda s: s

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'app'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'scripts'))
DEBUG = True
TEMPLATE_DEBUG = True
# DATABASES = {'default':
#              {'ENGINE': 'django.db.backends.sqlite3',
#               'NAME': os.path.join(PROJECT_ROOT, 'database.sqlite')}
#              }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'flipbook',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'de3712',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

TIME_ZONE = 'Europe/Paris'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

SECRET_KEY = 'fgh1rzme%sfv3#n+fb7h948yuv3(pt63abhi12_t7e^^5q8dyw'

AUTH_PROFILE_MODULE = "account.UserProfile"

LOGIN_URL = '/login/'

USE_TZ = True
USE_I18N = True
USE_L10N = True

SITE_ID = 1

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext('English')),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'meucatalogovirtual.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'zinnia.context_processors.version',
    'sekizai.context_processors.sekizai',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'cms', #django CMS itself
    'mptt', #utilities for implementing a modified pre-order traversal tree
    'menus', #helper for model independent hierarchical website navigation
    'south', #intelligent schema and data migrations
    'sekizai', #for javascript and css management
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    # 'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
    'tinymce',
    'tagging',
    'zinnia',
    'cmsplugin_zinnia',
    'account',
    'cmsplugin_contact',
    'cmsplugin_text_wrapper',
    'flipbook',
    'form_designer',
    'form_designer.contrib.cms_plugins.form_designer_form',
)

CMS_TEMPLATES = (
    ('white_template.html', 'Template Branco - Blog'),
	('gray_template.html', 'Template Cinza - Basico'),
    ('under_construction.html','Template Under Construction'),
)

CMS_TEXT_WRAPPERS = (
    ('Size 1523', {
        'render_template': 'wrappers/size1523.html',
    }),
    ('Size 1523 - 1000', {
        'render_template': 'wrappers/size1523_1000.html',
    }),
    ('Size 1523 - 1000 - 600', {
        'render_template': 'wrappers/size1523_1000_600.html',
    }),
    ('DIV', {
        'render_template': 'wrappers/div.html',
    }),
)
CMS_TEXT_WRAPPER_CLASSES = ('box1','accordion','grayboxlist',
                            'blueboxlist','yellowboxlist','m-grid',
                            'm-grid--divide-2','m-grid--divide-3','m-grid--divide-4',
                            'styleboxtop','styleboxcontent','styleboxbottom',
                            'gray-bg','white-bg','orange-display')

CMS_SEO_FIELDS = True

#ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'

ZINNIA_PAGINATION = 6

ZINNIA_ENTRY_CONTENT_TEMPLATES = [
	('zinnia/flipbook_entry_detail_small.html','Template Customizado - Lista')
]

ZINNIA_ENTRY_DETAIL_TEMPLATES = [
	('zinnia/flipbook_entry_detail_full.html','Template Customizado - Post')
]

CMSPLUGIN_ZINNIA_TEMPLATES = [
	('zinnia/flipbook_entry_detail_small.html','Template Customizado - Lista')
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

DEFAULT_FROM_EMAIL = "contato@webmail.com"

CMSPLUGIN_CONTACT_FORMS = (
    ('cmsplugin_contact.forms.ContactForm', _('default')),
    ('meucatalogovirtual.forms.ContactForm', _('Customizado')),
)

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,lists",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

DEFAULT_FROM_EMAIL = "noreply@meucatalogovirtual.com"
EMAIL_HOST = 'smtp.meucatalogovirtual.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "meucatalogovirtual@meucatalogovirtual.com"
EMAIL_HOST_PASSWORD = "z8g2y3p3"
EMAIL_USE_TLS = True