from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip



def trips(request): 
    trips = Trip.objects.all()
    context = {'trips': trips}
    return render(request, 'trips/trips.html',context)



def trip(request,pk): 
    tripObj = Trip.objects.get(id=pk)
    tags = tripObj.tags.all()
    return render(request, 'trips/single-trip.html',{'trip':tripObj, 'tags': tags})