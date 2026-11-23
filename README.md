# Online Smart Face Recognition Attendance Management System

🎓 **BCA 5th Semester College Minor Project**  
Developed with **Python, FastAPI, OpenCV, MySQL, Bootstrap 5 & Chart.js**

---

## 📌 1. Project Overview

The **Online Smart Face Recognition Attendance Management System** is a modern, contactless biometric attendance application engineered for colleges and universities. Traditional attendance mechanisms (roll call books, paper registers, RFID swipe cards) suffer from high time wastage, proxy attendance (buddy punching), and manual calculation errors. 

This system completely eliminates proxy attendance by capturing the student's face via an interactive browser webcam, analyzing facial structures with **OpenCV Computer Vision algorithms**, generating normalized feature embeddings, and logging verified attendance into a **MySQL database** with exact date and timestamps.

---

## 🚀 2. Key Features

### 👨‍💼 A. Admin Portal & Dashboard
- **Secure Authentication:** JWT-based bearer authentication with salted hashing.
- **Real-Time KPIs:** 
  - Total Students Registered
  - Total Present Today
  - Total Absent Today
  - Attendance Success Rate / Percentage
- **Interactive Graphs:**
  - **Daily Attendance Graph:** Bar chart tracking daily attendance over the past 7 days (powered by Chart.js).
  - **Monthly Attendance Graph:** Smooth line/area trend over the past 6 months.
- **Recent Attendance Feed:** Live table showing latest checked-in students with timestamps and verification badges.

### 👥 B. Student Management (Full CRUD)
- **Add Students:** Register new students with Name, Roll Number, Course, Semester, Email, Phone Number, and portal password.
- **Edit & Update:** Modify course, semester, or contact details.
- **Delete Student:** Cascading removal of student data, attendance history, and biometric face profiles.
- **Instant Search & Filter:** Filter by Course, Semester, or search dynamically by Name and Roll Number.
- **Biometric Status Badge:** Visual indicators showing whether a student has enrolled their face biometrics.

### 📸 C. Biometric Face Registration
- **Browser Webcam Feed:** Live user-facing camera stream with interactive visual alignment target brackets.
- **OpenCV Face Detection:** Uses Haar Cascades to locate faces, validates minimum resolution, and isolates cropped facial regions.
- **Feature Extraction & Embedding:** Normalizes lighting using CLAHE (Contrast Limited Adaptive Histogram Equalization) and computes high-dimensional gradient/intensity descriptors.
- **Duplicate Prevention:** Detects if the face being registered already matches an existing registered student, preventing duplicate identities.
- **Secure Storage:** Facial embeddings are serialized and saved to MySQL (`face_embeddings` table) and face photos are stored on disk.

### 🎥 D. Online Face Attendance Kiosk (Core Engine)
- **One-Click Biometric Attendance:**
  1. Student stands in front of the camera kiosk.
  2. The system captures the camera frame.
  3. OpenCV detects the face bounding box.
  4. Feature extraction creates the query embedding vector.
  5. The backend performs cosine similarity matching against registered students.
  6. If matched, checks if already marked today:
     - **If New Today:** Marks status as **Present**, logs exact date & time in MySQL, shows green verification card, and speaks confirmation via Text-to-Speech!
     - **If Already Marked:** Displays yellow warning banner: *"Attendance Already Marked Today."*
     - **If Not Recognized:** Displays red alert: *"Face Not Recognized. Please Register First."*
- **Auto-Scan Mode:** Continuous hands-free scanning every 2.8 seconds for fast walk-by student queues.
- **Spacebar Shortcut:** Press `Spacebar` for instant manual capture.
- **Today's Live Check-in Stream:** Real-time log of students verified during the current session.

### 📊 E. Attendance Reports & Data Export
- Filter records by:
  - Custom Date Range (Start Date to End Date)
  - Quick Presets: *Today, This Week, This Month, All Time*
  - Course (BCA, B.Sc IT, B.Tech CS, MCA) & Semester
  - Student Name or Roll Number
