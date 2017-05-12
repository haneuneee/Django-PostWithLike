# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Post(models.Model):
    created_by = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
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

    def up_voted_by(self, user):
        if self.votes.filter(voted_by=user).exists():
            return self.votes.filter(voted_by=user)[0].up
        else:
            return False

    def down_voted_by(self, user):
        if self.votes.filter(voted_by=user).exists():
            return not self.votes.filter(voted_by=user)[0].up
        else:
            return False


class Vote(models.Model):
    voted_by = models.ForeignKey(User)
    on_post = models.ForeignKey(Post, related_name='votes')
    up = models.BooleanField(default=True)  # False면 down


class Comment(models.Model):
    commented_by = models.ForeignKey(User)
    on_post = models.ForeignKey(Post, related_name='comments', null=True)
    reply_to = models.ForeignKey('self', related_name='replies',null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def description(self):
        replies = []
        for reply in self.replies.all():
            replies.append(reply.description())
        return {
            'id':self.id,
            'content':self.content,
            'commented_by': self.commented_by.username,
            'created_at':self.created_at.strftime("%H:%m"),
            'replies': replies
        }
