from django.shortcuts import render, get_object_or_404, redirect
from market.models import TimeSlot, Profile
from .models import Booking
from .forms import VisitorBooking
from django.contrib import messages


def book_a_slot(request, pk):
    """
    View to receive a booking and update the booking status

    Context:
        slot:
        An instance of of an available timeslot, identified by the pk of the
        slot that was clicked by the visitor

        booking_form:
        An instance of the VisitorBooking Form, tied to the booking model

    Template:
        'booking/booking.html'
    """
    slot = get_object_or_404(TimeSlot, pk=pk, availability_status=0)
    booking_form = VisitorBooking()

    if request.method == "POST":
        booking_form = VisitorBooking(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.time_slot = slot
            slot.availability_status = 1
            booking.save()
            slot.save()

            messages.add_message(
               request,
               messages.SUCCESS,
               f"Booking request for {slot.date} at "
               f"{slot.start_time} received. Please allow 24H for "
               f"{slot.mentor.name} to contact you via provided email. "
            )

            return redirect("home")

    return render(
        request,
        "booking/booking.html",
        {"booking_form": booking_form,
         "slot": slot
         }

    )


def booking_details(request):
    """
    View to list all bookings for request user.

    Context:
        booked_slots:
        An Instance of all booking objects, that belong the requesting mentor.

    Template:
        "booking/booking_details.html"
    """
    profile = get_object_or_404(Profile, user=request.user)
    # using reverse traversal to walk through relationships
    booked_slots = Booking.objects.filter(time_slot__mentor=profile).order_by("time_slot__date", "time_slot__start_time")  # noqa 501

    return render(
        request,
        "booking/booking_details.html",
        {"booked_slots": booked_slots,
         }
    )
