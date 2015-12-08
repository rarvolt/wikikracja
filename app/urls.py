"""
App urls definition
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# TODO: Change string view arguments to callables.

urlpatterns = patterns('',
                       url(r'^$', 'app.views.interested_act', name='interested_act'),
                       url(r'^contact$', 'app.views.vote_act', name='vote_act'),
                       url(r'^about', 'app.views.results', name='results'),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {
                               'template_name': 'app/login.html',
                               'authentication_form': BootstrapAuthenticationForm,
                               'extra_context':
                                   {
                                       'title': 'Log in',
                                       'year': datetime.now().year,
                                   }
                           }, name='login'
                           ),
                       url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
                       )
