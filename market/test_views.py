from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from .models import Profile, TimeSlot


class TestProfileDetailViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
        )
        self.profile = Profile(user=self.user, name="Test User",
                               slug="test-user", excerpt="Blog excerpt",
                               bio="test bio", experience="test experience",
                               specialism="test specialism", status=1)
        self.profile.save()

        # Dynamic date and time fields so that data will be valid in the future
        now = timezone.now()
        deadline = now + timedelta(hours=25)
        self.timeslot = TimeSlot(mentor=self.profile, date=deadline.date(),
                                 start_time=deadline.time(),
                                 end_time=(deadline +
                                           timedelta(hours=1)).time(),
                                 availability_status=0)
        self.timeslot.save()

    def test_profile_detail_loads_correct_profile(self):
        response = self.client.get(reverse(
            'profile_detail', args=['test-user']))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test User", response.content,
                      msg="Name is required, but not provided")
        self.assertIsInstance(
            response.context['profile'], Profile,
            msg="profile is not an instance of Profile")

        grouped_by_date = response.context['grouped_by_date']
        self.assertIn(
            self.timeslot, grouped_by_date[self.timeslot.date],
            msg="Time slot not bookable")
        self.assertIn(self.timeslot.date, grouped_by_date,
                      msg="Date should be in 'grouped_by_date")
