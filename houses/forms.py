from django import forms
from django.contrib.auth.models import User
from .models import Myhouses

class MyHouseEditForm(forms.ModelForm):    
    class Meta:        
        model = Myhouses        
        fields = ('name_of_accomodation', 'type_of_room', 'house_rent', 'availability', 'location', 'nearest_institution', 'description', 'image') 

  