from django import forms
from .models import Profile, TimeSlot


class ProfileSetup(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'excerpt', 'bio', 'experience', 'specialism')


class AvailabilitySetup(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ('date', 'start_time', 'end_time')