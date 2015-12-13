"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = (
    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
)
