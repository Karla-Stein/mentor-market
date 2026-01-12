from django.db import models
from market.models import Profile

# Create your models here.

STATUS = ((0, "Open"), (1, "Booked"))


class Booking(models.Model):
    mentor = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="bookings"
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    visitor_phone = models.CharField(max_length=25)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("mentor", "date", "start_time", "end_time")
        ordering = ["-date", "-start_time"]  # newest Profile is displayed first  # noqa 501
    
    def __str__(self):
        return f"{self.mentor} is booked on {self.date} at {self.start_time}"