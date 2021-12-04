from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip

TripsSList = [

{'id': '1', 
'title': 'Morocco',
 'description': "The one that explores Morocco's famous souks, mosques and scenery over 5 days" 
 },

{ 'id': '2',
 'title': 'European Discovery',
  'description': "The one that uncovers Europe’s finest in just under 2 weeks, complete with Bavarian beer and gondola rides" 
  },

{'id': '3',
 'title': 'Vietnam Experience',
  'description': 'The one that brings you the best of Vietnam, from colourful cities to epic natural wonders' 
  }

]

def trips(request): 
    trips = Trip.objects.all()
    context = {'trips': trips}
    return render(request, 'trips/trips.html',context)



def trip(request,pk): 
    tripObj = Trip.objects.get(id=pk)
    return render(request, 'trips/single-trip.html',{'trip':tripObj})