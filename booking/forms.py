from django import forms
from .models import Booking


class VisitorBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('visitor_name', 'visitor_email', 'visitor_phone')