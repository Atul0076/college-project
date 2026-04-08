# EduCore Pro - User Manual

**Version:** 1.0  
**Date:** April 8, 2026  
**System:** Educational Management Portal

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Authentication & Login](#authentication--login)
4. [Administrator Portal](#administrator-portal)
5. [Teacher Portal](#teacher-portal)
6. [Student Portal](#student-portal)
7. [Features Overview](#features-overview)
8. [Demo Accounts](#demo-accounts)
9. [Troubleshooting](#troubleshooting)

---

## Introduction

**EduCore Pro** is a comprehensive educational management system designed to streamline school operations and enhance communication between administrators, teachers, and students. This platform provides role-based access with specialized dashboards and features tailored for each user type.

### Key Features:
- **Role-Based Access Control**: Three distinct portals (Admin, Teacher, Student)
- **Attendance Tracking**: Real-time attendance recording and analytics
- **Grade Management**: Assignment tracking and performance metrics
- **Class Management**: Course organization and capacity planning
- **Student Directory**: Comprehensive student information database
- **Notification System**: Real-time communication and alerts
- **Responsive Design**: Works seamlessly on desktop and tablet devices

---

## Getting Started

### System Requirements:
- Modern web browser (Chrome, Firefox, Safari, Edge)
- JavaScript enabled
- Active internet connection
- No additional software installation needed

### Accessing the System:
1. Open your web browser
2. Navigate to the EduCore Pro login page
3. Enter your credentials (email and password)
4. You will be automatically directed to your role-specific dashboard

---

## Authentication & Login

### Login Page Features:
- **Email Address Field**: Enter your institutional email
- **Password Field**: Enter your secure password
- **Remember Me Option**: Optional; improves convenience for personal devices
- **Demo Credentials Display**: Shows available demo accounts for testing

### Password Requirements:
- Minimum 6 characters
- Can contain letters, numbers, and special characters
- Passwords are securely stored in browser's local storage

### Session Management:
- Sessions are stored locally on your device
- Closing the browser does not automatically log you out
- Use the **Logout** button to end your session
- After logout, you will be redirected to the login page

### Demo Accounts Available:

| Role | Email | Password | Purpose |
|------|-------|----------|---------|
| Super Admin | admin@educore.com | admin123 | Full system access, all features |
| Teacher | teacher1@school.edu | teacher123 | Class and student management |
| Student | ethan.r@school.edu | student123 | Academic tracking and classes |

*Note: Demo accounts are for testing purposes only and contain sample data.*

---

## Administrator Portal

### Access:
- **URL:** dashboard.html
- **Required Role:** Super Admin
- **Authentication:** Role-based, automatic redirect from login

### Dashboard Overview:
The admin dashboard displays:
- Total students enrolled across all classes
- Total active teachers
- Current semester classes in progress
- System statistics and notifications

### Main Menu (Sidebar):

#### 1. **Dashboard** 
- Overview of system health
- Key performance indicators
- Recent activity feed
- Student enrollment trends

#### 2. **Students**
- Complete student directory
- Student profiles with contact information
- Grade and attendance records
- Enrollment status (Active/Inactive)
- Parent contact information

#### 3. **Teachers**
- Teacher roster and assignments
- Subject specializations
- Class schedules and student loads
- Performance ratings
- Years of experience

#### 4. **Classes**
- All active and inactive classes
- Class capacity and enrollment status
- Teacher assignments
- Class schedules and room assignments
- Class code reference

#### 5. **Attendance**
- System-wide attendance reports
- Daily attendance logs
- Class-level attendance trends
- Attendance rate analytics

#### 6. **Settings**
- System configuration options
- User account management
- Administrative preferences
- System maintenance

---

## Teacher Portal

### Access:
- **URL:** teacher-dashboard.html
- **Required Role:** Teacher
- **Authentication:** Role-based, automatic redirect from login

### Dashboard Overview:
Teachers see personalized content including:
- Total classes taught
- Total students across all classes
- Teaching rating
- Years of experience
- Recent activity and submissions

### Main Menu (Sidebar):

#### 1. **Dashboard**
Main teaching hub displaying:
- Quick statistics (classes taught, student count, rating)
- Class performance cards with enrollment percentages
- Recent student submissions
- Important announcements and alerts

#### 2. **My Classes** (teacher-classes.html)
**Purpose:** Manage and view all classes you teach

**Features:**
- Grid view of all assigned classes
- Class details: Code, Grade Level, Room, Schedule
- Enrollment capacity visualization (progress bar)
- Action buttons: "View Class" and "Edit"

**Class Information Displayed:**
- Class Name
- Class Code (e.g., MATH-401)
- Grade Level
- Room Location
- Schedule (Days and Times)
- Enrollment Status (Current/Maximum Students)

#### 3. **Students** (teacher-students.html)
**Purpose:** Manage and view all students in your classes

**Features:**
- Searchable student directory
- Real-time search filtering (case-insensitive)
- Student avatar with initials
- Complete information for each student

**Columns Displayed:**
| Column | Information |
|--------|-------------|
| Name | Student's full name |
| Grade | Current grade level |
| Email | Institutional email address |
| GPA | Current Grade Point Average |
| Attendance % | Attendance rate percentage |
| Status | Active/Inactive status |
| Action | View student profile link |

**Search Functionality:**
- Type a student's name in the search box
- Results update in real-time
- Case-insensitive matching

#### 4. **Assignments** (teacher-assignments.html)
**Purpose:** Track and manage assignments and submissions

**Features:**
- Grid display of all assignments
- Submission progress tracking
- Due date indicators
- Submission statistics

**Assignment Card Shows:**
- Assignment Title
- Associated Class
- Due Date
- Submission Count (current/total)
- Progress bar (% submitted)
- "View Submissions" button

#### 5. **Attendance** (teacher-attendance.html)
**Purpose:** Record and track student attendance

**Features:**
- Date picker for attendance date
- Class selector dropdown (shows only your classes)
- Individual student attendance status
- Notes field for each student
- Save functionality

**Attendance Options:**
- **Present** (Default) - Student attended class
- **Late** - Student arrived after class started
- **Absent** - Student did not attend

**Workflow:**
1. Select a class from dropdown
2. Choose attendance date (defaults to today)
3. For each student, select their attendance status
4. Add optional notes in the Notes column
5. Click "Save Attendance" to record

---

## Student Portal

### Access:
- **URL:** student-dashboard.html
- **Required Role:** Student
- **Authentication:** Role-based, automatic redirect from login

### Dashboard Overview:
Students see their personalized academic information:
- Current attendance rate
- Active classes list
- Current GPA
- Next scheduled class and teacher

### Main Menu (Sidebar):

#### 1. **Dashboard**
Personal academic hub displaying:
- Quick statistics (attendance %, active classes, GPA)
- Next scheduled class details
- Recent notifications
- Quick action buttons

#### 2. **My Classes** (student-classes.html)
**Purpose:** View all enrolled classes and class details

**Features:**
- All enrolled classes displayed in card format
- Class information cards showing:
  - Class Name
  - Teacher Name
  - Grade Level
  - Room Location
  - Class Schedule (Days and Times)
  - Enrollment Progress Bar

**Card Actions:**
- "View Class" button for detailed class information
- Class status indicator (Active/Paused)

**Information Provided:**
- Complete class roster
- Class schedule and duration
- Teacher contact information
- Class capacity and current enrollment

#### 3. **Grades** (student-grades.html)
**Purpose:** Track academic performance and assignment grades

**Features:**
- Current GPA Display (prominently highlighted)
- Comprehensive grade history
- Performance analysis by subject

**Sections:**

**A. Current GPA**
- Shows overall GPA
- Color-coded for quick reference

**B. All Assessments**
- Complete table of all assignments and tests
- Columns: Assignment Name, Grade (A/B/C), Score (%), Date, Teacher
- Grade badges with color coding:
  - **A** (Green/Teal) - Excellent (90-100%)
  - **B** (Yellow/Amber) - Good (80-89%)
  - **C** (Orange/Coral) - Satisfactory (70-79%)

**C. Performance by Subject**
- Subject name
- Subject average (e.g., "Math Avg: 94%")
- Subject progress bar
- Current performance status

**Grading Scale:**
| Grade | Percentage | Status |
|-------|-----------|--------|
| A | 90-100% | Excellent |
| B | 80-89% | Good |
| C | 70-79% | Satisfactory |
| D | 60-69% | Needs Improvement |
| F | Below 60% | Failing |

#### 4. **Attendance** (student-attendance.html)
**Purpose:** Monitor personal attendance record

**Features:**
- Overall attendance rate (percentage)
- Attendance statistics
- Complete attendance history
- Attendance breakdown by class

**Stat Cards Displayed:**
- **Attendance Rate**: Overall percentage
- **Present Count**: Total days present
- **Absent Count**: Total days absent
- **Late Count**: Total times late

**Attendance History Table:**
- Date of class
- Class Name
- Attendance Status (Present/Late/Absent)
- Time information

**Color Coding:**
- **Present**: Teal/Green
- **Late**: Amber/Yellow
- **Absent**: Coral/Red

**Attendance by Class:**
- Class Name
- Attendance percentage for that specific class
- Visual progress bar showing attendance %

#### 5. **Notifications** (student-notifications.html)
**Purpose:** Receive and manage announcements and alerts

**Features:**
- Unread notification count display
- Notification history
- Read/Unread status tracking
- "Mark All Read" button

**Notification Types:**

| Type | Color | Purpose |
|------|-------|---------|
| Info | Teal | General announcements |
| Warning | Amber | Attendance or grade alerts |
| Alert | Coral | Urgent notices |

**Notification Information:**
- Message content
- Notification type icon
- Timestamp (relative: "2 min ago", "1 hr ago")
- Read status

**Example Notifications:**
- New class assignments
- Attendance below threshold
- Grade posting notifications
- Parent-teacher meeting schedules
- Important policy updates

---

## Features Overview

### Universal Features (All Roles)

#### 1. **User Profile**
- Located in top-right corner of dashboard
- Shows:
  - User name
  - User role
  - User email
  - Avatar/initials
  - Logout button

#### 2. **Navigation Sidebar**
- Permanent sidebar on desktop (hidden on mobile)
- Role-specific menu items
- Quick access to all features
- Active page highlighting
- Responsive design

#### 3. **Responsive Design**
- Optimized for desktop screens
- Works on tablets and mobile devices
- Sidebar collapses on smaller screens
- Touch-friendly buttons and controls

#### 4. **Dark Theme**
- Easy on the eyes for extended use
- Professional appearance
- Color-coded elements for better UX
- Consistent styling across all pages

### Role-Specific Features

#### Admin Features:
- Full system visibility
- All user management
- System-wide analytics
- Settings and configuration

#### Teacher Features:
- Class management
- Student roster access
- Assignment tracking
- Attendance recording

#### Student Features:
- Personal grades and GPA
- Class schedules
- Attendance tracking
- Notification center

---

## Demo Accounts

### Testing the System:

**For Administrators:**
- Email: `admin@educore.com`
- Password: `admin123`
- Access: Full system, all data visible
- Use case: Testing admin features and reports

**For Teachers:**
- Email: `teacher1@school.edu`
- Password: `teacher123`
- Access: Teacher-specific features and student management
- Demo Teacher Name: Mr. James Wilson
- Subject: English
- Classes: 4 classes, 92 students
- Use case: Testing class and assignment management

**For Students:**
- Email: `ethan.r@school.edu`
- Password: `student123`
- Access: Student portal features
- Student Name: Ethan Reynolds
- Grade: 10-A
- GPA: 3.8
- Attendance: 95%
- Use case: Testing grades, attendance, and notifications

### Sample Data Included:
- **10 Students**: Various grades and backgrounds
- **6 Teachers**: Different subjects and experience levels
- **7 Active Classes**: Scheduled with multiple teachers
- **7 Attendance Records**: Recent class attendance logs

---

## User Interface Guide

### Color Scheme:

| Color | Usage | Hex Code |
|-------|-------|----------|
| Navy | Background, text | #0a0f1e |
| Teal | Student portal accent, positive indicators | #14b8a6 |
| Amber | Teacher portal accent, warnings | #f59e0b |
| Coral | Alerts, urgent items | #f43f5e |
| Violet | Secondary accents | #8b5cf6 |
| White | Text, highlights | #ffffff |

### UI Components:

#### Buttons:
- Primary Action: Teal/Amber buttons (role-specific)
- Action Button Text: Clear, concise labels
- Hover State: Brightness increase
- States: Enabled, Disabled, Loading

#### Cards:
- White/Light background
- Shadow effects for depth
- Border radius for modern look
- Padding and spacing for readability

#### Tables:
- Striped rows for easy reading
- Sortable column headers
- Responsive table layout
- Pagination (if applicable)

#### Forms:
- Clear labels
- Input validation
- Error messages
- Submit/Cancel buttons

---

## Troubleshooting

### Common Issues and Solutions:

#### 1. Login Problems

**Issue:** "Cannot log in, page redirects to login"
- **Solution:** Clear browser cookies and cache, try again
- **Verify:** Correct email format (e.g., student@school.edu)
- **Check:** Confirm password is correct (case-sensitive)

**Issue:** "Wrong credentials message"
- **Solution:** Ensure email matches exactly (check for spaces)
- **Solution:** Use demo credentials for testing
- **Contact:** Admin if credentials are incorrect

#### 2. Page Display Issues

**Issue:** "Sidebar not showing or styling looks wrong"
- **Solution:** Refresh the page (Ctrl+F5 or Cmd+Shift+R)
- **Solution:** Clear browser cache and reload
- **Browser:** Try a different browser (Chrome, Firefox, Safari)

**Issue:** "Data not loading or showing outdated information"
- **Solution:** Hard refresh the page
- **Solution:** Clear browser localStorage (see below)
- **Session:** Log out and log back in

#### 3. Session and Storage Issues

**Issue:** "Session expires too quickly"
- **Solution:** Sessions are stored locally and don't auto-expire
- **Use Logout:** Click logout button when leaving the system
- **Security:** Use logout on shared computers

**Clear Browser Storage (for testing):**
1. Open browser Developer Tools (F12)
2. Go to Application/Storage tab
3. Find "localStorage"
4. Remove "edu_auth" and "edu_students" entries
5. Refresh page

#### 4. Attendance/Grade Issues

**Issue:** "Can't save attendance or grades"
- **Solution:** Ensure all required fields are filled
- **Solution:** Refresh and try again
- **Check:** Verify you have the correct role for the action

**Issue:** "Data disappeared after closing browser"
- **Note:** This is expected behavior for demo data
- **Solution:** Data is stored in browser's local storage
- **Persistence:** Log back in with same credentials

#### 5. Navigation Issues

**Issue:** "Can't navigate to class details or student profiles"
- **Solution:** Features with placeholder buttons are for future development
- **Alternative:** Use the main sidebar to navigate
- **Working Features:** See Features Overview section for available functions

### Browser Compatibility:

| Browser | Version | Support |
|---------|---------|---------|
| Chrome | Latest | ✓ Fully Supported |
| Firefox | Latest | ✓ Fully Supported |
| Safari | Latest | ✓ Fully Supported |
| Edge | Latest | ✓ Fully Supported |
| Internet Explorer | 11+ | ✗ Not Supported |

### Device Support:

| Device | Support | Notes |
|--------|---------|-------|
| Desktop | ✓ Full | Optimal experience |
| Laptop | ✓ Full | All features work |
| Tablet | ✓ Partial | Sidebar collapses |
| Mobile | ◐ Limited | Responsive layout |

### Getting Help:

1. **Check the Manual:** Review relevant section above
2. **Try Troubleshooting:** Follow steps for your issue
3. **Clear Cache:** Hard refresh or clear storage
4. **Contact Admin:** For persistent problems
5. **Email Support:** admin@educore.com

---

## Technical Information

### Technology Stack:
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Styling:** Tailwind CSS v3 (via CDN)
- **Icons:** SVG (inline)
- **Storage:** Browser Local Storage
- **Framework:** No external JS frameworks

### Browser Data Storage:
- Sessions stored in `localStorage` under key: `edu_auth`
- Student data: `edu_students`
- Teachers data: `edu_teachers`
- Classes data: `edu_classes`
- Attendance data: `edu_attendance`

### Performance:
- Lightweight, no dependencies
- Fast load times
- Minimal bandwidth usage
- Works offline (read-only after initial load)

---

## Frequently Asked Questions (FAQ)

**Q: Is my data saved permanently?**
A: Data is stored in your browser's local storage. Clearing browser data will remove it. This is development/demo software; production version would use a database.

**Q: Can I access from multiple devices?**
A: Currently, each device has separate storage. Future versions will include cloud sync.

**Q: What if I forget my password?**
A: Use the demo credentials provided to reset. Admin can manage user accounts in production.

**Q: Can students edit their own grades?**
A: No, only teachers and admins can modify grades. Student view is read-only.

**Q: How often is attendance recorded?**
A: Teachers record attendance per class session. 

**Q: Can I print reports?**
A: Use your browser's print function (Ctrl+P or Cmd+P) to print any page.

**Q: Is the system secure?**
A: This is a demo system. Production version would include SSL, encrypted passwords, and secure authentication.

---

## System Updates & Improvements

### Current Version: 1.0

**Implemented Features:**
- ✓ Role-based authentication
- ✓ Student portal with grades and attendance
- ✓ Teacher portal with class and assignment management
- ✓ Admin dashboard
- ✓ Responsive design
- ✓ Dark theme UI

**Planned Features (Future):**
- Cloud-based storage
- Real-time notifications via email
- Mobile app
- Advanced analytics and reporting
- Parent portal
- Integration with external systems

---

## Contact & Support

**System Administrator:**
- Email: admin@educore.com
- Portal: dashboard.html

**Technical Support:**
- For bugs or issues, contact the system administrator
- Include error messages and steps to reproduce

**User Feedback:**
- Feature requests and suggestions welcome
- Help us improve by reporting issues

---

## License & Terms

**EduCore Pro v1.0**
© 2026 EduCore Systems

This manual and the associated software are provided for educational and evaluation purposes. All rights reserved.

For more information or customization, contact the system administrator.

---

**Document Version:** 1.0  
**Last Updated:** April 8, 2026  
**Manual Created For:** EduCore Pro Educational Management System
