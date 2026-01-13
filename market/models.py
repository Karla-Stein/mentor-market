from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="mentor_profile"
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
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
    