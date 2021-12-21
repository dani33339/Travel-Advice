from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review, Trip
from .forms import TripForm, ReviewForm
from django.contrib import messages
from .utils import searchTrips


def trips(request): 
    trips, search_query = searchTrips(request)
    context = {'trips': trips, 'search_query': search_query}
    return render(request, 'trips/trips.html',context)


def trip(request,pk): 
    tripObj = Trip.objects.get(id=pk)
    tags = tripObj.tags.all()
    form = ReviewForm()

    if request.method == 'POST': 
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.trip = tripObj
        review.owner = request.user.profile
        review.save()
        tripObj.getVoteCount()
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('trip',pk=tripObj.id)

    return render(request, 'trips/single-trip.html',{'trip':tripObj, 'tags': tags,'form':form})

@login_required(login_url='login')
def createTrip(request): 
    profile = request.user.profile
    form = TripForm()

    if request.method =='POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid(): 
            trip = form.save(commit=False)
            trip.owner = profile
            trip.save()
            return redirect('account')
    context = {'form':form}
    return render(request,"trips/trip_form.html",context)    

@login_required(login_url='login')
def updateTrip(request,pk): 
    profile = request.user.profile
    trip = profile.trip_set.get(id=pk)
    form = TripForm(instance=trip)

    if request.method =='POST':
        form = TripForm(request.POST, request.FILES,instance=trip)
        if form.is_valid(): 
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request,"trips/trip_form.html",context)  

@login_required(login_url='login')
def deleteTrip(request,pk): 
    profile = request.user.profile
    trip = profile.trip_set.get(id=pk)
    if request.method == 'POST': 
        trip.delete()
        return redirect('account')
    context = {'trip':trip}
    return render(request, 'delete_template.html',context)

