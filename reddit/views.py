# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Vote, Comment
from .forms import PostForm, TestForm, CommentForm


def must_be_yours(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs["pk"]
        post = Post.objects.get(pk=pk)
        if not (post.created_by.id == request.user.id):
            return HttpResponse("It is not yours ! You are not permitted !",
                                content_type="application/json", status=403)
        return func(request, *args, **kwargs)

    return check_and_call


def index(request):
    print('index')
    posts = Post.objects.all()
    form = TestForm()
    print('response')
    # for post in posts:
    #     vote = post.votes.filter(voted_by=request.user)
    #     post.voted.up = vote.up
    #     post.voted.down = not vote.up
    return render(request, 'post_list.html', {'posts': posts, 'form': form})


def addPost(request):
    if request.method == 'POST':
        # new
        post = Post()
        post.title = request.POST.get('title', '')
        post.content = request.POST.get('content', '')
        post.created_by = request.user
        post.save()
        # save
        print(post.get_absolute_url())
        return redirect(post.get_absolute_url())
    else:
        form = PostForm()
        return render(request, 'post_add.html', {'form': form})


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comment_form': comment_form})


@csrf_exempt
def ratePost(request, pk):
    vote, create = Vote.objects.update_or_create(
        voted_by=request.user, on_post=Post.objects.get(pk=pk),
        defaults={'up': int(request.POST.get('val')) == 1}
    )
    vote.save()
    return HttpResponse('../')


@must_be_yours
def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('reddit:index')


@must_be_yours
def editPost(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title', '')
        post.content = request.POST.get('content', '')
        post.save()
        return redirect(post.get_absolute_url())
    elif request.method == 'GET':
        form = PostForm(initial={'title': post.title})
        return render(request, 'post_edit.html', {'post': post, 'form': form})
    else:
        message = '오류'
        response = JsonResponse({'status': 'false', 'message': message})
        response.status_code = 500
        return response


# comment

def addComment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        comment = Comment()
        print(request.POST.get('content', ''))
        comment.content = request.POST.get('content', '')
        comment.on_post = post
        comment.commented_by = request.user
        comment.save()
        return redirect(post.get_absolute_url())
    else:
        message = '잘못된 접근'
        response = JsonResponse({'status': 'false', 'message': message})
        response.status_code = 500
        return response


def editComment(request, pk):
    message = '잘못된 접근'
    response = JsonResponse({'status': 'false', 'message': message})
    response.status_code = 500
    return response


def deleteComment(request, pk):
    message = '잘못된 접근'
    response = JsonResponse({'status': 'false', 'message': message})
    response.status_code = 500
    return response


def addReply(request, pk):
    if request.method == 'POST':
        reply = Comment()
        reply.commented_by = request.user
        reply.content = request.POST.get('content', '')
        reply.reply_to = Comment.objects.get(pk=pk)
        reply.save()
        redirect_url = request.POST.get('redirect','')
        return redirect(redirect_url)
    else:
        message = '잘못된 접근'
        response = JsonResponse({'status': 'false', 'message': message})
        response.status_code = 500
        return response
