"""
Definition of views.
"""

from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, View, UpdateView

from .mixins import LoginRequiredMixin
from .models import Act, Votes, Settings


class IndexView(TemplateView):
    """Renders the home page."""
    template_name = 'app/index.html'


class AboutView(TemplateView):
    """Renders the about page."""
    template_name = 'app/about.html'


class ContactView(TemplateView):
    """Renders the contact page."""
    template_name = 'app/contact.html'


class ListActsView(ListView):
    model = Act
    context_object_name = 'acts'
    paginate_by = 10  # Settings.objects.all()[0].act_count_page


class VoteActView(LoginRequiredMixin, View):
    """User voted"""
    undo = False

    def get(self, request, *args, **kwargs):
        act = get_object_or_404(Act, act_id=kwargs['act_id'])
        if self.undo:
            act.users.remove(request.user)
        else:
            act.users.add(request.user)

        if act.count >= 20:  # Settings.objects.get(pk=1).act_threshold
            now = datetime.now()
            duration = timedelta(days=20)  # Settings.objects.get(pk=1).vote_duration
            vote = Votes(act=act,
                         vote_start=now,
                         vote_end=now + duration)
            vote.save()

        return HttpResponseRedirect(reverse('acts'))


class SettingsView(UpdateView):
    model = Settings
    fields = ['act_count_threshold', 'act_count_page']
    template_name_suffix = '_update'
    success_url = '/settings/'

    def get_object(self, queryset=None):
        return Settings.objects.all()[0]
