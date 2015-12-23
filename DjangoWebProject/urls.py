"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import url, include
from django.contrib import admin

from .registration_settings import REGISTRATION_HMAC

if REGISTRATION_HMAC:
    accounts_urls = 'registration.backends.hmac.urls'
else:
    accounts_urls = 'registration.backends.simple.urls'

urlpatterns = (
    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accounts_urls)),
)
