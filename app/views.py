"""
Definition of views.
"""

from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext


# TODO: Change view functions to clases.


def interested_act(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/interested.html',
        context_instance=RequestContext(request,
        {
            'title': 'Which Act are you interested in?',
            'year': datetime.now().year,
        })
    )


def vote_act(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vote.html',
        context_instance=RequestContext(request,
        {
            'title': 'Vote the act',
            'year': datetime.now().year,
        })
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
            'app/about.html',
        context_instance=RequestContext(request,
        {
            'title': 'See how you have voted and how the envoys did.',
            'message': 'Votes.',
            'year': datetime.now().year,
        })
    )
