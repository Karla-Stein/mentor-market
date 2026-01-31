from django import forms
from .models import Profile, TimeSlot


class ProfileSetup(forms.ModelForm):
    """
    Form to collect Mentor details.
    Model:
        Profile
    """
    class Meta:
        model = Profile
        fields = ('name', 'excerpt', 'bio', 'experience', 'specialism',
                  'featured_image')


class AvailabilitySetup(forms.ModelForm):
    """
    Form to collect Mentor availability.
    Model:
        TimeSlot
    """
    class Meta:
        model = TimeSlot
        fields = ('date', 'start_time', 'end_time')
        # Add date and time picker
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control', 'step': '3600'}
            ),
            'end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control', 'step': '3600'}
            )}
