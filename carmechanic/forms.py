from django import forms
from .models import CarPart, Checkout

class CarPartForm(forms.ModelForm):
    class  Meta:
        model = CarPart
        labels = {
            'productnames' : 'Productname',
            'descriptions' : 'Description',
            'price' : 'Price',
            'images' : 'Image URL',
        }
        fields = [
            'productnames',
            'descriptions',
            'price',
            'images',
        ]
