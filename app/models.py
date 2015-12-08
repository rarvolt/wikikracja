"""
Definition of models.
"""

from django.db import models


class Act(models.Model):
    act_title = models.CharField(max_length=200)
    act_link = models.CharField(max_length=200)


class PreChoice(models.Model):
    act = models.ForeignKey(Act)
    text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)


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
