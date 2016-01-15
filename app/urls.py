"""
App urls definition
"""

from django.conf.urls import url

from .views import IndexView, AboutView, ContactView, ListActsView, VoteActView, SettingsView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^acts/$', ListActsView.as_view(), name='acts'),
    url(r'^acts/(?P<act_id>\d+)/vote/$', VoteActView.as_view(undo=False), name='act_vote'),
    url(r'^acts/(?P<act_id>\d+)/vote/undo$', VoteActView.as_view(undo=True), name='act_unvote'),

    url(r'^settings/$', SettingsView.as_view(), name='settings'),

    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
]
