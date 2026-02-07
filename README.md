# [mentor-market](https://my-mentor-market-e1c13c4d04df.herokuapp.com)

Developer: Karla Steinbrink ([Karla-Stein](https://www.github.com/Karla-Stein))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Karla-Stein/mentor-market)](https://www.github.com/Karla-Stein/mentor-market/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Karla-Stein/mentor-market)](https://www.github.com/Karla-Stein/mentor-market/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Karla-Stein/mentor-market)](https://www.github.com/Karla-Stein/mentor-market)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://my-mentor-market-e1c13c4d04df.herokuapp.com)

PROJECT INTRODUCTION AND RATIONALE

The idea for Mentor Market was inspired by a real challenge I experienced during my web development course. Partway through the programme, structured mentor support was revoked, leaving many students without direct guidance at a critical stage of learning.

This highlighted how important accessible mentorship is, not only for technical support, but also for confidence, motivation and direction. As a learner transitioning into tech, I wanted to explore how a simple, structured platform could help connect students with experienced developers who are willing to share their knowledge.

Mentor Market was built as a practical learning project to apply real-world development concepts such as authentication, user roles, relational databases, form handling and booking logic. The project reflects both my technical progress and the personal experience that shaped its purpose.

**Site Mockups**

![screenshot](documentation/mockup.jpg)

source: [mentor-market amiresponsive](https://ui.dev/amiresponsive?url=https://my-mentor-market-e1c13c4d04df.herokuapp.com)


## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- To provide mentors with a simple and professional platform to showcase their skills, manage their availability and accept bookings.
- To offer users and visitors an intuitive way to discover mentors, explore their profiles and book available time slots.
- To lay the foundation for future mentor/visitor interaction service through messaging. 


**Primary User Needs**
- Mentors need a simple way to create a professional profile, manage their availability and control which time slots they are offering.
- Visitors need a clear and intuitive way to browse mentor profiles, view available time slots and book a session without needing to create an account.
- The Platform owner needs a structured system that allows for safe data handling, moderation and future expansions.

**Business Goals**
- Create a trusted platform that connects aspiring developers with experienced coding mentors.
- Enable mentors to showcase their expertise and offer bookable 1:1 guidance.
- Provide visitors with a simple way to find and book support.
- Build a scalable foundation that can later support messaging, visitor accounts and long-term mentor–mentee relationships.


#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Public mentor profiles with grouped by date availability display.
- About section that explains the process.
- Mentor profile management (create, read, update, delete and submit for approval).
- Mentor availability management (set, edit, and delete time slots).
- Access control for mentors (login required for profile and availability management).
- Visitor booking system for available mentor time slots.
- Booking confirmation feedback for visitors.
- Booking tab for Mentors to view all received bookings.
- Custom 404 handling for broken links.
- Responsive design across desktop, tablet and mobile devices.


#### 3. Structure

**Information Architecture**

 ***Navigation Menu***:
 - Home (mentor listings)
 - About
 - Login / Register (for Mentors)
 - My Profile (mentors only)
 - My Availability (mentors only)
 - My Bookings (mentors only)
 - Logout (when authenticated)

 ***Hierarchy***:
 - Mentor cards are displayed prominently on the homepage.
 - Each mentor card links to a detailed profile page.
 - Available time slots are shown clearly within each mentor profile.
 - Booking call-to-action guides visitors to book a session.
 - Mentor management features through a protected navigation area.



 **User Flow**

 ***For Mentors***
 1. Mentor visits site:
   - Sign up
   - Creates Profile
   - Waits for approval
 2.	Upon approval:
   - Mentors can manage their profile and availability
 3.	Mentors view their bookings:
   - See all booked sessions ordered by date
   - Access visitor details for each booking
   - Manually needs to contact his Mentee

***For Visitor***
 1.	Visitors browse mentors:
   - View mentor cards on the homepage
   - Click a profile to read about the mentor and see available time slots
 2.	Visitors book a session:
   - Select an available time slot
   - Enter name, email, and (optional) phone number
   - Submit booking request
 3.	System confirms the booking:
   - The slot is marked as booked
   - A success message is shown to the visitor
   - Needs to wait for the Mentor to contact them


#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)


#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)



### Colour Scheme

I used [figma.com](https://www.figma.com/) to generate my color palette.

![screenshot](documentation/colour_palette/colourscheme.jpeg) 


### Typography

- [Zalando Sans Expanded](https://fonts.google.com/specimen/Montserrat) was used for the title in Navbar
- [Manrope](https://fonts.google.com/specimen/Lato) was used for main body text.
- [Anton](https://fonts.google.com/specimen/Lato) was used for the hero section.
- [Font Awesome](https://fontawesome.com) icons was used for the GitHub icon in the footer.


## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/wireframes/home_phone.jpeg) | ![screenshot](documentation/wireframes/home-tablet.jpeg) | ![screenshot](documentation/wireframes/home_desktop.jpeg) |
| Profile Detail | ![screenshot](documentation/wireframes/profile_detail_home.jpeg) | ![screenshot](documentation/wireframes/profile_detail_tablet.jpeg) | ![screenshot](documentation/wireframes/profile_detail_desktop.jpeg) |
| My Availability | ![screenshot](documentation/wireframes/availability_phone.jpeg) | ![screenshot](documentation/wireframes/availability_tablet.jpeg) | ![screenshot](documentation/wireframes/availability_desktop.jpeg) |
| Profile Set Up / Edit | ![screenshot](documentation/wireframes/setup_edit_phone.jpeg) | ![screenshot](documentation/wireframes/setup_edit_tablet.jpeg) | ![screenshot](documentation/wireframes/setup_edit_desktop.jpeg) |
| My Bookings | ![screenshot](documentation/wireframes/my_bookings_phone.jpeg) | ![screenshot](documentation/wireframes/my_bookings_tablet.jpeg) | ![screenshot](documentation/wireframes/my_bookings_desktop.jpeg) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |




 ## User Stories

 | Target | Expectation | Outcome |
| --- | --- | --- |
| As a visitor |  I can scroll through a feed of approved Mentor cards | so that I can quickly find a suitable Mentor.|
| As a visitor | I can view a Mentor's detailed profile | so that I can decide whether to book with them.|
| As a visitor | I can book an available slot by submitting my details | so that I can schedule a mentoring session.|
| As the platform | I can prevent the same slot being booked by more than one person | so that schedules stay accurate.|
| As a mentor | I can create an account  | so that I can apply to be listed on the platform.|
| As a mentor | I can log in and log out | so that I can mange my profile and available slots securely. |
| As a mentor | I can create and edit my profile | so that I can offer my mentoring to clients. |
| As a mentor |  I can alter my profile | so that I can update or delete my offering. |
| As a mentor | I can add slots that are available on the hour | so that visitors can book time with me. |
| As a mentor | I can edit my availability | so that I can correct times or update my schedule. |
| As a mentor | I can delete an unbooked slot | so that I can remove availability I no longer want to offer. |
| As a mentor | I can view my upcoming bookings | so that I know who I am meeting and when. |


## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Sign Up | Authentication is handled by allauth, allowing Mentors to register accounts. | ![screenshot](documentation/features/sign_up.jpeg) |
| Sign in | Authentication is handled by allauth, allowing Mentors to log in to their existing accounts. | ![screenshot](documentation/features/sign_in.jpeg) |
| Sign out | Authentication is handled by allauth, allowing Mentors to log out of their accounts. | ![screenshot](documentation/features/sign_out.jpeg) |
| Paginated Mentor List | The homepage displays Mentor cards in pages with 8 cards per page | ![screenshot](documentation/features/paginated_mentor_list.jpeg) |
| Mentor card | Mentor cards with information including image, name and a brief excerpt of their offering. | ![screenshot](documentation/features/mentor_card.jpeg) |
| Detailed Profile | Upon clicking the 'go to profile' cta user are taken to a page that displays detailed information such as bio, skills and experience. | ![screenshot](documentation/features/detailed_profile.jpeg) |
| Edit and delete profile | Authenticated mentors can edit and delete their own profile. | ![screenshot](documentation/features/edit_delete_features.jpeg) |
| Delete profile modal | When deleting their profile autheticated Mentors are prompted a modal to confirm their choice. | ![screenshot](documentation/features/profile_delete_modal.jpeg) |
| Edit profile | The edit profile button redirects to the prepopulated profile form | ![screenshot](documentation/features/profile_edit.jpeg) |
| Set availability | Authenticated mentors can set their available dates, session start and session end times. | ![screenshot](documentation/features/set_availability.jpeg) |
| Date picker | Mentors can choose their date on a date picker widget for ease of use. | ![screenshot](documentation/features/date_widget.jpeg) |
| Time hint | Mentors can schedule sessions on the hour. | ![screenshot](documentation/features/time_hint.jpeg) |
| Manage availability cta| A section that clearly communicates where authenticated Mentors can manage their availability | ![screenshot](documentation/features/manage_availability_cta.jpeg) |
| List of slots grouped by date | Mentors can choose which slot of a certain date they would like to edit or delete. | ![screenshot](documentation/features/slot_list.jpeg) |
| Edit or delete availability | Upon choosing which slot to alter, the 'Set your Availability" form prepopulates with the chosen slot, giving the mentor the option to update or delete the slot. | ![screenshot](documentation/features/manage_availability.jpeg) |
| Delete availability modal | When deleting the chosen slot Mentors are prompted a modal to confirm their choice. | ![screenshot](documentation/features/delete_slot_modal.jpeg) |
| No bookings feedback | A message to the authenticated mentor that there are no bookings at the current time.| ![screenshot](documentation/features/feeback_no_bookings.jpeg) |
| List of bookings | All bookings linked to authenticated mentor are listed and ordered by date to be viewed. | ![screenshot](documentation/features/my_bookings_list.jpeg) |
| Booking details | Every listed booking is a dropdown that lists booking details such as name, email, start and endtime of the session as well as a timeframe by which the Mentee needs to be contacted. | ![screenshot](documentation/features/my_bookings_details.jpeg) |
| Book a slot | Not authenticated visitor can choose a timeslot on the detailed profile page of the chosen Mentor.| ![screenshot](documentation/features/slot_choice.jpeg) |
| Booking form | A form for not authenticated visitor to enter their name, email and optional their contact number to reserve a slot. | ![screenshot](documentation/features/booking_form.jpeg) |
| Booking confirmation message | After booking, the not authenticated user is redirected to the homepage that displays a confirmation message.  | ![screenshot](documentation/features/booking_message.jpeg) |


### Future Features

- **Booking Cancellation by Mentors**:
 Enable mentors to cancel an existing booking when schedule changes occur. This feature would allow mentors to manage their availability more effectively and handle adjustments while keeping bookings accurate and up to date.
- **Recurring Availability Setup**: 
Enable mentors to define recurring weekly or monthly availability, allowing the system to automatically generate time slots for a selected period. This would reduce manual setup and ensure availability is displayed in a clear order.
- **Booking Confirmation Toggle**:
 Allow mentors to manually confirm a booking via toggle. Once confirmed, the booking status updates accordingly.
- **Reopen Cancelled Bookings**: 
Allow mentors to reopen previously cancelled bookings, automatically resetting the slot’s availability status to 'open'. This would make the time slot visible again on the public mentor profile, enabling new visitors to book the session.
- **Visitor Account Registration**: 
Enable visitors to sign up using Django authentication so they can manage their bookings and access a personal booking history.
- **Visitor Login & Logout**: 
Allow visitors to securely log in and log out using Django authentication so they can access and manage their bookings.
- **Messaging System**: 
Enable logged-in users to communicate directly with mentors or students through an in-platform messaging tab, allowing conversations to be managed and revisited in one central place.
- **Automated Booking Confirmation Emails**: 
Automatically send a confirmation email to the visitor when a booking is confirmed. This ensures clear communication and provides students with written confirmation of their scheduled session.

