from django.urls import path
from django.urls.resolvers import URLResolver
from . import views


urlpatterns = [ 
     path('', views.trips,name="trips"),
     path('trip/<str:pk>/',views.trip,name="trip"),

     path('create-trip/',views.createTrip,name="create-trip"),

     path('update-trip/<str:pk>/',views.updateTrip,name="update-trip"),

     path('delete-trip/<str:pk>/',views.deleteTrip,name="delete-trip"),
]