# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Vote
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def addPost(request):
    if request.method == 'POST':
        # new
        post = Post()
        post.title = request.POST.get('title', '')
        post.created_by = request.user
        post.save()
        # save
        return redirect(post.get_absolute_url())
    else:
        form = PostForm()
        return render(request, 'add_post.html', {'form': form})


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'DELETE':
        post.delete()
    return render(request, 'detail_post.html', {'post': post})


@csrf_exempt
def ratePost(request, pk):
    vote, create = Vote.objects.update_or_create(
        voted_by=request.user, on_post=Post.objects.get(pk=pk),
        defaults={'up': int(request.POST.get('val')) == 1}
    )
    vote.save()

    return HttpResponseRedirect("../")
