"""
App urls definition
"""

from django.conf.urls import url
from django.views.generic import TemplateView

# TODO: Change string view arguments to callables.

urlpatterns = [
    url(r'^$', 'app.views.interested_act', name='index'),
    url(r'^contact/$', TemplateView.as_view(template_name="app/contact.html"), name='contact'),
    url(r'^about/$', TemplateView.as_view(template_name="app/about.html"), name='about'),
]
