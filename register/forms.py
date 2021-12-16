from django import forms
from forum.models import Author
from django.forms import widgets

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Author
        fields =("fullname","bio")

        
    #כדי לעשות עיצוב על הטופס יצירת טיול חדש 
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items(): 
            field.widget.attrs.update({'class':'input'})
    