from django.shortcuts import render

from .models import Post
# Create your views here.


def homeView(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        "posts": posts
    })