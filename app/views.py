"""
Definition of views.
"""

from django.views.generic import TemplateView, ListView

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
