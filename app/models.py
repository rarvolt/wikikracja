"""
Definition of models.
"""

from django.db import models


class Act(models.Model):
    act_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


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
