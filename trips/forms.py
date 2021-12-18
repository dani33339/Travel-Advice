from django.db.models.base import Model
from django.forms import ModelForm, fields
from django import forms
from .models import Trip, Review

class TripForm(ModelForm): 
    class Meta: 
        model = Trip 
        fields = ['title','featured_image', 'description', 'tags'] # make form over all the fields in data base

        widgets = { 
            'tags':forms.CheckboxSelectMultiple(),
        }
    #כדי לעשות עיצוב על הטופס יצירת טיול חדש 
    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items(): 
            field.widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm): 
    class Meta: 
        model = Review 
        fields = ['value', 'body']

        labels = { 
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items(): 
            field.widget.attrs.update({'class':'input'})

                