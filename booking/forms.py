from django import forms
from .models import Booking


class VisitorBooking(forms.ModelForm):
    """
    Form to collect visitor data upon booking.

    **Model:**
        `booking.Booking`.
    """
    class Meta:
        model = Booking
        fields = ('visitor_name', 'visitor_email', 'visitor_phone')
