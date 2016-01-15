"""
Definition of models.
"""

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Act(models.Model):
    act_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='user')

    def __str__(self):
        return self.title

    @property
    def count(self):
        return self.users.all().count()


class Votes(models.Model):
    act = models.ForeignKey(Act)
    vote_start = models.DateTimeField()
    vote_end = models.DateTimeField()
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)

    def __str__(self):
        return self.act.title

    @property
    def vote_open(self):
        return datetime.now() >= self.vote_end


class Choice(models.Model):
    act = models.ForeignKey(Act)
    text = models.CharField(max_length=200)
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)


class EnvoyChoice(models.Model):
    act = models.ForeignKey(Act)
    text = models.CharField(max_length=200)
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)


class Settings(models.Model):
    act_count_threshold = models.PositiveIntegerField(default=0)
    act_count_page = models.PositiveIntegerField(default=0)
