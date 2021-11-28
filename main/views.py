from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Post

def home(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request, 'main/forums.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post":post,
    }
    return render(request, 'main/detail.html', context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts":posts,
        "forum": category,
    }

    return render(request, 'main/posts.html', context)

