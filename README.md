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



 