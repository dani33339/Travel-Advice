from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def forumhome(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request,'forum/forums.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post":post,
    }
    return render(request,'forum/detail.html', context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts":posts,
        "forum": category,
    }

    return render(request, 'forum/posts.html', context)
@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            return redirect("home")
    context.update({
        "form": form,
        "title": "Create New Post",
    })
    return render(request, "forum/create_post.html", context)