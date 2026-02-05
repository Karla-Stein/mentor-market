from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime, timedelta
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))


class Profile(models.Model):
    """
    Model to store mentor details. :model: `auth.User`.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="mentor_profile"
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=120)
    bio = models.TextField()
    experience = models.TextField()
    specialism = models.TextField()
    member_since = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-member_since"]  # newest Profile is displayed first

    def __str__(self):
        return f"Profile of {self.user}"


AVAILABILITY_STATUS = ((0, "Open"), (1, "Booked"))


class TimeSlot(models.Model):
    """
    Model to store mentor availability. Where mentor, date, start and end time
    are unique together meaning in combination they can only exist
    once and prevent duplicate availability slots.
    Related to :model: `Profile`'
    """
    mentor = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="availability"
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    availability_status = models.IntegerField(choices=AVAILABILITY_STATUS, default=0)  # noqa 501

    class Meta:
        unique_together = ("mentor", "date", "start_time", "end_time")

    def __str__(self):
        return f"{self.mentor.name} is available on {self.date} from {self.start_time} to {self.end_time}"  # noqa 501

    # combine slot date and start_time to be
    # able to compare with current datetime
    @property
    def start_datetime(self):
        tz = timezone.get_current_timezone()
        naive = datetime.combine(self.date, self.start_time)
        return timezone.make_aware(naive, tz)

    # Ensure slot to be booked starts least 24 hours from time of booking
    @property
    def is_bookable(self):
        return self.start_datetime >= timezone.now() + timedelta(hours=24)
