# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation

### HTML

I have used the recommended HTML W3C Validator to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| market | [index.html](https://github.com/Karla-Stein/mentor-market/blob/main/market/templates/market/index.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmy-mentor-market-e1c13c4d04df.herokuapp.com%2F) | ![screenshot](documentation/html_validation/index.jpeg) | Homepage does not require log-in, hence validated via URL |
| market | [profile_detail.html](https://github.com/Karla-Stein/mentor-market/blob/main/market/templates/market/profile_detail.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmy-mentor-market-e1c13c4d04df.herokuapp.com%2Fkarla-steinbrink%2F) | ![screenshot](documentation/html_validation/profile_detail.jpeg) | Detailed profile page does not require log-in, hence validated via URL. |
| market | [profile_setup.html](https://github.com/Karla-Stein/mentor-market/blob/main/market/templates/market/profile_setup.html) |  | ![screenshot](documentation/html_validation/profile_setup_input.jpeg) | Log in required, hence validated by input. |
| market | [profile_setup.html]((https://github.com/Karla-Stein/mentor-market/blob/main/market/templates/market/profile_setup.html)) | edit-profile/ | ![screenshot](documentation/html_validation/profile_edit_input.jpeg) | Edit route uses profile_setup template. Login required, hence validated by input. |
| market | [availability.html](https://github.com/Karla-Stein/mentor-market/blob/main/market/templates/market/availability.html) |  | ![screenshot](documentation/html_validation/availability_input.jpeg) |  Log in required, hence validated by input.|
| market | [availabilityp.html](https://github.com/Karla-Stein/mentor-market/blob/main/market/templates/market/availability.html)|  edit-availability/<pk> | ![screenshot](documentation/html_validation/edit_availability_input.jpeg) | Edit route uses availability template. Login required, hence validated by input.|
| booking | [booking_details.html](https://github.com/Karla-Stein/mentor-market/blob/main/booking/templates/booking/booking_details.html) |  | ![screenshot](documentation/html_validation/my_booking_details_input.jpeg) |  Log in required, hence validated by input. |
| booking | [booking.html](https://github.com/Karla-Stein/mentor-market/blob/main/booking/templates/booking/booking.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmy-mentor-market-e1c13c4d04df.herokuapp.com%2Fbooking%2Fbook-a-slot%2F75) | ![screenshot](documentation/html_validation/booking.jpeg) | Booking page does not require log-in, hence validated via URL. |

> **Note:**  
> Authentication-related templates (login, logout, signup, password reset) are provided by `django-allauth`.  
> They were not modified as part of this project and only inherit global styling via the base template.  
> As no custom HTML structure was introduced, I excluded these templates from manual HTML validation.


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/Karla-Stein/mentor-market/blob/main/static/css/style.css) | [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmy-mentor-market-e1c13c4d04df.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings)| ![screenshot](documentation/css_validation/css.jpeg) | |
| static | [style.css](https://github.com/Karla-Stein/mentor-market/blob/main/static/css/style.css) | [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmy-mentor-market-e1c13c4d04df.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings)| ![screenshot](documentation/css_validation/css_warnings.jpeg) | CSS validation produced warnings related to CSS custom properties (variables). These warnings are expected due to the dynamic nature of CSS variables and do not affect functionality or browser compatibility. |



### Javascript

I have used the recommended [JShint Validator](https://jshint.com) to validate my JS files.

| Directory | File | Screenshot | 
| --- | --- | --- | 
| static | [availability_delete.js](https://github.com/Karla-Stein/mentor-market/blob/main/static/js/availability_delete.js) | ![screenshot](documentation/js/availability_delete.jpeg) |  
| static | [profile_delete.js](https://github.com/Karla-Stein/mentor-market/blob/main/static/js/profile_delete.js) |  ![screenshot](documentation/js/profile_delete.jpeg) |  


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | 
| --- | --- | --- | --- | 
| booking | [admin.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/admin.py) | ![screenshot](documentation/python_validation/booking_admin.jpeg) | 
| booking | [forms.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/forms.py) | ![screenshot](documentation/python_validation/booking_forms.jpeg) | 
| booking | [models.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/models.py) | ![screenshot](documentation/python_validation/booking_models.jpeg) | 
| booking | [test_forms.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/test_forms.py) | ![screenshot](documentation/python_validation/booking_test_forms.jpeg) | 
| booking | [test_models.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/test_models.py) | ![screenshot](documentation/python_validation/booking_test_models.jpeg) | 
| booking | [test_views.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/test_views.py) |  [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/test_views.py) | ![screenshot](documentation/python_validation/booking_test_views.jpeg)
| booking | [urls.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/urls.py) | ![screenshot](documentation/python_validation/booking_urls.jpeg) | 
| booking | [views.py](https://github.com/Karla-Stein/mentor-market/blob/main/booking/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/booking/views.py) | ![screenshot](documentation/python_validation/booking_views.jpeg) | 
| market | [admin.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/admin.py) | ![screenshot](documentation/python_validation/market_admin.jpeg) | 
| market | [forms.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/forms.py) | ![screenshot](documentation/python_validation/market_forms.jpeg) | 
| market | [models.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/models.py) | ![screenshot](documentation/python_validation/market_models.jpeg) | 
| market | [test_forms.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/test_forms.py) | ![screenshot](documentation/python_validation/market_test_forms.jpeg) | 
| market | [test_models.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/test_models.py) | ![screenshot](documentation/python_validation/market_test_models.jpeg) | 
| market | [test_views.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/test_views.py) |  [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/test_views.py) | ![screenshot](documentation/python_validation/market_test_views.jpeg)
| market | [urls.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/urls.py) | ![screenshot](documentation/python_validation/market_urls.jpeg) | 
| market | [views.py](https://github.com/Karla-Stein/mentor-market/blob/main/market/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/market/views.py) | ![screenshot](documentation/python_validation/market_views.jpeg) | 
| mentor_market | [settings.py](https://github.com/Karla-Stein/mentor-market/blob/main/mentor_market/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/mentor_market/settings.py) | ![screenshot](documentation/python_validation/mentor_market_settings.jpeg) | 
| mentor_market | [urls.py](https://github.com/Karla-Stein/mentor-market/blob/main/mentor_market/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/mentor-market/refs/heads/main/mentor_market/urls.py) | ![screenshot](documentation/python_validation/mentor_market_urls.jpeg) | 


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Sign up | ![screenshot](documentation/browsers/chrome_signup.jpeg) | ![screenshot](documentation/browsers/firefox_signup.jpeg) | ![screenshot](documentation/browsers/safari_signup.jpeg) | Works as expected |
| Log in| ![screenshot](documentation/browsers/chrome_login.jpeg) | ![screenshot](documentation/browsers/firefox_login.jpeg) | ![screenshot](documentation/browsers/safari_login.jpeg) | Works as expected |
| Log out | ![screenshot](documentation/browsers/chrome_logout.jpeg) | ![screenshot](documentation/browsers/firefox_logout.jpeg) | ![screenshot](documentation/browsers/safari_logout.jpeg) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome_home.jpeg) | ![screenshot](documentation/browsers/firefox_home.jpeg) | ![screenshot](documentation/browsers/safari_home.jpeg) | Works as expected |
| Profile setup  | ![screenshot](documentation/lighthouse/profilesetup_mobile.jpeg) | ![screenshot](documentation/lighthouse/profilesetup_desktop.jpeg) |
| My Profile | ![screenshot](documentation/browsers/chrome_myprofile.jpeg) | ![screenshot](documentation/browsers/firefox_myprofile.jpeg) | ![screenshot](documentation/browsers/safari_myprofile.jpeg) | Works as expected |
| My Availability | ![screenshot](documentation/browsers/chrome_myavailability.jpeg) | ![screenshot](documentation/browsers/firefox_myavailability.jpeg) | ![screenshot](documentation/browsers/safari_myavailability.jpeg) | Does not work as expected on Safari, as there is no hint that slots must be booked on the hour. |
| My Bookings | ![screenshot](documentation/browsers/chrome_mybookings.jpeg) | ![screenshot](documentation/browsers/firefox_mybookings.jpeg) | ![screenshot](documentation/browsers/safari_mybookings.jpeg) | Works as expected |
| Edit Profile | ![screenshot](documentation/browsers/chrome_editprofile.jpeg) | ![screenshot](documentation/browsers/firefox_editprofile.jpeg) | ![screenshot](documentation/browsers/safari_editprofile.jpeg) | Works as expected |
| Edit Availability | ![screenshot](documentation/browsers/chrome_editavailability.jpeg) | ![screenshot](documentation/browsers/firefox_editavailability.jpeg) | ![screenshot](documentation/browsers/safari_editavailability.jpeg) | Does not work as expected on Safari. No hint that slots must be booked on the hour.|
| Book A Slot | ![screenshot](documentation/browsers/chrome_bookaslot.jpeg) | ![screenshot](documentation/browsers/firefox_bookaslot.jpeg) | ![screenshot](documentation/browsers/safari_bookaslot.jpeg) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome_404.jpeg) | ![screenshot](documentation/browsers/firefox_404.jpeg) | ![screenshot](documentation/browsers/safari_404.jpeg) | Works as expected |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Sign up | ![screenshot](documentation/responsiveness/mobile_signup.png) | ![screenshot](documentation/responsiveness/tablet_signup.jpeg) | ![screenshot](documentation/browsers/chrome_signup.jpeg) | Works as expected |
| Log out | ![screenshot](documentation/responsiveness/mobile_logout.png) | ![screenshot](documentation/responsiveness/tablet_logout.jpeg) | ![screenshot](documentation/browsers/chrome_logout.jpeg) | Works as expected |
| Log in | ![screenshot](documentation/responsiveness/mobile_login.png) | ![screenshot](documentation/responsiveness/tablet_login.jpeg) | ![screenshot](documentation/browsers/chrome_login.jpeg) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile_home.png) | ![screenshot](documentation/responsiveness/tablet_home.jpeg) | ![screenshot](documentation/browsers/chrome_home.jpeg) | Works as expected |
| Profile setup  | ![screenshot](documentation/lighthouse/profilesetup_mobile.jpeg) | ![screenshot](documentation/lighthouse/profilesetup_desktop.jpeg) |
| My Profile | ![screenshot](documentation/responsiveness/mobile_myprofile.png) | ![screenshot](documentation/responsiveness/tablet_myprofile.jpeg) | ![screenshot](documentation/browsers/chrome_myprofile.jpeg) | Works as expected |
| Edit Profile | ![screenshot](documentation/responsiveness/mobile_profileedit.png) | ![screenshot](documentation/responsiveness/tablet_editprofile.jpeg) | ![screenshot](documentation/browsers/chrome_editprofile.jpeg) | Works as expected |
| My Availability | ![screenshot](documentation/responsiveness/mobile_myavailability.png) | ![screenshot](documentation/responsiveness/tablet_myavailability.jpeg) | ![screenshot](documentation/browsers/chrome_myavailability.jpeg) | Works as expected |
| Edit Availability | ![screenshot](documentation/responsiveness/mobile_editavailability.png) | ![screenshot](documentation/responsiveness/tablet_editavailability.jpeg) | ![screenshot](documentation/browsers/chrome_editavailability.jpeg) | Works as expected |
| My Bookings | ![screenshot](documentation/responsiveness/mobile_mybookings.png) | ![screenshot](documentation/responsiveness//tablet_mybookings.jpeg) | ![screenshot](documentation/browsers/chrome_mybookings.jpeg) | Works as expected |
| Book A Slot | ![screenshot](documentation/responsiveness/mobile_bookaslot.png) | ![screenshot](documentation/responsiveness/tablet_bookaslot.jpeg) | ![screenshot](documentation/browsers/chrome_bookaslot.jpeg) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile_404.png) | ![screenshot](documentation/responsiveness/tablet_404.jpeg) | ![screenshot](documentation/browsers/chrome_404.jpeg) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Sign up | ![screenshot](documentation/lighthouse/mobile_signup.jpeg) | ![screenshot](documentation/lighthouse/signup_desktop.jpeg) |
| Log in | ![screenshot](documentation/lighthouse/mobile_login.jpeg) | ![screenshot](documentation/lighthouse/login_desktop.jpeg) |
| Log out | ![screenshot](documentation/lighthouse/mobile_logout.jpeg) | ![screenshot](documentation/lighthouse/logout_desktop.jpeg) |
| Home | ![screenshot](documentation/lighthouse/mobile_home.jpeg) | ![screenshot](documentation/lighthouse/home_desktop.jpeg) |
| Profile setup  | ![screenshot](documentation/lighthouse/mobile_profilesetup.jpeg) | ![screenshot](documentation/lighthouse/profilesetup_desktop.jpeg) |
| My Profile | ![screenshot](documentation/lighthouse/mobile_profiledetail.jpeg) | ![screenshot](documentation/lighthouse/profile_desktop.jpeg) |
| Edit Profile | ![screenshot](documentation/lighthouse/mobile_editprofile.jpeg) | ![screenshot](documentation/lighthouse/editprofile_desktop.jpeg) |
| My availability | ![screenshot](documentation/lighthouse/mobile_myavailability.jpeg) | ![screenshot](documentation/lighthouse/availability_desktop.jpeg) |
| Edit Availability | ![screenshot](documentation/lighthouse/mobile_editavailability.jpeg) | ![screenshot](documentation/lighthouse/editavailability_desktop.jpeg) |
| My Bookings | ![screenshot](documentation/lighthouse/mobile_mybookings.jpeg) | ![screenshot](documentation/lighthouse/mybookings_desktop.jpeg) |
| Book A Slot | ![screenshot](documentation/lighthouse/mobile_bookaslot.jpeg) | ![screenshot](documentation/lighthouse/bookingform_desktop.jpeg) |
| 404 | ![screenshot](documentation/lighthouse/mobile_404.jpeg) | ![screenshot](documentation/lighthouse/404_desktop.jpeg) |


## Defensive Programming


Defensive programming was manually tested to ensure the application handles invalid input, prevents unauthorised access and protects user data. Testing was performed across user types: guest user, Mentor A, Mentor B, and admin/superuser where applicable.

| Page / Feature | Expectation | Test Performed | Result Received | Screenshot |
| --- | --- | --- | --- | --- | 
| Profile setup | Mentor must be logged in to create a profile. | Attempted to access profile setup while logged out. | Redirected to login page (access denied). | ![screenshot](documentation/defensive/not_authorised_setup_to_login.jpeg)|
|  | Users cannot submit an empty profile form. | Profile form with required fields submitted blank. | Validation errors displayed; profile not created. | ![screenshot](documentation/defensive/profile_setup_blank_field.jpeg)|
|  | Slug is generated safely from mentor name. | Created profile with valid name containing spaces/capital letters. | Slug generated correctly and profile saved. | ![screenshot](documentation/defensive/slug.jpeg) |
| Edit Profile | A mentor can only edit their own profile. | Logged in as Mentor A, visited `edit-profile/` and confirmed the form loads with Mentor A’s existing data. | Form was pre-populated with Mentor A’s profile. | ![screenshot](documentation/defensive/edit_profile_formload.jpeg) |
|  | A mentor can not edit another mentor’s profile via URL manipulation. | Logged in as Mentor A and attempted to access another profile by altering the URL. (Not possible by design because `edit-profile/` does not accept a `pk` or `slug`.) Also attempted direct access to a public profile URL (`/<slug>/`) and confirmed it only displays details, not an edit option. | Access denied. 404 returned. | ![screenshot](documentation/defensive/mentor-edit-404.jpeg) |
| Delete Profile | A mentor can only delete their own profile. | Logged in as Mentor A and used the delete option from their own profile. | Profile was deleted successfully and user was redirected as expected. | ![screenshot](documentation/defensive/successfull_profile_delete.jpeg) |
|  | A mentor can not be able to delete another mentor’s profile. | Logged in as Mentor A and viewed Mentor B’s profile. The delete button was not displayed in the UI. Then manually attempted to access Mentor B’s delete URL by altering the slug in the browser. | Deletion was prevented at two levels: (1) the delete button is conditionally rendered only for the profile owner, and (2) the backend view validates ownership (`if request.user == profile.user`) before deleting. Only the profile owner can initiate deletion. | ![screenshot](documentation/defensive/no_permission_feedback.jpeg) |
| Availability  | Mentor must be authenticated and published to access availability setup. | Tried manipulationg the url to get to availability page while logged in but not published. | Redirected to home page. | ![screenshot](documentation/defensive/availability_access_for_non_published.jpeg)|
|  | Date fields must be valid. | Submitted availability form with missing date field. | Validation errors shown; slot not created. | ![screenshot](documentation/defensive/form_no_date.jpeg) |
| | Time fields must be valid. | Submitted availability form with missing time field. | Validation errors shown; slot not created. | ![screenshot](documentation/defensive/form_no_time.jpeg) |
| | Time must be set on the hour. | Submitted availability form with invalid time. | Validation errors shown; slot not created. | ![screenshot](documentation/defensive/form_invalid_time.jpeg) |
|  | Time slots must be unique. | Tried to create the same slot on the same date. | Error message shown; timeoverlap slot not saved. | ![screenshot](documentation/defensive/timeoverlap.jpeg)|
|  | Mentors cannot edit/delete another mentor’s slot. | Logged in as Mentor B and accessed Mentor A’s edit slot URL. | Access denied / 404 returned. | ![screenshot](documentation/defensive/edit_availability_404.jpeg) |
| Booking | Visitors can book without authentication. | Booked an available slot as guest user. | Booking created successfully. | ![screenshot](documentation/defensive//booking_confirmation.jpeg)|
|  | Required fields must be completed. | Submitted booking form without name/email. | Validation errors displayed; booking not created. | ![screenshot](documentation/defensive/booking_form_required.jpeg) |
|  | Slots cannot be booked more than once. | Booked a slot then attempted booking same slot again via URL. | Booking prevented; 404 returned. | ![screenshot](documentation/defensive/book_a_slot_404.jpeg)|
| Booking (Mentor View) | Only authenticated mentors can view bookings. | Attempted to access booking details page via url while logged out. | Access denied. 404 returned. | ![screenshot](documentation/defensive//booking_details_404.jpeg)  |
|  | Mentors should only see their own bookings. | Logged in as Mentor A, viewed Mentor B's profile and tried altering the url. | Mentor B's bookings are not accessible. 404 returned. | ![screenshot](documentation/defensive//booking_detail_restriction.jpeg)|
| Admin Access | Standard users must not access admin pages. | Logged in as authnticated non-superuser and navigated to `/admin/`. | Access denied / redirected to admin login. | ![screenshot](documentation/defensive/admin_restriction.jpeg) |
| 404 Handling | Invalid URLs should not expose debug information. | Visited non-existent URL. | Custom 404 handling displayed safely. | ![screenshot](documentation/defensive/404_page.jpeg)|


## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a visitor |  I can scroll through a feed of approved Mentor cards | so that I can quickly find a suitable Mentor.| ![screenshot](documentation/features/paginated_mentor_list.jpeg) |
| As a visitor | I can view a Mentor's detailed profile | so that I can decide whether to book with them.| ![screenshot](documentation/features/detailed_profile.jpeg) |
| As a visitor | I can book an available slot by submitting my details | so that I can schedule a mentoring session.| ![screenshot](documentation/features/booking_form.jpeg) |
| As a mentor | I can create an account  | so that I can apply to be listed on the platform.| ![screenshot](documentation/features/sign_up.jpeg) |
| As a mentor | I can log in and log out | so that I can mange my profile and available slots securely. | ![screenshot](documentation/features/sign_in.jpeg) ![screenshot](documentation/features/sign_out.jpeg) |
| As a mentor | I can create and edit my profile | so that I can offer my mentoring to clients. |![screenshot](documentation/features/profile_setup_form.jpeg) ![screenshot](documentation/features/profile_edit.jpeg) |
| As a mentor | I can alter my profile | so that I can update or delete my offering. | ![screenshot](documentation/features/profile_delete_modal.jpeg) |
| As a mentor | I can add slots that are available on the hour | so that visitors can book time with me. | ![screenshot](documentation/defensive/form_invalid_time.jpeg) |
| As a mentor | I can edit my availability | so that I can correct times or update my schedule. | ![screenshot](documentation/features/manage_availability.jpeg) |
| As a mentor | I can delete an unbooked slot | so that I can remove availability I no longer want to offer. | ![screenshot](documentation/features/manage_availability.jpeg) |
| As a mentor | I can view my upcoming bookings | so that I know who I am meeting and when. | ![screenshot](documentation/features/my_bookings_details.jpeg) |
| As the Platform | I can prevent bookings within 24 hours of the session start | so that Mentors are given enough time to respond to their mentees. | ![screenshot](documentation/userstory_testing/date_of_today.jpeg) ![screenshot](documentation/userstory_testing/existing_slot.jpeg) ![screenshot](documentation/userstory_testing/slot_not_visible_for%20_visitor.jpeg)|
| As the platform | I can prevent the same slot being booked by more than one person | so that schedules stay accurate.| ![screenshot](documentation//userstory_testing/slot_booked.jpeg) ![screenshot](documentation//userstory_testing/slot_hidden.jpeg) |
| As an Admin | I can review and approve mentor profiles | so that only suitable mentors are published. | ![screenshot](documentation/features/admin_control.jpeg) |



