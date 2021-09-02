from django import forms
from .models import *

# car add form
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('name', 'model', 'horsepower', 'description', 'price', 'image')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ("comment", "rating")