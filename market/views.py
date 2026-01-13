from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile, TimeSlot

# Create your views here.


class ProfileList(generic.ListView):
    queryset = Profile.objects.filter(status=1).order_by("-member_since")
    template_name = "market/index.html"
    paginate_by = 8


def profile_detail(request, slug):
    """
    Display an individual :model:`market.Profile`.

    **Context**

    ``profile``
        An instance of :model:`market.Profile`.

    **Template:**

    :template:`market/profile_detail.html`
    """
    queryset = Profile.objects.filter(status=1)
    profile = get_object_or_404(queryset, slug=slug)
    time_slots = TimeSlot.objects.filter(mentor=profile, availability_status=0)

    return render(
        request,
        "market/profile_detail.html",
        {"profile": profile,
         "time_slots": time_slots}
    )