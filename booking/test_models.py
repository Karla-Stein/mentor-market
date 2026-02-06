from django.test import TestCase
from django.contrib.auth.models import User
from market.models import TimeSlot, Profile
from booking.models import Booking


class BookingModelTest(TestCase):
    """Test for the Booking model."""
    def test_booking_str_return_profile_of_username(self):
        """Test that __str__ returns '{self.visitor_name} booked
        {self.time_slot.mentor.name} on {self.time_slot.date} at
        {self.time_slot.start_time}'.""" 
        # ARRANGE
        user = User.objects.create_user(username='alice',
                                        password='testpw123')
        profile = Profile.objects.create(user=user,
                                         name='Alice Smith',
                                         slug='alice-smith',
                                         excerpt='I help with Python',
                                         bio='Full bio here',
                                         experience='5 years teaching',
                                         specialism='Python programming'
                                         )
        timeslot = TimeSlot.objects.create(mentor=profile,
                                           date='2026-02-02',
                                           start_time='12:00',
                                           end_time='13:00')
        booking = Booking.objects.create(time_slot=timeslot,
                                         visitor_name='Lucy Wang',
                                         visitor_email='lucy@lucy.com')

        # ACT - Do the action we're testing
        result = str(booking)
        # ASSERT - Check the result is what we expected
        self.assertEqual(result, 'Lucy Wang booked Alice Smith on '
                         '2026-02-02 at 12:00',
                         msg='String message incorrect')
     
    def test_booking_is_linked_to_one_timeslot(self):
        """Test that the booking correctly links to one timeslot"""
        # ARRANGE
        user = User.objects.create_user(username='alice',
                                        password='testpw123')
        profile = Profile.objects.create(user=user,
                                         name='Alice Smith',
                                         slug='alice-smith',
                                         excerpt='I help with Python',
                                         bio='Full bio here',
                                         experience='5 years teaching',
                                         specialism='Python programming'
                                         )
        timeslot = TimeSlot.objects.create(mentor=profile,
                                           date='2026-02-02',
                                           start_time='12:00',
                                           end_time='13:00')
        booking = Booking.objects.create(time_slot=timeslot,
                                         visitor_name='Lucy Wang',
                                         visitor_email='lucy@lucy.com')

        # Act & Assert
        self.assertEqual(booking.time_slot, timeslot)
        self.assertEqual(timeslot.bookings, booking)

