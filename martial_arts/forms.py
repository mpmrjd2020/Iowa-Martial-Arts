from django import forms
from .models import Location, Class_Schedule

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('dojo_name', 'address', 'picture_url', 'email', 'phone', 'cover',)


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class_Schedule
        fields = ('style', 'instructor', 'schedule', 'location',)

