from django.forms import ModelForm
from .models import Trip

class TripForm(ModelForm): 
    class Meta: 
        model = Trip 
        fields = ['title','featured_image', 'description', 'tags'] # make form over all the fields in data base