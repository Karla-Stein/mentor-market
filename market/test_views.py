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


class TestSetMentorProfileViews(TestCase):
    """Tests login required and feedback message"""
    def setUp(self):

        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
           )

        self.client.login(
            username="Test_user", password="testpw123")

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertNotEqual(response.status_code, 200)

    def test_status_code_and_feedback_msg(self):

        profile_data = {"name": "Test User",
                        "excerpt": "Blog excerpt",
                        "bio": "test bio",
                        "experience": "test experience",
                        "specialism": "test specialism",
                        }
        response = self.client.post(reverse(
            'profile'), profile_data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.client.login(
            username="Test_user", password="testpw123"))
        self.assertIn(
            b"Profile submitted. Awaiting approval",
            response.content
        )


class TestSetMentorAvailabilityView(TestCase):
    """Tests for login required and successfull adding of slots"""
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
           )
        self.client.login(
            username="Test_user", password="testpw123")

        self.profile = Profile(user=self.user, name="Test User",
                               slug="test-user", excerpt="Blog excerpt",
                               bio="test bio", experience="test experience",
                               specialism="test specialism", status=1)
        self.profile.save()

    def test_status_code(self):
        self.client.logout()
        response = self.client.get(reverse('availability'))
        self.assertNotEqual(response.status_code, 200)

    def test_slot_successful_submitted(self):
        slot_data = {
            "date": "2026-01-01",
            "start_time": "10:00",
            "end_time": "11:00",
        }
        response = self.client.post(reverse('availability'), slot_data,
                                    # follows the redirect
                                    follow=True)

        self.assertIn(
            b"Slot succesfully added",
            response.content
        )


class TestProfileDeleteView(TestCase):
    """Tests for login required and succefully deletion of a profile"""
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
        )
        self.client.login(
            username="Test_user", password="testpw123")

        self.profile = Profile(user=self.user, name="Test User",
                               slug="test-user", excerpt="Blog excerpt",
                               bio="test bio", experience="test experience",
                               specialism="test specialism", status=1)
        self.profile.save()

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('profile_delete',
                                           args=["test-user"]))
        self.assertNotEqual(response.status_code, 200)

    def test_status_code_and_response_content(self):
        response = self.client.get(reverse('profile_delete',
                                           args=["test-user"]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Profile successfully deleted",
            response.content
        )
        # check if the deleted profile still exists
        self.assertFalse(
            Profile.objects.filter(slug='test-user').exists(),
            msg="Profile not deleted"
        )


class TestEditProfileView(TestCase):
    """Test for login required, succesfull editing"""
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
        )
        self.client.login(
            username="Test_user", password="testpw123")

        self.profile = Profile(user=self.user, name="Test User",
                               slug="test-user", excerpt="Blog excerpt",
                               bio="test bio", experience="test experience",
                               specialism="test specialism", status=1)
        self.profile.save()

    def test_login_required(self):
        # check that status_code is not 200, if not logged in
        self.client.logout()
        response = self.client.get(reverse('edit_profile'))
        self.assertNotEqual(response.status_code, 200)

    def test_form_updatet(self):
        profile_data = {
            "name": "New Name",
            "excerpt": "Blog excerpt",
            "bio": "test bio",
            "experience": "test experience",
            "specialism": "test specialism"
        }
        response = self.client.post(reverse('edit_profile'), profile_data)
        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b"Profile edit successfully submitted",
            response.content
        )
        # Updates DB with new profile_data
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.name, "New Name")
