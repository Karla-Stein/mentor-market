from django.db import models
from market.models import TimeSlot


class Booking(models.Model):
    """
    A model to store visitor details for specific time slot.
  
    The booking model is also used to/as:
        - prevent double bookings via oneToOne relationship with TimeSlot
        - to render booked slots on the booking/booking.html for
        logged in mentors.
    """
    time_slot = models.OneToOneField(
        TimeSlot, on_delete=models.CASCADE, related_name="bookings"
    )
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    visitor_phone = models.CharField(max_length=25, blank=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-booked_at"]  # latest booking to be shown first
  
    def __str__(self):
        return f"{self.visitor_name} booked {self.time_slot.mentor.name} on {self.time_slot.date} at {self.time_slot.start_time}"  # noqa 501