# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import ast
import os
try:
    from urllib.parse import urlparse, urlunparse
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
    from urlparse import urlparse, urlunparse
# Load more settings from a file called local_settings.py if it exists
try:
    from my_geonode.local_settings import *
#    from geonode.local_settings import *
except ImportError:
    from geonode.settings import *

#
# General Django development settings
#
PROJECT_NAME = 'my_geonode'
MY_SITE_URL = 'https://makerghat.urbansciences.in/'
# add trailing slash to site url. geoserver url will be relative to this
if not SITEURL.endswith('/'):
    SITEURL = '{}/'.format(SITEURL)

SITENAME = os.getenv("SITENAME", 'my_geonode')
DEBUG = True
# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', "en")

INSTALLED_APPS += (
                    'melghat_app.apps.MelghatAppConfig',
                    'wagtail.contrib.forms',
                    'wagtail.contrib.redirects',
                    'wagtail.embeds',
                    'wagtail.sites',
                    'wagtail.users',
                    'wagtail.snippets',
                    'wagtail.documents',
                    'wagtail.images',
                    'wagtail.search',
                    'wagtail.admin',
                    'wagtail.core',

                    'modelcluster',
                    )
if PROJECT_NAME not in INSTALLED_APPS:
    INSTALLED_APPS += (PROJECT_NAME,'dashboard','school_gis', 'fgis_map.apps.FgisMapConfig','fgis_cms.apps.FgisCmsConfig',)

MIDDLEWARE += (
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

WAGTAIL_SITE_NAME = 'makerghat.urbansciences.in'
# Location of url mappings
ROOT_URLCONF = os.getenv('ROOT_URLCONF', '{}.urls'.format(PROJECT_NAME))

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

TEMPLATES[0]['DIRS'].insert(0, os.path.join(LOCAL_ROOT, "templates"))
loaders = TEMPLATES[0]['OPTIONS'].get('loaders') or ['django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader']
# loaders.insert(0, 'apptemplates.Loader')
TEMPLATES[0]['OPTIONS']['loaders'] = loaders
TEMPLATES[0].pop('APP_DIRS', None)
DATABASE_ROUTERS = ['my_geonode.router.DatastoreRouter']