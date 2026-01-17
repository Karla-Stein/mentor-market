from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile, TimeSlot
from .forms import ProfileSetup
from django.contrib import messages

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

    # To store date as key and slot objects as value
    grouped_by_date = {}

    # Loop through open slots 
    for slot in time_slots:
        if slot.date not in grouped_by_date:
            # Create empty list for date 
            grouped_by_date[slot.date] = []
        # Add Time slot to the list 
        grouped_by_date[slot.date].append(slot)

    return render(
        request,
        "market/profile_detail.html",
        {"profile": profile,
         "time_slots": time_slots,
         "grouped_by_date": grouped_by_date}
    )


def set_mentor_profile(request):
    """
    Display a form to collect user data for profile set up.

    Context:
        profile_form:
        An instance of the ProfileSetup form.

    template: 
        `market/profile_setup.html`
    """
    profile_form = ProfileSetup()
    if request.method == "POST":
        profile_form = ProfileSetup(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

    messages.add_message(
        request,
        messages.SUCCESS,
        "Profile submitted and awaiting approval"
    )

    return render(
        request,
        "market/profile_setup.html",
        {"profile_form": profile_form}

    )
