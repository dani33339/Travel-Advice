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

def createTrip(request): 
    form = TripForm()

    if request.method =='POST':
        form = TripForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('trips')
    context = {'form':form}
    return render(request,"trips/trip_form.html",context)    

def updateTrip(request,pk): 
    trip = Trip.objects.get(id=pk)
    form = TripForm(instance=trip)

    if request.method =='POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid(): 
            form.save()
            return redirect('trips')
    context = {'form':form}
    return render(request,"trips/trip_form.html",context)  

def deleteTrip(request,pk): 
    trip = Trip.objects.get(id=pk)
    if request.method == 'POST': 
        trip.delete()
        return redirect('trips')
    context = {'trip':trip}
    return render(request, 'trips/delete_template.html',context)