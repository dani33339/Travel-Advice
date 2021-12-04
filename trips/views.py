from django.shortcuts import render
from django.http import HttpResponse


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
    page = 'trips'
    number = 9
    context = {'page':page, 'number':number,'trips':TripsSList}
    return render(request, 'trips/trips.html',context)



def trip(request,pk): 
    tripsObj = None
    for i in TripsSList: 
        if i['id'] == pk: 
            tripsObj = i
    return render(request, 'trips/single-trip.html',{'trip':tripsObj})