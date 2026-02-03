from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .models import Profile, TimeSlot
from .forms import ProfileSetup, AvailabilitySetup


def redirectPNF(request, exception):
    """
    404 handler.
    Redirects the user to the home page in case of broken or non existing urls
    """
    return redirect('home')


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


@login_required
def set_mentor_profile(request):
    """
    Display a form to collect user data for profile set up
    or to edit for approved profiles.

    **Context:**
    ``profile:``
        Instance of :model: `market.Profile`.
    ``profile_form:``
        An instance of :form: `market.ProfileSetup form`.

    **template:**
    :template: `market/profile_setup.html`
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


@login_required
def set_mentor_availability(request):
    """
    Display a form to collect mentor availability, after Profile approval
    Display set availabilities.

    **Context:**
    ``availability_form:``
        An instance of the :form: `market.AvailabilitySetup`.
    ``profile``:
        An instance of :model: `market.Profile`.
    ``time_slot``:
    An instance of :model: `market.TimeSlot`.

    **Template:**
    :template: `market/availability.html`
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
            # prevent time overlap
            for slot in time_slots:
                if availabilities.date == slot.date:
                    if availabilities.start_time < slot.end_time and availabilities.end_time > slot.start_time:  # noqa 501
                        messages.add_message(
                            request,
                            messages.ERROR,
                            "Time overlap"
                        )
                        return redirect("availability")
                
            availabilities.mentor = profile
            availabilities.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Slot succesfully added"
            )

            return redirect("availability")
      
    return render(
        request,
        "market/availability.html",
        {"availability_form": availability_form,
         "time_slots": time_slots,
         "grouped_by_date": grouped_by_date}

    )


@login_required
def profile_delete(request, slug):
    """
    Enable Mentor to delete their profile.
    Redirects to homepage after modal confirmation.

    **Context**:
    ``profile``:
        An instance of :model: `market.Profile`.

    **Redirect**
    :template: `market.index.html`.
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


@login_required
def edit_profile(request):
    """
    Enable Mentor to edit their profile.

    **Context:**
    ``profile_form:``
        An instance of :form: `market.ProfileSetup`.

    **Template:**
    :template: `market/profile_setup.html`

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


@login_required
def edit_availability(request, pk):
    """
    View to edit available slots

    **Context:**
    ``profile:``
        An instance of :model: `market.Profile`.
    ``slot:``
        An instance of :model: `market.TimeSlot`.
    ``availability_form:``
        An instance of :form: `market.AvailabilitySetup`.
        prepopulated with selected slot.

    **Template:**
     :template: `market/availability.html`
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


@login_required
def delete_availability(request, pk):
    """
    Enable mentor to delete their set avaiability.
    Redirect sends mentor back to the updated availability page.

    **Context**:
    ``profile``:
        An instance of :model: `market.Profile`.
    ``slot``:
        An instance of :model: `market.TimeSlot`.

    **Redirect**
    :template: `market.availability.html`.
    """
    profile = get_object_or_404(Profile, user=request.user)
    slot = get_object_or_404(TimeSlot, pk=pk, mentor=profile)
    slot.delete()

    messages.add_message(
               request,
               messages.SUCCESS,
               "Availability slot successfully deleted"
           )
    return redirect("availability")