- **One-Click Export:** Download clean `.csv` reports compatible with Microsoft Excel and Google Sheets.
- **Printable Register:** Clean print layout ready for college faculty submissions.

### 🎓 F. Student Personal Dashboard
- Student login using Roll Number and password.
- View personal attendance summary:
  - Total Days Present
  - Total Days Absent
  - Attendance Percentage Progress Meter
- **University 75% Exam Eligibility Warning:** Automatic alert informing students if their attendance falls below 75%.
- Detailed personal attendance log.

---

## 🛠️ 3. Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3, Chart.js, Font Awesome 6, SweetAlert2 |
| **Backend** | Python 3.10+, FastAPI, Uvicorn, Pydantic v2, Python-Multipart |
| **Computer Vision** | OpenCV (`cv2`), Haar Cascade Classifiers, CLAHE Equalization, HOG Descriptors, Cosine Similarity |
| **Database** | MySQL Server / MariaDB (XAMPP), SQLAlchemy ORM, PyMySQL |
| **Security** | PyJWT, SHA-256 with Salt, CORS Middleware |

---

## 📁 4. Project Folder Structure

```
face_attendance_system/
├── frontend/                     # Modern UI Web Client
│   ├── index.html                # Project Landing & Portal Hub
│   ├── login.html                # Admin & Student Login
│   ├── dashboard.html            # Admin Analytics Dashboard
│   ├── students.html             # Student Management (CRUD)
│   ├── registration.html         # Biometric Face Registration
│   ├── attendance.html           # Live Face Attendance Kiosk
│   ├── reports.html              # Attendance Reports & CSV Export
│   ├── student_dashboard.html    # Student Personal Portal
│   ├── css/
│   │   └── style.css             # Premium Blue/Dark Design System
│   └── js/
│       ├── api.js                # Centralized REST API Service
│       └── webcam.js             # Camera & Face Frame Capture Helper
│
├── backend/                      # FastAPI Python Application
│   ├── main.py                   # FastAPI Application Entry & Static Mounts
│   ├── database.py               # MySQL Engine & Smart SQLite Fallback
│   ├── models.py                 # SQLAlchemy Database Models
│   ├── schemas.py                # Pydantic Request/Response Models
│   ├── auth.py                   # JWT Auth & Security Utilities
│   ├── requirements.txt          # Python Package Dependencies
│   ├── routes/
│   │   ├── auth.py               # Authentication Routes
│   │   ├── students.py           # Student Management Routes
│   │   ├── attendance.py         # Biometric Attendance Pipeline
│   │   └── reports.py            # Reports & Chart Analytics Routes
│   ├── face_recognition/
│   │   ├── __init__.py
│   │   ├── detection.py          # OpenCV Face Detection
│   │   ├── encoding.py           # CLAHE & Feature Vector Extraction
│   │   └── recognition.py        # Cosine Similarity Matching
│   └── uploads/                  # Uploaded Biometrics Storage
│       ├── faces/                # Enrolled Student Face Snapshots
│       └── snapshots/            # Attendance Check-in Proof Snapshots
│
├── database/
│   └── schema.sql                # Complete MySQL Database Schema Script
│
├── run.py                        # Python One-Click System Launcher
├── start_system.bat              # Windows 11 Batch Launcher
├── .env                          # Local Environment Configuration
├── .env.example                  # Environment Template
└── README.md                     # Documentation
```

---

## 🗄️ 5. Database Schema & Architecture

The database is named `face_attendance_db` and contains 5 interconnected tables:

1. **`admins`**: Stores administrative credentials, hashed passwords, and contact info.
2. **`students`**: Stores student profiles (Roll Number, Name, Course, Semester, Email, Phone, Photo Path).
3. **`face_embeddings`**: Stores 1D normalized biometric feature vectors serialized as JSON linked to `student_id`.
4. **`attendance`**: Stores attendance logs (`student_id`, `date`, `time`, `status`, `confidence_score`, `snapshot_path`). Enforces unique constraint `(student_id, date)` so students can only mark attendance once per day!
5. **`users`**: Login credentials table connecting roles (`Admin`, `Student`) with hashed passwords.

