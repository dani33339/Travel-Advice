#this file contains functions views.py calls
from .models import Trip, Tag
#A Q object is an object used to encapsulate a collection of keyword arguments.
from django.db.models import Q


#trips search function
def searchTrips(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    trips = Trip.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return trips, search_query