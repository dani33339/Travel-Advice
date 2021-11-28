from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login,authenticate


def signup(request):
    context={}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect("home")
    context.update({
        "form":form,
        "title":"Signup",
    })
    return render(request,"register/signup.html",context)

def signin(request):
    context = {}
    form = AuthenticationForm(request,data=request.POST)
    if request.method=="POST":
        if form.is_valid():
            user=form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            user = authenticate(username=user,password=password)
            if user is not None:
                return redirect("home")
    context.update({
        "form":form,
        "title":"Signin",
    })
    return render(request,"register/signin.html",context)

