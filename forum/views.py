from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def forumhome(request):
    forums = Category.objects.all()
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
    }
    return render(request,'forum/forums.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)

    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

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
            return redirect("trips")
    context.update({
        "form": form,
        "title": "Create New Post",
    })
    return render(request, "forum/create_post.html", context)

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
    }

    return render(request, "forum/latest-posts.html", context)