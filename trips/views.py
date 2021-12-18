from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trip
from .forms import TripForm



def trips(request): 
    trips = Trip.objects.all()
    context = {'trips': trips}
    return render(request, 'trips/trips.html',context)



def trip(request,pk): 
    tripObj = Trip.objects.get(id=pk)
    tags = tripObj.tags.all()
    return render(request, 'trips/single-trip.html',{'trip':tripObj, 'tags': tags})

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
            return redirect('trips')
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
            return redirect('trips')
    context = {'form':form}
    return render(request,"trips/trip_form.html",context)  

@login_required(login_url='login')
def deleteTrip(request,pk): 
    profile = request.user.profile
    trip = profile.trip_set.get(id=pk)
    if request.method == 'POST': 
        trip.delete()
        return redirect('trips')
    context = {'trip':trip}
    return render(request, 'trips/delete_template.html',context)