---

## ⚙️ 6. Installation & Setup Guide (Windows 11)

### Step 1: Clone / Navigate to Project Directory
Open PowerShell or Command Prompt:
```powershell
cd "c:\Users\Arman Mishra\OneDrive\Desktop\AI notes\face_attendance_system"
```

### Step 2: Install Python Dependencies
Run:
```powershell
pip install -r backend/requirements.txt
```

### Step 3: MySQL Database Setup (Optional but Recommended)
1. Open **XAMPP Control Panel** and start **Apache** and **MySQL**.
2. Open your browser and go to `http://localhost/phpmyadmin`.
3. Click **New** on the left sidebar, name the database `face_attendance_db`, and click **Create**.
4. Click on `face_attendance_db`, go to the **Import** tab, choose the file `database/schema.sql`, and click **Import**.

> 💡 **Smart Automatic Fallback Feature:** If MySQL or XAMPP is not running, the application **automatically operates on a built-in local SQLite database (`face_attendance.db`)**, ensuring zero crashes during college demonstrations! When you start MySQL, it connects to MySQL automatically.

### Step 4: Configure Environment Variables
Verify `.env` in the `face_attendance_system/` root folder:
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=face_attendance_db
SECRET_KEY=bca_smart_face_attendance_secret_key_2026_super_secure!
FACE_MATCH_THRESHOLD=0.70
```

### Step 5: Start the System
You can start the project in either of two ways:

#### Option A: Double-Click Launcher
Double-click `start_system.bat` in the project folder.

#### Option B: Terminal Command
```powershell
python run.py
```

The system will start FastAPI on `http://127.0.0.1:8000` and automatically open your default web browser!

---

## 🔑 7. Default Credentials for Testing

| Role | Username / Identifier | Password | Access Level |
| :--- | :--- | :--- | :--- |
| **System Admin** | `admin` | `admin123` | Full Admin Dashboard, Student CRUD, Reports, Enrollment |
| **Sample BCA Student** | `BCA2026001` | `student123` | Student Personal Portal & Attendance History |

*(You can also click the quick **"Demo: admin / admin123"** helper pill on the login page to auto-fill credentials instantly!)*

---

## 🧪 8. College Viva & Demonstration Workflow

For your BCA minor project presentation to external examiners, follow this 4-step sequence:

1. **Step 1 - Admin Login & Student Creation:**
   - Log in at `http://127.0.0.1:8000/login` with `admin` / `admin123`.
   - Go to **Student Management**, click **Add New Student**, and enter student details (e.g. Roll: `BCA2026002`, Name: `Your Name`, Course: `BCA`, Semester: `5th Semester`).
2. **Step 2 - Face Biometric Enrollment:**
   - Navigate to **Face Registration**.
   - Select the newly created student.
   - Look into the webcam and click **Capture & Enroll Face**.
   - Show the examiner how the face crop and high-dimensional biometric descriptor are generated and saved.
3. **Step 3 - Live Attendance Verification:**
   - Open **Take Face Attendance** (`attendance.html`).
   - Click **Scan Face & Mark Attendance** (or press Spacebar).
   - The system detects your face, matches it, marks attendance with date and exact time, speaks the voice confirmation, and logs the entry to MySQL!
   - Scan your face a second time to demonstrate **Duplicate Attendance Prevention**: The system will display *"Attendance Already Marked Today."*
4. **Step 4 - Reports & Analytics:**
   - Go to **Attendance Reports**.
   - Show the filtered attendance register.
   - Click **Export to CSV / Excel** to demonstrate instant spreadsheet export.

---

## 👨‍🎓 Project Credits

- **Project:** Online Smart Face Recognition Attendance Management System
- **Qualification:** Bachelor of Computer Applications (BCA) - 5th Semester Minor Project
- **Engineered by:** Antigravity AI & Senior Full-Stack Engineering Team
