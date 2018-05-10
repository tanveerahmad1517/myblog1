from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from posts.models import Post


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        posts = Post.objects.all()
    else:
        user = request.user
    args = {'user': user, 'posts': posts}


    return render(request, 'posts/profile.html', args)