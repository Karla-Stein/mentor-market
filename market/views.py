from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Profile, TimeSlot
from .forms import ProfileSetup, AvailabilitySetup
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect


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
            # set slug to profile name
            slug = slugify(profile.name)
            profile.slug = slug
            profile.save()
                
            messages.add_message(
               request,
               messages.SUCCESS,
               "Profile submitted. Awaiting approval"
            )

    return render(
        request,
        "market/profile_setup.html",
        {"profile_form": profile_form}

    )


def set_mentor_availability(request):
    """
    Display a form to collect mentor availability, after Profile approval

    Context:
        availability_form:
        An instance of the AvailabilitySetup form.

    template:
        `market/availability.html`
    """
    availability_form = AvailabilitySetup()
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        availability_form = AvailabilitySetup(data=request.POST)
        if availability_form.is_valid():
            availabilities = availability_form.save(commit=False)
            availabilities.mentor = profile
            availabilities.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Availability successfully submitted"
            )
                
    return render(
        request,
        "market/availability.html",
        {"availability_form": availability_form}

    ) 


def profile_edit(request, slug):
    """
    Update an existing profile (only if the logged-in user
    is the owner of the profile).  
    Redirect back to the profile_detail page afterwards.
    """
    queryset = Profile.objects.filter(status=1)
    profile = get_object_or_404(queryset, slug=slug, user=request.user)
    if request.method == "POST":
        profile_form = ProfileSetup(data=request.POST, instance=profile)

        if profile_form.is_valid():
            updated_profile = profile_form.save(commit=False)
            updated_profile.slug = slugify(updated_profile.name)
            updated_profile.approved = False  # forces re-approval after edits
            updated_profile.save()
            messages.success(request, "Profile updated!")
        else:
            messages.error(request, "Error updating Profile.")

    return HttpResponseRedirect(reverse("profile_detail", args=[slug]))    
