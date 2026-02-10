from django.test import TestCase
from .forms import ProfileSetup, AvailabilitySetup


class TestProfileSetup(TestCase):

    def test_form_is_valid(self):
        """Positive test for all fields"""
        profile_setup_form = ProfileSetup({'name': 'Test Name',
                                           'excerpt': 'Test excerpt',
                                           'bio': 'test bio',
                                           'experience': 'test exprerience',
                                           'specialism': 'test speciaslism',
                                           })
        self.assertTrue(profile_setup_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """Negative test for all fields"""
        profile_setup_form = ProfileSetup({'name': '',
                                           'excerpt': '',
                                           'bio': '',
                                           'experience': '',
                                           'specialism': '',
                                           })
        self.assertFalse(profile_setup_form.is_valid(), msg='Form is valid')

    def test_name_is_required(self):
        """Test for the 'name' field"""
        profile_setup_form = ProfileSetup({'name': '',
                                           'excerpt': 'test',
                                           'bio': 'test',
                                           'experience': 'test',
                                           'specialism': 'test',
                                           })
        self.assertFalse(profile_setup_form.is_valid(),
                         msg='No nmae provided. The form should be invalid')

    def test_excerpt_is_required(self):
        """Test for the 'excerpt' field"""
        profile_setup_form = ProfileSetup({'name': 'test',
                                           'excerpt': '',
                                           'bio': 'test',
                                           'experience': 'test',
                                           'specialism': 'test',
                                           })
        self.assertFalse(profile_setup_form.is_valid(),
                         msg='No excerpt provided. The form should be invalid')

    def test_bio_is_required(self):
        """Test for the 'bio' field"""
        profile_setup_form = ProfileSetup({'name': 'test',
                                           'excerpt': 'test',
                                           'bio': '',
                                           'experience': 'test',
                                           'specialism': 'test',
                                           })
        self.assertFalse(profile_setup_form.is_valid(),
                         msg='No bio provided. The form should be invalid')

    def test_experience_is_required(self):
        """Test for the 'experience' field"""
        profile_setup_form = ProfileSetup({'name': 'test',
                                           'excerpt': 'test',
                                           'bio': 'test',
                                           'experience': '',
                                           'specialism': 'test',
                                           })
        self.assertFalse(profile_setup_form.is_valid(),
                         msg='No experience provided. '
                         'The form should be invalid')

    def test_specialsim_is_required(self):
        """Test for the 'specialism' field"""
        profile_setup_form = ProfileSetup({'name': 'test',
                                           'excerpt': 'test',
                                           'bio': 'test',
                                           'experience': 'test',
                                           'specialism': '',
                                           })
        self.assertFalse(profile_setup_form.is_valid(),
                         msg='No specialism provided. '
                         'The form should be invalid')


class TestAvailabilitySetup(TestCase):

    def test_form_is_valid(self):
        """Positive test for all fields"""
        availability_setup_form = AvailabilitySetup({'date': '2026-08-02',
                                                     'start_time': '13:00',
                                                     'end_time': '14:00'})
        self.assertTrue(availability_setup_form.is_valid(),
                        msg='Form is not valid')

    def test_form_is_invalid(self):
        """Negative Test for all fields"""
        availability_setup_form = AvailabilitySetup({'date': '',
                                                     'start_time': '',
                                                     'end_time': ''})
        self.assertFalse(availability_setup_form.is_valid(),
                         msg='Form is valid')

    def test_start_required(self):
        """Test for the 'start-time' field"""
        availability_setup_form = AvailabilitySetup({'date': '2026-02-1',
                                                     'start_time': '',
                                                     'end_time': '13:00'})
        self.assertFalse(availability_setup_form.is_valid(),
                         msg='No start time provided. '
                         'The form shoulb be invalid')

    def test_date_required(self):
        """Test for the 'date' field"""
        availability_setup_form = AvailabilitySetup({'date': '',
                                                     'start_time': '12:00',
                                                     'end_time': '13:00'})
        self.assertFalse(availability_setup_form.is_valid(),
                         msg='No date provided. The form shoulb be invalid')

    def test_end_required(self):
        """Test for the 'end_time' field"""
        availability_setup_form = AvailabilitySetup({'date': '2026-01-1',
                                                     'start_time': '12:00',
                                                     'end_time': ''})
        self.assertFalse(availability_setup_form.is_valid(),
                         msg='No end time provided. '
                         'The form shoulb be invalid')
