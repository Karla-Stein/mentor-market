from django.test import TestCase
from .forms import VisitorBooking


class TestVisitorBooking(TestCase):

    def test_form_is_valid(self):
        """Positive test for all fields"""
        visitor_booking_form = VisitorBooking({'visitor_name': 'Test Name',
                                              'visitor_email': 'test@email.com'
                                               })

        self.assertTrue(visitor_booking_form.is_valid(),
                        msg='Form is not valid')

    def test_form_is_invalid(self):
        """Negative test for all fields"""
        visitor_booking_form = VisitorBooking({'visitor_name': '',
                                               'visitor_email': ''
                                               })
        self.assertFalse(visitor_booking_form.is_valid(), msg='Form is valid')

    def test_name_is_required(self):
        """Test for 'visitor_name' field"""
        visitor_booking_form = VisitorBooking({'visitor_name': '',
                                               'visitor_email':
                                               'test@email.com'
                                               })
        self.assertFalse(visitor_booking_form.is_valid(),
                         msg='No name provided. The form should be invalid')

    def test_email_is_required(self):
        """Test for 'visitor_email' field"""
        visitor_booking_form = VisitorBooking({'visitor_name': 'name',
                                              'visitor_email': ''
                                               })
        self.assertFalse(visitor_booking_form.is_valid(),
                         msg='No email provided. The form should be invalid')
