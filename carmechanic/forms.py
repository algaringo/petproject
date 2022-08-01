from django import forms
from .models import AppRating, MechanicRating, Mechanic

MECHANIC = Mechanic.objects.all().values_list('mechanics', 'mechanics')

lists = []

for item in MECHANIC:
    lists.append(item)


class AppRatingForm(forms.ModelForm):
    class  Meta:
        model = AppRating
        labels = {
            'title' : 'Title',
            'content' : 'Comment',
            'ratings' : 'Rating'
        }
        fields = [
            'title',
            'content',
            'ratings'
        ]

class MechanicRatingForm(forms.ModelForm):
    class  Meta:
        model = MechanicRating
        labels = {
            'mechanicrating' : 'Rating',
            'comment' : 'Comment',
            'mechanics' : 'Mechanic'
        }
        fields = [
            'ratings',
            'content',
            'mechanics'
        ]
        widgets = {
            'mechanics': forms.Select(choices=lists, attrs={'class': 'form-control'})
        }