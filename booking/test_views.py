from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from market.models import Profile, TimeSlot
from .models import Booking


class TestBookASlotView(TestCase):
    """Test status code"""
    def setUp(self):
        self.user = User.objects.create_user(
                username="Test_user",
                password="testpw123",
                email="test@test.com"
            )

        self.profile = Profile(user=self.user, name="Test User",
                               slug="test-user", excerpt="Blog excerpt",
                               bio="test bio",
                               experience="test experience",
                               specialism="test specialism", status=1)
        self.profile.save()

        self.timeslot = TimeSlot(mentor=self.profile, date="2026-02-12",
                                 start_time="10:00",
                                 end_time="11:00",
                                 availability_status=0)
        self.timeslot.save()

    def test_status_code(self):
        response = self.client.get(
            reverse('book_a_slot_with', args=[self.timeslot.pk]))
        self.assertEqual(response.status_code, 200)

    def test_create_booking(self):
        visitor_data = {
                        "visitor_name": "Bob Visitor",
                        "visitor_email": "bob@test.com"
                       }
        response = self.client.post(reverse('book_a_slot_with',
                                    args=[self.timeslot.pk]),
                                    visitor_data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Booking.objects.filter(
                        time_slot=self.timeslot,
                        visitor_email="bob@test.com"
                        ).exists(),
                        msg="The booking does not exist")
        self.assertFalse(Booking.objects.filter(
                        time_slot=self.timeslot,
                        visitor_email=""
                        ).exists(),
                        msg="The booking exist despite not having "
                        "a required email")
