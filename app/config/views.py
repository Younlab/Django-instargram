from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def index(requset):
    return redirect('posts:post-list')