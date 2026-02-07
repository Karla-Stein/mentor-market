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
| As a mentor | I can alter my profile | so that I can update or delete my offering. |
| As a mentor | I can add slots that are available on the hour | so that visitors can book time with me. |
| As a mentor | I can edit my availability | so that I can correct times or update my schedule. |
| As a mentor | I can delete an unbooked slot | so that I can remove availability I no longer want to offer. |
| As a mentor | I can view my upcoming bookings | so that I know who I am meeting and when. |
| As the Platform | I can prevent bookings within 24 hours of the session start | so that Mentors are given enough time to respond to their mentees. |
| As an Admin | I can review and approve mentor profiles | so that only suitable mentors are published. |


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



## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | Used where necessary to enhance usability. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |
| [![badge](https://img.shields.io/badge/Gemini-grey?logo=googlegemini&logoColor=#8E75B2)](https://gemini.google.com) | Generating images. |
| [![badge](https://img.shields.io/badge/favicon.io-grey?logo=fi&logoColor=209CEE)](https://favicon.io) | Generating the favicon. |
| [![YouTube](https://img.shields.io/badge/YouTube-grey?logo=youtube&logoColor=red)](https://www.youtube.com/) | Tutorials. |
| [![Medium](https://img.shields.io/badge/Medium-grey?logo=medium&logoColor=black)](https://medium.com) | Articles. |
| [![Lucid](https://img.shields.io/badge/Lucid-ERD-grey?logo=lucid&logoColor=orange)](https://lucid.app) | Planning the initial ERD |
| [![Google Sheets](https://img.shields.io/badge/Google%20Sheets-grey?logo=googlesheets&logoColor=white)](https://www.google.com/sheets/about/) | Refining the ERD |
| [![Mermaid](https://img.shields.io/badge/Mermaid-ERD-grey?logo=mermaid&logoColor=coral)](https://mermaid.live) | Creating an interactive version of the ERD |



## Database Design

### Data Model

The initial database design was planned in advance using Lucid, where a separate Visitor model was defined to reflect future authentication and booking management features.

During development and data flow visualisation, it became clear that for the current MVP scope, visitor authentication was not required. To reduce unnecessary complexity, visitor details were stored directly on the Booking model while keeping the overall structure extensible for the future.

This approach allowed the core booking functionality to remain simple and robust, while preserving a clear upgrade path for introducing authenticated visitor accounts later.


**Database Design Evolution**

| Stage | Tool | Purpose | ERD |
| --- | --- | --- | --- | 
| Initial Planned MVP ERD | [![Lucid](https://img.shields.io/badge/Lucid-ERD-grey?logo=lucid&logoColor=orange)](https://lucid.app) | Created during the planning phase to define core relationships, including a separate Visitor model to support future authentication and account management. | ![screenshot](documentation/erd/erd_lucid.jpeg) |
| Refined MVP ERD | [![Google Sheets](https://img.shields.io/badge/Google%20Sheets-grey?logo=googlesheets&logoColor=green)](https://www.google.com/sheets/about/) | Used to visualise and validate the MVP data model, embedding visitor details within the Booking model to simplify relationships while maintaining future extensibility. | ![screenshot](documentation/erd/erd_sheet.jpeg) |
| Final MVP ERD (Implemented Model Design) | ![Mermaid](https://img.shields.io/badge/Mermaid-ERD-grey?logo=mermaid&logoColor=coral)(https://mermaid.live) | This ERD represents the final MVP database structure, generated with Mermaid to visualise the implemented Django models and confirm the one-to-one relationship between bookings and mentor-specific time slots.  *(for interactivity, see below)*| ![screenshot](documentation/erd/erd_mermaid.jpeg) |




**Interactive ERD (Mermaid)**

```mermaid
erDiagram
    USER ||--|| PROFILE : "has mentor_profile"
    PROFILE ||--o{ TIMESLOT : "defines availability"
    TIMESLOT ||--|| BOOKING : "is booked by"

    PROFILE {
        int id PK
        int user_id FK "OneToOne -> USER"
        string name "unique"
        string slug "unique"
        string featured_image "CloudinaryField"
        string excerpt
        string bio
        string experience
        string specialism
        datetime member_since
        int status "0 Draft | 1 Published"
        datetime updated_on
    }

    TIMESLOT {
        int id PK
        int mentor_id FK "ForeignKey -> PROFILE"
        date date
        time start_time
        time end_time
        int availability_status "0 Open | 1 Booked"
        string unique_together "mentor + date + start_time + end_time"
    }

    BOOKING {
        int id PK
        int time_slot_id FK "OneToOne -> TIMESLOT"
        string visitor_name
        string visitor_email
        string visitor_phone "blank allowed"
        datetime booked_at
    }
``` 


source: [Mermaid](https://mermaid.live/edit#pako:eNqFVNtu4jAQ_RXLrwVEwj0P-9AWVojuggr7skKKHDIEq46d9aVbFvj32rlQoLD1QxTPzJk5c2aSHV6JGHCAQT5SkkiSLjmy59d8-Iz2-3p9v0ez5-lo_DREAVriDVEoBa6FDDMp1pTBEheIKsqBxA4txj-G86fpIkfFsKYcFCKvhDISUUb1tsIdA8tq99PpZPzze46jCkVCvECMojz-vNKuuLpDuUY0RrPJuckokKG1jyY22ZTDQtgHqn_L26sIuKO0pDxBnKRgIw2nfwxc8Stmkv_510C0kRCHNCWJy_TAhIkpJ3I7osDiKxB4W4HM9Cd7RMWV2AwkBb6Cz8wyWFHCqEo_XDHRoKntKIU0skIoeoZ0AiltCStLtIkeJVlrtEcempnIJtrAGd1jMpO51zgU5TQO1ViOg_x6LuUGVZMZCQk04RPYutmU470snj8-TDkXS1_q0L1eOIDHF2ZX9nT9wpPWpxnwvPP7fNmuTKmYeKhFAnoD0qKKFtBdwe3uhIq9HMvjC42q5f5aIgcPFRP66v5WWl-h-koVdeK6Xb7phNQqcdObbQR32xsxwl8QYUz8vbEMxdcZknJ_D7iGE0ljHGhpoGZFkraQveK84SW24jlVyn8CMUy7tA6WEf5biLRCSmGSDQ7WhCl7K3au_EEdrdLKDPJBGK5x0PaaeRIc7PCbvXbbjU7f89ttv-d7Lb9Xw1sc1Ftet9Fv-v5g0G12es1e51DD__KyXsPze32v3W11B61Oq9vza5gYLeZbvipIHd4B-JKW4Q)


