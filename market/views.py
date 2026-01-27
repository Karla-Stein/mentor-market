from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Profile, TimeSlot
from .forms import ProfileSetup, AvailabilitySetup
from django.contrib import messages
from django.utils.text import slugify


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
    time_slots = TimeSlot.objects.filter(
        mentor=profile,
        availability_status=0).order_by("date")

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
    Display a form to collect user data for profile set up
    or to edit for approved profiles.

    Context:
        profile:
        Instance of model Profile,
        profile_form:
        An instance of the ProfileSetup form,

    template:
        `market/profile_setup.html`
    """
    profile_form = ProfileSetup()

    if request.method == "POST":
        profile_form = ProfileSetup(request.POST, request.FILES)
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
    Display set availabilities.

    Context:
        availability_form:
        An instance of the AvailabilitySetup form.

    template:
        `market/availability.html`
    """
    availability_form = AvailabilitySetup()
    profile = get_object_or_404(Profile, user=request.user)
    time_slots = TimeSlot.objects.filter(
        mentor=profile,
        availability_status=0).order_by("date")

    # To store date as key and slot objects as value
    grouped_by_date = {}

    # Loop through open slots
    for slot in time_slots:
        if slot.date not in grouped_by_date:
            # Create empty list for date
            grouped_by_date[slot.date] = []
        # Add Time slot to the list
        grouped_by_date[slot.date].append(slot)

    if request.method == "POST":
        availability_form = AvailabilitySetup(data=request.POST)
        if availability_form.is_valid():
            availabilities = availability_form.save(commit=False)
            for slot in time_slots:
                if availabilities.date == slot.date:
                    if availabilities.start_time < slot.end_time or availabilities.end_time > slot.start_time:  # noqa 501
                        messages.add_message(
                            request,
                            messages.ERROR,
                            "Time overlep"
                        )
                        return redirect("availability")
            availabilities.mentor = profile
            availabilities.save()

            return redirect("availability")
                
    return render(
        request,
        "market/availability.html",
        {"availability_form": availability_form,
         "time_slots": time_slots,
         "grouped_by_date": grouped_by_date}

    )


def profile_delete(request, slug):
    """
    Enable Mentor to delete their profile.
    Redirects to homepage after modal confirmation.
    """
    queryset = Profile.objects.filter(status=1)
    profile = get_object_or_404(queryset, slug=slug)

    if request.user == profile.user:
        profile.delete()

        messages.add_message(
            request,
            messages.SUCCESS,
            "Profile successfully deleted"
        )

    return redirect("home")


def edit_profile(request):
    """
    Enable Mentor to edit their profile.
  
    Context:
    profile_form:
        An instance of the ProfileSetup form.

    Template:
        `market/profile_setup.html`

    """
    profile = Profile.objects.filter(user=request.user).first()
    profile_form = ProfileSetup(instance=profile)

    if request.method == "POST":
        profile_form = ProfileSetup(request.POST, request.FILES,
                                    instance=profile)
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
               "Profile edit successfully submitted"
            )

    return render(
        request,
        "market/profile_setup.html",
        {"profile_form": profile_form}

    )


def edit_availability(request, pk):
    """
    View to edit available slots

    Context:
    profile:
        An instance of the Profile model.
    slot:
        An instance of a timeslot identified by pk and mentor profile.
    availability_form:
        An instance of the availability set up form
        prepopulated with selected slot.

    Template:
        `market/availability.html`
    """
    profile = get_object_or_404(Profile, user=request.user)
    slot = get_object_or_404(TimeSlot, pk=pk, mentor=profile)
    availability_form = AvailabilitySetup(instance=slot)

    if request.method == "POST":
        availability_form = AvailabilitySetup(request.POST,
                                              instance=slot)
        if availability_form.is_valid():
            availability_form.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Availability successfully updated"
            )

            return redirect("availability")

    return render(
        request,
        "market/availability.html",
        {"availability_form": availability_form,
         "slot": slot}
    )


def delete_availability(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    slot = get_object_or_404(TimeSlot, pk=pk, mentor=profile)
    slot.delete()

    messages.add_message(
               request,
               messages.SUCCESS,
               "Availability slot successfully deleted"
           )
    
    return redirect("availability")



