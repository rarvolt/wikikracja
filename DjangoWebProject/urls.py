"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^', include('app.urls')),
                       )
