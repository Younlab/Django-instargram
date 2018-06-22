from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from django.shortcuts import render



def post_list(requset):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }

    return render(requset, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'posts':post,
        'pk':pk,
    }

    return render(request, 'posts/post_detail.html', context)
