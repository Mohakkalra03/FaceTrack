# FACETRACK

University Face Attendance System

FACETRACK is a desktop ERP-style identity and attendance system for faculty-driven student attendance using face recognition. Faculty controls student registration, timetable management, and attendance sessions. Students get read-only access to profile, timetable, and attendance analytics.

## Features

- Role-based login for admin, faculty, and students
- Admin-managed faculty registration and timetable assignment
- Faculty-controlled attendance sessions for assigned classes only
- Student registration with webcam face sample capture
- Embedding-based student recognition with Euclidean distance matching
- Weekly timetable creation and today-class attendance workflow
- Duplicate attendance prevention
- Faculty reports with CSV export
- Student dashboard with profile, timetable, and attendance percentage
- SQLite persistence and file logging

## Project Structure

```text
FACETRACK/
|-- main.py
|-- setup_database.py
|-- gui/
|   |-- login_window.py
|   |-- faculty_dashboard.py
|   |-- student_dashboard.py
|   |-- register_student.py
|   |-- attendance_page.py
|   |-- timetable_page.py
|-- face_engine/
|   |-- face_capture.py
|   |-- face_encode.py
|   |-- face_recognizer.py
|-- database/
|   |-- db.py
|   |-- models.py
|-- services/
|   |-- attendance_service.py
|   |-- timetable_service.py
|   |-- student_service.py
|   |-- faculty_service.py
|-- utils/
|   |-- config.py
|   |-- helpers.py
|-- data/
|   |-- faces/
|   |-- database.db
|-- requirements.txt
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Optional database bootstrap:

```bash
python setup_database.py
```

4. Run the application:

```bash
python main.py
```

## Default Admin Login

- Username: `admin`
- Password: `admin123`

## Notes

- `face_recognition` is used when available. If it is not installed successfully on the local machine, FACETRACK falls back to a simplified OpenCV-based embedding mode so the application still runs for demonstration and testing.
- Attendance can only be started by faculty after selecting one of today's timetable classes.
- Student accounts cannot create attendance, alter timetable data, or modify institutional records.
