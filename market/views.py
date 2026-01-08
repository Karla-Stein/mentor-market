# from django.shortcuts import render
from django.views import generic
from .models import Profile

# Create your views here.


class ProfileList(generic.ListView):
    queryset = Profile.objects.filter(status=1).order_by("-member_since")
    template_name = "profile_list.html"
