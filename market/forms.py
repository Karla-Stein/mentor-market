from django import forms
from .models import Profile


class ProfileSetup(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'excerpt', 'bio', 'experience', 'specialism')