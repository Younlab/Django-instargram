from django.http import HttpResponse

from posts.models import Post
from django.shortcuts import render


def post_list(requset):
    # post = Post.objects.all()
    # context = {
    #     'posts':post,
    # }
    #
    # return render(requset, 'post-list', context)
    return HttpResponse('post-list')


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'posts':post,
        'pk':pk,
    }

    return render(request, 'post-detail', context)
