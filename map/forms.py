from django import forms
from .models import Rental
from django_google_maps.widgets import GoogleMapsAddressWidget


class SampleForm(forms.ModelForm):

    class Meta(object):
        model = Rental
        fields = ['address', 'geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }