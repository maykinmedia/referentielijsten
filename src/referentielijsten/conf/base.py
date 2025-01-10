from django.urls import reverse_lazy

from import_export.formats.base_formats import DEFAULT_FORMATS
from notifications_api_common.settings import *  # noqa
from open_api_framework.conf.base import *  # noqa

from .api import *  # noqa

#
# Core Django settings
#

#
# APPLICATIONS enabled for this project
#
INSTALLED_APPS = INSTALLED_APPS + [
    "import_export",
    # Project applications.
    "referentielijsten.accounts",
    "referentielijsten.utils",
    "referentielijsten.api",
]
# open-api-framework currently installs `django.contrib.sites`, but we want to move
# away from this in the future
INSTALLED_APPS.remove("django.contrib.sites")

#
# SECURITY settings
#
CSRF_FAILURE_VIEW = "referentielijsten.accounts.views.csrf_failure"

#
# Custom settings
#
PROJECT_NAME = "Referentielijsten"

# This setting is used by the csrf_failure view (accounts app).
# You can specify any path that should match the request.path
# Note: the LOGIN_URL Django setting is not used because you could have
# multiple login urls defined.
LOGIN_URLS = [reverse_lazy("admin:login")]


# Default (connection timeout, read timeout) for the requests library (in seconds)
REQUESTS_DEFAULT_TIMEOUT = (10, 30)

##############################
#                            #
# 3RD PARTY LIBRARY SETTINGS #
#                            #
##############################

#
# Django-Admin-Index
#
ADMIN_INDEX_DISPLAY_DROP_DOWN_MENU_CONDITION_FUNCTION = (
    "referentielijsten.utils.django_two_factor_auth.should_display_dropdown_menu"
)

#
# MAYKIN-2FA
#
# It uses django-two-factor-auth under the hood so you can configure
# those settings too.
#
# we run the admin site monkeypatch instead.
# Relying Party name for WebAuthn (hardware tokens)
TWO_FACTOR_WEBAUTHN_RP_NAME = "referentielijsten"

#
# django-import-export
#
IMPORT_EXPORT_FORMATS = DEFAULT_FORMATS


#
# Django setup configuration
#
SETUP_CONFIGURATION_STEPS = (
    "mozilla_django_oidc_db.setup_configuration.steps.AdminOIDCConfigurationStep",
)
