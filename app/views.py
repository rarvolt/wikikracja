"""
Definition of views.
"""

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, View

from .mixins import LoginRequiredMixin
from .models import Act


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


class VoteActView(LoginRequiredMixin, View):
    """User voted"""
    undo = False

    def get(self, request, *args, **kwargs):
        act = get_object_or_404(Act, act_id=kwargs['act_id'])
        if self.undo:
            act.users.remove(request.user)
        else:
            act.users.add(request.user)
        return HttpResponseRedirect(reverse('acts'))
