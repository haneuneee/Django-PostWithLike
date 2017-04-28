# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Post(models.Model):
    created_by = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def _get_vote_sum(self):
        vote_sum = 0
        for vote in self.votes.all():
            # print('vote.up for '+str(self.pk)+' :'+str(vote.up))
            if vote.up:
                vote_sum = vote_sum + 1
            else:
                vote_sum = vote_sum - 1
        return vote_sum

    vote_sum = property(_get_vote_sum)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reddit:detail', kwargs={'pk': self.pk})


class Vote(models.Model):
    voted_by = models.ForeignKey(User, null=True)
    on_post = models.ForeignKey(Post, related_name='votes')
    up = models.BooleanField(default=True)  # False면 down