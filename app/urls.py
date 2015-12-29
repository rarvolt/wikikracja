"""
App urls definition
"""

from django.conf.urls import url

from .views import IndexView, AboutView, ContactView, ListActsView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^acts/$', ListActsView.as_view(), name='acts'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
]
