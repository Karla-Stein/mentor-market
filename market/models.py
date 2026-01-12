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
    excerpt = models.TextField(blank=True)
    bio = models.TextField()
    experience = models.TextField()
    specialism = models.TextField()
    member_since = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-member_since"]  # newest Profile is displayed first  # noqa 501
    
    def __str__(self):
        return f"Profile of {self.user}"
