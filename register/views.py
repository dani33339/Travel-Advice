from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from register.forms import UpdateForm
from django.contrib.auth import logout as lt
from users.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from forum.models import Author
from users.models import Profile

@unauthenticated_user
def signup(request):
    context={}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user=form.save()
            Guide_CheckBox = request.POST.getlist('Guide_CheckBox')
            if Guide_CheckBox:
                group = Group.objects.get(name='guide')
                new_user.groups.add(group)
                Profile.objects.create(
                    user=new_user,
                )
            else:
                group = Group.objects.get(name='traveler')
                new_user.groups.add(group)
            login(request,new_user)
            return redirect("update_profile")
    context.update({
        "form":form,
        "title":"Signup",
    })
    return render(request,"register/signup.html",context)

@unauthenticated_user
def signin(request):
    context = {}
    form = AuthenticationForm(request,data=request.POST)
    if request.method=="POST":
        if form.is_valid():
            user=form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            user = authenticate(username=user,password=password)
            if user is not None:
                login(request, user)
                return redirect("trips")
    context.update({
        "form":form,
        "title":"Signin",
    })
    return render(request,"register/signin.html",context)

@login_required
def update_profile(request):
    context = {}
    user = request.user
    form = UpdateForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            update_profile=form.save(commit=False)
            author = Author.objects.filter(user=request.user)
            if author:
                author.delete()
            else:
                update_profile.user=user
                update_profile.save()
                if user.groups.filter(name="guide"):
                     return redirect("edit-account")
                return redirect("trips")
    context.update({
        "form": form,
        "title": "Update",
    })

    return render(request, "register/update.html", context)

@login_required
def logout(request):
    lt(request)
    return redirect("trips")
