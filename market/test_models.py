from django.test import TestCase
from django.contrib.auth.models import User
from market.models import Profile, TimeSlot


class ProfileModelTest(TestCase):
    """Tests for the Profile model."""
    def test_profile_str_return_profile_of_username(self):
        """Test that __str__ returns 'Profile of {username}'."""    
        # ARRANGE - Create the data we need
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

        # ACT - Do the action we're testing
        result = str(profile)
        # ASSERT - Check the result is what we expected
        self.assertEqual(result, 'Profile of alice',
                         msg='String message incorrect')
        
    def test_profile_status_to_draft(self):
        """Test that new profiles have status=0 (Draft) by default"""
        # Arrange 
        user = User.objects.create_user(username='Bob',
                                        password='testpw123')
        
        # Act
        profile = Profile.objects.create(user=user,
                                         name='Bob Jones',
                                         slug='bob-jones',
                                         excerpt='I mentor juniors',
                                         bio='test bio',
                                         experience='3years',
                                         specialism='Javascript'
                                         )
        # Assert
        self.assertEqual(profile.status, 0)

    def test_profile_is_linked_to_user(self):
        """Test that the profile correctly links to its user"""
        # Arrange
        user = User.objects.create_user(username='Maria',
                                        password='testpw123')
        profile = Profile.objects.create(user=user,
                                         name='Maria White',
                                         slug='maria-white',
                                         excerpt='test excerpt',
                                         bio='test bio',
                                         experience=' test experience',
                                         specialism='test specialism'
                                         )
        # Act & Assert
        self.assertEqual(profile.user, user)
        self.assertEqual(user.mentor_profile, profile)


class TimeSlotTest(TestCase):
    """Tests for the TimeSlot model."""
    def test_timeslot_str_return_mentorname_date_start_and_endtime(self):
        """Test that __str__ returns '{self.mentor.name} is available on
        {self.date} from {self.start_time} to {self.end_time}'."""  
        # ARRANGE - Create the data we need
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
                                           end_time='13:00'
                                           )

        # ACT 
        result = str(timeslot)
        # ASSERT 
        self.assertEqual(result, 'Alice Smith is available on 2026-02-02 from'
                         ' 12:00 to 13:00',
                         msg='String message incorrect')
        
    def test_timeslot_status_to_draft(self):
        """Test that new timeslots have availability_status=0 (Open)
        by default"""
        # Arrange
        user = User.objects.create_user(username='Bob',
                                        password='testpw123')
      
        profile = Profile.objects.create(user=user,
                                         name='Bob Jones',
                                         slug='bob-jones',
                                         excerpt='I mentor juniors',
                                         bio='test bio',
                                         experience='3years',
                                         specialism='Javascript'
                                         )
        # Act
        timeslot = TimeSlot.objects.create(mentor=profile,
                                           date='2026-02-02',
                                           start_time='12:00',
                                           end_time='13:00')
        # Assert
        self.assertEqual(timeslot.availability_status, 0,
                         msg='Availability status does not deafult to 0')
