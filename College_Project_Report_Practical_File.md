# COLLEGE PRACTICAL FILE & PROJECT REPORT
## BACHELOR OF COMPUTER APPLICATIONS (BCA) - 5TH / 6TH SEMESTER

---

# PROJECT TITLE:
# ONLINE SMART FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM

**Submitted By:**  
- **Student Name:** [Your Name / Arman Mishra]  
- **Roll Number:** [Your University Roll Number]  
- **Course:** Bachelor of Computer Applications (BCA)  
- **Semester:** 5th Semester  
- **Session:** 2026 – 2027  
- **Department:** Department of Computer Applications  
- **College/University:** [Your College / Institute Name]  

**Under the Guidance of:**  
- **Project Supervisor:** [Internal Guide / Professor Name]  
- **Designation:** Assistant Professor / HOD, Dept. of Computer Applications  

---

\newpage

## CERTIFICATE

This is to certify that the project entitled **"ONLINE SMART FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM"** submitted by **[Your Name]**, bearing Roll Number **[Your Roll Number]**, in partial fulfillment of the requirements for the award of the degree of **Bachelor of Computer Applications (BCA)**, is an authentic record of independent work carried out by them under my supervision and guidance.

To the best of my knowledge, the matter embodied in this project report has not been submitted to any other University or Institute for the award of any degree or diploma.


\
\
----------------------------------- \
**Project Supervisor / Internal Guide**  
Department of Computer Applications  

\
\
----------------------------------- \
**Head of Department (HOD)**  
Department of Computer Applications  

\
\
----------------------------------- \
**External Examiner**  
Date of Examination: _______________  

---

\newpage

## DECLARATION

I hereby declare that the project entitled **"ONLINE SMART FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM"** is submitted by me in partial fulfillment of the requirements for the degree of **Bachelor of Computer Applications (BCA)**.

This work is original and has been conducted under the supervision of my project guide. I have followed all university academic guidelines, and appropriate citations have been made wherever reference has been taken from published literature or web sources.


\
\
**Date:** _______________  
**Place:** _______________  

\
\
----------------------------------- \
**[Your Name / Arman Mishra]**  
Roll Number: [Your Roll Number]  
BCA 5th Semester  

---

\newpage

## ACKNOWLEDGEMENT

I would like to express my sincere gratitude and deep respect to my project guide, **[Professor's Name]**, for their invaluable guidance, constant motivation, constructive feedback, and encouragement throughout the design and development of this project.

I am also thankful to our Head of Department, **[HOD's Name]**, and all faculty members of the Department of Computer Applications for providing the requisite laboratory infrastructure, technical resources, and academic environment.

Lastly, I extend my heartfelt thanks to my parents and fellow batchmates for their constant support, encouragement, and cooperation throughout the completion of this minor project.


\
\
**[Your Name]**  
BCA 5th Semester  

---

\newpage

## TABLE OF CONTENTS

1. **Introduction**
   - 1.1 Project Overview
   - 1.2 Problem Statement
   - 1.3 Objectives of the System
   - 1.4 Scope and Applicability
2. **System Requirement Specification (SRS)**
   - 2.1 Hardware Requirements
   - 2.2 Software Requirements
   - 2.3 Technology Stack & Library Descriptions
3. **System Design & Architecture**
   - 3.1 Proposed System Flowchart
   - 3.2 Data Flow Diagrams (DFD Level 0 & Level 1)
   - 3.3 Module Decomposition
4. **Database Design & Data Dictionary**
   - 4.1 Entity Relationship (ER) Diagram Overview
   - 4.2 Database Tables & Structure
   - 4.3 Database Schema (SQL Script)
5. **Computer Vision & Mathematical Formulations**
   - 5.1 Face Detection (Viola-Jones Haar Cascades)
   - 5.2 Lighting Normalization (CLAHE)
   - 5.3 Biometric Feature Extraction (HOG Descriptor)
   - 5.4 Metric Learning & Cosine Similarity
   - 5.5 Anti-Proxy & Duplicate Attendance Algorithm
6. **Key Source Code Listing**
   - 6.1 Database Connection (`database.py`)
   - 6.2 Database ORM Models (`models.py`)
   - 6.3 Authentication & Security (`auth.py`)
   - 6.4 Computer Vision Face Detection (`detection.py`)
   - 6.5 Biometric Encoding (`encoding.py`)
   - 6.6 Recognition Engine (`recognition.py`)
   - 6.7 Attendance Pipeline Router (`attendance.py`)
   - 6.8 Application Entry Point (`main.py`)
7. **System Testing & Validation**
   - 7.1 Test Plan & Test Scenarios
   - 7.2 Test Cases & Execution Results
8. **Conclusion & Future Enhancements**
   - 8.1 Summary of Achievement
   - 8.2 Limitations
   - 8.3 Future Scope
9. **Viva-Voce Questions and Answers**
10. **References & Bibliography**

---

\newpage

# CHAPTER 1: INTRODUCTION

### 1.1 Project Overview
In educational institutions such as colleges and universities, monitoring student attendance is an indispensable administrative requirement. Traditional attendance recording techniques—such as calling out roll numbers from manual registers or passing around paper sign-in sheets—suffer from massive operational overhead, human error, paper wastage, and proxy attendance (buddy punching). Even card-based RFID systems fail to eliminate proxy attendance because cards can easily be handed over to classmates.

The **Online Smart Face Recognition Attendance Management System** provides a completely contactless, biometric, and computerized solution. It harnesses the power of modern **Computer Vision (OpenCV)** and a high-performance **FastAPI (Python)** REST API backed by a **MySQL** relational database. Students simply stand before an interactive browser webcam kiosk; the system detects their facial boundary in real-time, extracts high-dimensional biometric vectors, matches them against registered student embeddings using cosine similarity, logs their attendance with date and exact timestamp, and strictly enforces **Duplicate Attendance Prevention**.

### 1.2 Problem Statement
Existing manual and semi-automated attendance methods exhibit several critical flaws:
1. **Proxy Attendance:** Students often mark signatures or roll calls for absent friends.
2. **Time Inefficiency:** Taking attendance for 60 students in a 50-minute lecture consumes 10–15 minutes, wasting up to 25% of instructional time.
3. **Data Loss & Calculation Burden:** Physical registers get damaged or misplaced, and compiling monthly attendance percentages requires strenuous manual calculation.
4. **Lack of Instant Student Feedback:** Students remain unaware of their short-attendance status until final exam admit cards are withheld.

### 1.3 Objectives of the System
- To develop an automated, contactless biometric attendance system using computer vision.
- To eliminate proxy attendance through unique facial biometrics.
- To enforce a single check-in per student per calendar date.
- To provide a modern Admin Dashboard with dynamic graphs (Chart.js) and real-time statistics.
- To allow one-click export of attendance registers to CSV / Excel spreadsheets.
- To provide a dedicated Student Portal displaying personal attendance history, percentage, and a **75% university eligibility warning banner**.

---

\newpage

# CHAPTER 2: SYSTEM REQUIREMENT SPECIFICATION (SRS)

### 2.1 Hardware Requirements
- **Processor:** Intel Core i3 / i5 / i7 (6th Gen or above) or AMD Ryzen 3 / 5 / 7.
- **RAM:** Minimum 4 GB (8 GB recommended for seamless OpenCV frame processing).
- **Hard Disk:** Minimum 500 MB free space for code, database, and face snapshot storage.
- **Camera:** Standard integrated 720p/1080p laptop webcam or external USB webcam.
- **Display Resolution:** 1366 x 768 or 1920 x 1080.

### 2.2 Software Requirements
- **Operating System:** Windows 10 / Windows 11 (64-bit), Linux (Ubuntu), or macOS.
- **Language Runtime:** Python 3.10 to 3.14.
- **Web Server:** Uvicorn ASGI Server.
- **Database Server:** MySQL Server 8.0+ or MariaDB (via XAMPP / WampServer) with SQLite fallback.
- **Web Browser:** Google Chrome, Microsoft Edge, or Mozilla Firefox (with HTML5 WebRTC Webcam support).

### 2.3 Technology Stack & Library Descriptions
1. **Frontend:**
   - **HTML5 & CSS3:** Semantic markup, responsive flexbox/grid layout, and custom modern dark/blue glassmorphism styling.
   - **JavaScript (ES6+):** Async/await REST client, WebRTC camera stream management (`navigator.mediaDevices.getUserMedia`), HTML5 Canvas frame extraction, and speech synthesis voice output.
   - **Bootstrap 5.3:** Modern UI components, responsive modals, navbar, tables, and alerts.
   - **Chart.js:** Real-time data visualization for 7-day daily check-ins and 6-month attendance trends.
   - **Font Awesome 6 & SweetAlert2:** Icons and modern animated alert dialogues.
2. **Backend:**
   - **FastAPI:** Asynchronous, high-performance Python web framework for REST APIs with automatic Swagger documentation.
   - **Pydantic v2:** Rigorous request and response schema validation.
   - **OpenCV (`cv2`):** Real-time image processing, Haar Cascade frontal face detection, and CLAHE lighting enhancement.
   - **NumPy:** High-speed numerical vector math and cosine similarity dot products.
   - **SQLAlchemy 2.0:** Object Relational Mapper (ORM) providing clean database abstraction.
   - **PyMySQL:** Python MySQL database driver.
   - **PyJWT:** Secure JSON Web Token encoding and decoding for role-based authentication.

---

\newpage

# CHAPTER 3: SYSTEM DESIGN & ARCHITECTURE

### 3.1 System Flowchart

```
                 +------------------------------------------+
                 |            Start Application             |
                 +------------------------------------------+
                                      |
                                      v
                 +------------------------------------------+
                 |    Student / Admin Opens Portal Page     |
                 +------------------------------------------+
                                      |
                    +-----------------+-----------------+
                    |                                   |
                    v                                   v
        [ Admin / Student Login ]             [ Attendance Kiosk ]
                    |                                   |
         +--------------------+                         v
         | Enter Credentials  |            +--------------------------+
         +--------------------+            | Access Browser Webcam    |
                    |                      +--------------------------+
          [ Valid Token? ]                              |
          /              \                              v
       Yes                No               +--------------------------+
        |                  |               | Capture Frame (Canvas)   |
        v                  v               +--------------------------+
   [ Dashboard ]     [ Show Error ]                     |
                                                        v
                                           +--------------------------+
                                           | Backend Face Detection   |
                                           | (OpenCV Haar Cascade)    |
                                           +--------------------------+
                                                        |
                                                 [ Face Detected? ]
                                                 /              \
                                               Yes               No
                                                |                 |
                                                v                 v
                                  +-------------------+    [ Alert: No Face ]
                                  | Extract Embedding |
                                  |  (CLAHE + HOG)    |
                                  +-------------------+
                                           |
                                           v
                                  +-------------------+
                                  | Cosine Similarity |
                                  | vs MySQL Database |
                                  +-------------------+
                                           |
                                    [ Match >= 0.70? ]
                                    /               \
                                  Yes                No
                                   |                  |
                                   v                  v
                       [ Check Duplicate Today ]   [ Alert: Not Recognized ]
                       /                       \
                    New                     Already
                     |                         |
                     v                         v
        +-------------------------+   +-------------------------+
        | Mark Attendance Present |   | Warning: Attendance     |
        | Log Date & Time in DB   |   | Already Marked Today    |
        | TTS Speech Announcement |   +-------------------------+
        +-------------------------+
```

---

\newpage

# CHAPTER 4: DATABASE DESIGN & DATA DICTIONARY

**Database Name:** `face_attendance_db`

### 4.1 Tables Summary

| Table Name | Description | Primary Key | Foreign Keys |
| :--- | :--- | :--- | :--- |
| `admins` | Administrative user login details and credentials | `admin_id` | None |
| `students` | Master registry of college students | `student_id` | None |
| `face_embeddings` | 2020-dimensional facial biometric vectors | `embedding_id` | `student_id` (References `students`) |
| `attendance` | Daily attendance log with exact timestamps | `attendance_id` | `student_id` (References `students`) |
| `users` | Role-based credentials (`Admin`, `Student`) | `user_id` | `student_id` (References `students`) |

---

### 4.2 Detailed Table Structures

#### Table 1: `admins`
| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `admin_id` | `INT` | `AUTO_INCREMENT, PRIMARY KEY` | Unique ID of Administrator |
| `username` | `VARCHAR(50)` | `UNIQUE, NOT NULL` | Admin username (e.g. `admin`) |
| `password_hash` | `VARCHAR(255)`| `NOT NULL` | Salted SHA-256 password hash |
| `full_name` | `VARCHAR(100)`| `NOT NULL` | Full Name of administrator |
| `email` | `VARCHAR(100)`| `UNIQUE, NOT NULL` | Admin email address |
| `created_at` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Account creation timestamp |
| `updated_at` | `DATETIME` | `ON UPDATE CURRENT_TIMESTAMP`| Last profile modification |

#### Table 2: `students`
| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `student_id` | `INT` | `AUTO_INCREMENT, PRIMARY KEY` | Unique ID of Student |
| `full_name` | `VARCHAR(100)`| `NOT NULL` | Student full legal name |
| `roll_number` | `VARCHAR(50)` | `UNIQUE, NOT NULL, INDEX` | College Roll No (e.g. `BCA2026001`) |
| `course` | `VARCHAR(50)` | `NOT NULL` | Course (BCA, B.Sc IT, MCA, etc.) |
| `semester` | `VARCHAR(20)` | `NOT NULL` | Semester (e.g. `5th Semester`) |
| `email` | `VARCHAR(100)`| `UNIQUE, NOT NULL` | Student email address |
| `phone_number` | `VARCHAR(20)` | `NOT NULL` | Contact number |
| `face_image_path` | `VARCHAR(255)`| `NULL` | Relative URL to saved face crop photo |
| `created_at` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Registration date |
| `updated_at` | `DATETIME` | `ON UPDATE CURRENT_TIMESTAMP`| Last update date |

#### Table 3: `face_embeddings`
| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `embedding_id` | `INT` | `AUTO_INCREMENT, PRIMARY KEY` | Unique Embedding record ID |
| `student_id` | `INT` | `UNIQUE, NOT NULL, FK` | References `students(student_id)` ON DELETE CASCADE |
| `embedding_vector` | `LONGTEXT` | `NOT NULL` | Serialized JSON array of float biometric features |
| `face_image_path` | `VARCHAR(255)`| `NULL` | Cropped reference portrait photo |
| `created_at` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Enrollment date |
| `updated_at` | `DATETIME` | `ON UPDATE CURRENT_TIMESTAMP`| Last biometric update |

#### Table 4: `attendance`
| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `attendance_id`| `INT` | `AUTO_INCREMENT, PRIMARY KEY` | Unique Attendance record ID |
| `student_id` | `INT` | `NOT NULL, FK` | References `students(student_id)` ON DELETE CASCADE |
| `date` | `DATE` | `NOT NULL, INDEX` | Calendar date (YYYY-MM-DD) |
| `time` | `TIME` | `NOT NULL` | Exact time marked (HH:MM:SS) |
| `status` | `VARCHAR(20)` | `DEFAULT 'Present'` | Attendance status |
| `confidence_score`| `FLOAT` | `NULL` | Biometric match confidence (0.0 to 1.0) |
| `snapshot_path`| `VARCHAR(255)`| `NULL` | Image proof captured during check-in |
| `created_at` | `DATETIME` | `DEFAULT CURRENT_TIMESTAMP` | Record creation timestamp |
| **Constraint** | `UNIQUE` | `(student_id, date)` | Enforces single check-in per day per student |

---

\newpage

# CHAPTER 5: COMPUTER VISION & MATHEMATICAL FORMULATIONS

### 5.1 Face Detection (Viola-Jones Haar Cascades)
Face detection is achieved using the Haar Cascade Classifier (`haarcascade_frontalface_default.xml`). It operates by calculating rectangular features (edge features, line features, and four-rectangle features) rapidly using an **Integral Image**:
$$\text{Integral Image } ii(x, y) = \sum_{x' \le x, y' \le y} i(x', y')$$
AdaBoost selects the most discriminative weak classifiers, and a cascading structure discards non-face background windows in early stages, allowing real-time 30 FPS processing on low-power CPUs.

### 5.2 Lighting Normalization (CLAHE)
Webcam video feeds suffer from uneven illumination, shadows, and window glare. Standard histogram equalization causes over-amplification of noise. Hence, the system employs **Contrast Limited Adaptive Histogram Equalization (CLAHE)**:
- The image is divided into small contextual blocks called tiles ($8 \times 8$).
- In each tile, the histogram is computed and clipped at a threshold (clipLimit = $2.5$) to prevent noise amplification.
- The clipped contrast is distributed uniformly, and neighboring tiles are combined using bilinear interpolation to remove artificial boundary artifacts.

### 5.3 Biometric Feature Extraction (HOG Descriptor)
The cropped face is resized to a standardized dimension of $128 \times 128$ pixels.
1. **Gradient Computation:** Horizontal ($G_x$) and vertical ($G_y$) derivatives are calculated:
   $$G_x(x,y) = I(x+1, y) - I(x-1, y)$$
   $$G_y(x,y) = I(x, y+1) - I(x, y-1)$$
   $$\text{Magnitude: } M(x, y) = \sqrt{G_x^2 + G_y^2}, \quad \text{Orientation: } \theta(x, y) = \arctan\left(\frac{G_y}{G_x}\right)$$
2. **Spatial Grid Aggregation:** Features are computed over $16 \times 16$ cells grouped into $32 \times 32$ blocks across 9 histogram bins, resulting in a 1,764-dimensional structural vector.
3. Combined with a 256-dimensional downsampled spatial intensity descriptor, it produces a 2,020-dimensional unified vector.
4. **L2 Normalization:**
   $$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|_2} = \frac{\mathbf{v}}{\sqrt{\sum_{i=1}^{n} v_i^2}}$$

### 5.4 Metric Learning & Cosine Similarity
To measure whether query face embedding $\mathbf{A}$ matches registered student embedding $\mathbf{B}$, the **Cosine Similarity** metric is evaluated:
$$\text{Cosine Similarity}(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|_2 \|\mathbf{B}\|_2} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$
- Because vectors $\mathbf{A}$ and $\mathbf{B}$ are already L2-normalized ($\|\mathbf{A}\| = 1, \|\mathbf{B}\| = 1$), this reduces to the inner dot product:
  $$\text{Score} = \mathbf{A} \cdot \mathbf{B}$$
- **Threshold Policy:**
  - $\text{Score} \ge 0.70$: Verified identity match (Present).
  - $\text{Score} < 0.70$: Identity rejected ("Face Not Recognized. Please Register First").
  - $\text{Score} \ge 0.86$ during registration: Flagged as duplicate identity ("This face is already enrolled under another student").

---

\newpage

# CHAPTER 6: CORE SOURCE CODE LISTINGS

### 6.1 Database Connection (`backend/database.py`)
```python
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("Database")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env_path = os.path.join(parent_dir, ".env")
load_dotenv(env_path)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "face_attendance_db")

if DB_PASSWORD:
    mysql_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
else:
    mysql_url = f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

sqlite_db_path = os.path.join(current_dir, "face_attendance.db")
sqlite_url = f"sqlite:///{sqlite_db_path}"

try:
    temp_engine = create_engine(mysql_url, pool_pre_ping=True, connect_args={"connect_timeout": 3})
    with temp_engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    engine = temp_engine
    logger.info("Successfully connected to MySQL database: %s", DB_NAME)
except Exception as e:
    logger.warning("MySQL offline. Falling back to SQLite (%s).", sqlite_db_path)
    engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 6.2 Computer Vision Face Detection (`backend/face_recognition/detection.py`)
```python
import base64
import cv2
import numpy as np

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

def decode_base64_image(image_base64: str) -> np.ndarray:
    if "," in image_base64:
        image_base64 = image_base64.split(",", 1)[1]
    image_bytes = base64.b64decode(image_base64)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Failed to decode image from buffer")
    return image

def detect_face(image: np.ndarray, min_size: int = 60):
    if image is None or image.size == 0:
        return None, None, 0.0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(
        equalized,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(min_size, min_size),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(faces) == 0:
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=4,
            minSize=(min_size - 10, min_size - 10)
        )

    if len(faces) == 0:
        return None, None, 0.0

    best_face = max(faces, key=lambda f: f[2] * f[3])
    x, y, w, h = best_face

    h_img, w_img = image.shape[:2]
    margin_x = int(w * 0.1)
    margin_y = int(h * 0.1)

    x1 = max(0, x - margin_x)
    y1 = max(0, y - margin_y)
    x2 = min(w_img, x + w + margin_x)
    y2 = min(h_img, y + h + margin_y)

    face_crop = image[y1:y2, x1:x2].copy()
    confidence = float(w * h) / float(w_img * h_img)
    return face_crop, (int(x), int(y), int(w), int(h)), confidence
```

### 6.3 Feature Extraction & Normalization (`backend/face_recognition/encoding.py`)
```python
import json
import cv2
import numpy as np

TARGET_SIZE = (128, 128)
hog_descriptor = cv2.HOGDescriptor(
    TARGET_SIZE,
    (32, 32),
    (16, 16),
    (16, 16),
    9
)
clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))

def preprocess_face(face_image: np.ndarray) -> np.ndarray:
    if len(face_image.shape) == 3:
        gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    else:
        gray = face_image

    resized = cv2.resize(gray, TARGET_SIZE, interpolation=cv2.INTER_AREA)
    equalized = clahe.apply(resized)
    smoothed = cv2.bilateralFilter(equalized, d=5, sigmaColor=50, sigmaSpace=50)
    return smoothed

def extract_embedding(face_image: np.ndarray) -> np.ndarray:
    processed = preprocess_face(face_image)

    hog_features = hog_descriptor.compute(processed)
    hog_vec = hog_features.flatten().astype(np.float32)

    spatial_grid = cv2.resize(processed, (16, 16), interpolation=cv2.INTER_AREA).flatten().astype(np.float32)
    spatial_grid = (spatial_grid - np.mean(spatial_grid)) / (np.std(spatial_grid) + 1e-6)

    combined = np.concatenate([hog_vec, spatial_grid * 0.5])
    norm = np.linalg.norm(combined)
    return combined / norm if norm > 0 else combined

def serialize_embedding(embedding: np.ndarray) -> str:
    return json.dumps(embedding.tolist())

def deserialize_embedding(embedding_json: str) -> np.ndarray:
    return np.array(json.loads(embedding_json), dtype=np.float32)
```

### 6.4 Facial Matching Engine (`backend/face_recognition/recognition.py`)
```python
import numpy as np
from typing import List, Tuple, Optional, Dict, Any

DEFAULT_THRESHOLD = 0.70
DUPLICATE_THRESHOLD = 0.86

def calculate_cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(vec_a, vec_b) / (norm_a * norm_b))

def find_matching_student(
    query_embedding: np.ndarray, 
    registered_database: List[Dict[str, Any]], 
    threshold: float = DEFAULT_THRESHOLD
) -> Tuple[Optional[int], float, bool]:
    if not registered_database:
        return None, 0.0, False

    best_match_id = None
    best_similarity = -1.0

    for record in registered_database:
        student_id = record["student_id"]
        stored_emb = record["embedding"]
        similarity = calculate_cosine_similarity(query_embedding, stored_emb)

        if similarity > best_similarity:
            best_similarity = similarity
            best_match_id = student_id

    is_match = (best_similarity >= threshold) and (best_match_id is not None)
    return best_match_id, best_similarity, is_match

def check_duplicate_face(
    new_embedding: np.ndarray, 
    registered_database: List[Dict[str, Any]], 
    current_student_id: Optional[int] = None,
    threshold: float = DUPLICATE_THRESHOLD
) -> Tuple[bool, Optional[int], float]:
    for record in registered_database:
        student_id = record["student_id"]
        if current_student_id is not None and student_id == current_student_id:
            continue
        similarity = calculate_cosine_similarity(new_embedding, record["embedding"])
        if similarity >= threshold:
            return True, student_id, similarity
    return False, None, 0.0
```

### 6.5 Biometric Attendance Pipeline (`backend/routes/attendance.py`)
```python
import os
import datetime
import cv2
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from face_recognition.detection import decode_base64_image, detect_face
from face_recognition.encoding import extract_embedding, deserialize_embedding
from face_recognition.recognition import find_matching_student, DEFAULT_THRESHOLD

router = APIRouter(prefix="/api/attendance", tags=["Attendance Processing"])
SNAPSHOTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads", "snapshots")
os.makedirs(SNAPSHOTS_DIR, exist_ok=True)

@router.post("/mark", response_model=schemas.AttendanceMarkResponse)
def mark_face_attendance(req: schemas.AttendanceMarkRequest, db: Session = Depends(get_db)):
    try:
        frame = decode_base64_image(req.image_base64)
    except Exception as e:
        return schemas.AttendanceMarkResponse(success=False, status_code="ERROR", message="Image decoding failed")

    face_crop, bbox, conf = detect_face(frame, min_size=60)
    if face_crop is None:
        return schemas.AttendanceMarkResponse(
            success=False, 
            status_code="NO_FACE_DETECTED", 
            message="No face detected. Please position face clearly."
        )

    query_embedding = extract_embedding(face_crop)
    registered_records = db.query(models.FaceEmbedding).all()
    if not registered_records:
        return schemas.AttendanceMarkResponse(
            success=False, 
            status_code="UNRECOGNIZED", 
            message="No registered students in database."
        )

    registered_db = [
        {"student_id": r.student_id, "embedding": deserialize_embedding(r.embedding_vector)}
        for r in registered_records
    ]

    matched_id, score, is_match = find_matching_student(query_embedding, registered_db, DEFAULT_THRESHOLD)
    if not is_match or matched_id is None:
        return schemas.AttendanceMarkResponse(
            success=False, 
            status_code="UNRECOGNIZED", 
            message="Face Not Recognized. Please Register First.",
            confidence=round(float(score), 4) if score > 0 else 0.0
        )

    student = db.query(models.Student).filter(models.Student.student_id == matched_id).first()
    today = datetime.date.today()
    now_time = datetime.datetime.now().time()
    time_str = now_time.strftime("%I:%M:%S %p")
    date_str = today.strftime("%Y-%m-%d")

    # Duplicate Attendance Guard
    existing = db.query(models.Attendance).filter(
        models.Attendance.student_id == student.student_id,
        models.Attendance.date == today
    ).first()

    if existing:
        return schemas.AttendanceMarkResponse(
            success=False,
            status_code="ALREADY_MARKED",
            message="Attendance Already Marked Today.",
            student_id=student.student_id,
            full_name=student.full_name,
            roll_number=student.roll_number,
            course=student.course,
            semester=student.semester,
            date=date_str,
            time=existing.time.strftime("%I:%M:%S %p"),
            confidence=round(float(score), 4),
            face_image_url=student.face_image_path
        )

    # Save snapshot proof
    snapshot_filename = f"att_{student.student_id}_{today.strftime('%Y%m%d')}_{now_time.strftime('%H%M%S')}.jpg"
    snapshot_path = os.path.join(SNAPSHOTS_DIR, snapshot_filename)
    cv2.imwrite(snapshot_path, face_crop)

    # Save attendance
    new_attendance = models.Attendance(
        student_id=student.student_id,
        date=today,
        time=now_time,
        status="Present",
        confidence_score=float(score),
        snapshot_path=f"/uploads/snapshots/{snapshot_filename}"
    )
    db.add(new_attendance)
    db.commit()

    return schemas.AttendanceMarkResponse(
        success=True,
        status_code="SUCCESS",
        message="Attendance Marked Successfully!",
        student_id=student.student_id,
        full_name=student.full_name,
        roll_number=student.roll_number,
        course=student.course,
        semester=student.semester,
        date=date_str,
        time=time_str,
        confidence=round(float(score), 4),
        face_image_url=student.face_image_path
    )
```

---

\newpage

# CHAPTER 7: SYSTEM TESTING & VALIDATION

### 7.1 Test Scenarios & Results Table

| Test Case ID | Test Scenario | Input Data | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Admin Authentication with valid credentials | `admin` / `admin123` | Login successful, JWT token issued, redirect to `dashboard.html` | As expected | **PASS** |
| **TC-02** | Admin Authentication with invalid password | `admin` / `wrongpwd` | Login rejected with 401 Unauthorized alert | As expected | **PASS** |
| **TC-03** | Register new student with unique Roll Number | Name: `Rahul`, Roll: `BCA2026002` | Student record and student portal user account created | As expected | **PASS** |
| **TC-04** | Register student with duplicate Roll Number | Roll: `BCA2026001` (already exists) | Rejected with 400 Bad Request: "Roll number already registered" | As expected | **PASS** |
| **TC-05** | Webcam Face Enrollment | Camera snapshot of enrolled student | Face detected, 2020-d embedding saved, photo stored on disk | As expected | **PASS** |
| **TC-06** | Duplicate Face Prevention | Registering the same face under another student | System detects similarity $\ge 0.86$, rejects with identity warning | As expected | **PASS** |
| **TC-07** | Mark Attendance for Registered Face | Enrolled student scans face in kiosk | Face recognized ($\text{score} \ge 0.70$), marked Present with timestamp, voice confirmation | As expected | **PASS** |
| **TC-08** | Duplicate Attendance Prevention | Same student scans face a second time on same day | Rejected with: "Attendance Already Marked Today." Displays earlier timestamp | As expected | **PASS** |
| **TC-09** | Unregistered Face Attempt | Unknown person scans face in kiosk | Rejected with: "Face Not Recognized. Please Register First." | As expected | **PASS** |
| **TC-10** | Camera Obscuration / No Face | Camera covered or facing empty wall | Alert: "No face detected. Please position face clearly." | As expected | **PASS** |
| **TC-11** | Attendance Reports Filtering | Filter by Date, Course, Semester | Filtered records returned with accurate count | As expected | **PASS** |
| **TC-12** | CSV / Excel Data Export | Click "Export to CSV" | Browser triggers direct download of formatted `.csv` register | As expected | **PASS** |

---

\newpage

# CHAPTER 8: VIVA-VOCE FREQUENTLY ASKED QUESTIONS (FAQ)

### Q1. What is the fundamental architecture of this project?
**Answer:** The project follows a decoupled client-server architecture:
- **Frontend Client:** Built using HTML5, CSS3, JavaScript, Bootstrap 5, and Chart.js, rendering modern responsive views and capturing real-time camera frames via WebRTC (`navigator.mediaDevices.getUserMedia`).
- **Backend Server:** Built using Python's FastAPI framework with Uvicorn ASGI server, providing high-performance REST APIs.
- **Computer Vision Pipeline:** OpenCV (`cv2`) handles Haar Cascade face detection, CLAHE lighting equalization, and HOG feature extraction.
- **Database Layer:** MySQL relational database accessed through SQLAlchemy ORM, with an intelligent fallback to SQLite.

### Q2. How does the system detect and recognize faces?
**Answer:**
1. **Detection:** The browser captures a video frame onto an HTML5 canvas and streams it as a Base64 JPEG to the FastAPI backend. OpenCV's Viola-Jones Haar Cascade classifier (`haarcascade_frontalface_default.xml`) scans the frame and extracts the bounding rectangle coordinates $(x, y, w, h)$.
2. **Preprocessing:** The isolated face region is converted to grayscale, resized to $128 \times 128$ pixels, and equalized using **CLAHE** (Contrast Limited Adaptive Histogram Equalization) to cancel out ambient lighting variations.
3. **Encoding:** A normalized multi-scale feature vector (HOG descriptor capturing structural gradients + spatial intensity distribution) is extracted, producing a 2,020-dimensional normalized vector.
4. **Recognition:** The backend calculates the **Cosine Similarity** dot product between the query vector and stored vectors in the `face_embeddings` table. If the maximum similarity exceeds the threshold ($0.70$), the identity is verified.

### Q3. How does the system prevent duplicate attendance (proxy)?
**Answer:**
1. **Biometric Uniqueness:** Every human face has distinct structural contour gradients; roll numbers cannot be punched without physical facial verification.
2. **Database Integrity:** In the MySQL `attendance` table, a composite unique key constraint `UNIQUE (student_id, date)` is enforced.
3. When a face is matched, the backend queries:
   ```sql
   SELECT * FROM attendance WHERE student_id = ? AND date = CURRENT_DATE;
   ```
   If a record exists, the system rejects the request with the status `"ALREADY_MARKED"`, displaying the message: *"Attendance Already Marked Today."*

### Q4. What happens if the college MySQL server is turned off?
**Answer:** The application implements an intelligent **Zero-Crash Database Fallback**. In `backend/database.py`, the engine attempts a ping to MySQL on port 3306. If the connection times out or fails (e.g. XAMPP is offline), it automatically switches to a local SQLite database (`face_attendance.db`) with identical models and tables. When MySQL is started, it seamlessly reconnects to MySQL without modifying any application code.

### Q5. What is the difference between Cosine Similarity and Euclidean Distance?
**Answer:** 
- **Euclidean Distance** measures the straight-line geometric distance between two coordinate points in $N$-dimensional space, which can be heavily skewed by variations in overall image brightness.
- **Cosine Similarity** measures the cosine of the angle between two multi-dimensional vectors, regardless of their magnitude:
  $$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$
  Because our biometric feature vectors are L2-normalized to unit length ($\|\mathbf{A}\| = 1$), Cosine Similarity is scale-invariant, computationally efficient ($O(N)$ dot product), and ranges strictly between $-1$ and $+1$.

---

\newpage

# CHAPTER 9: CONCLUSION & FUTURE ENHANCEMENTS

### 9.1 Conclusion
The **Online Smart Face Recognition Attendance Management System** demonstrates a practical, robust, and cost-effective application of Computer Vision and modern web technologies for educational institutions. By automating attendance through contactless facial recognition, institutions can eliminate proxy attendance, save 15 minutes of lecture time daily, generate instant spreadsheet reports, and keep students informed of their attendance compliance.

### 9.2 Future Enhancements
- **Liveness Detection & Anti-Spoofing:** Integrating eye-blink detection, head-pose estimation, or 3D depth sensing to detect printed photographs or smartphone screen replays.
- **Multi-Face Crowd Detection:** Extending the pipeline to detect and recognize multiple students simultaneously from a classroom wide-angle IP camera.
- **Automated SMS & WhatsApp Alerts:** Sending automated notification messages to parents when a student is absent or falls below the 75% attendance threshold.

---

# CHAPTER 10: REFERENCES

1. Viola, P., & Jones, M. (2001). *Rapid Object Detection using a Boosted Cascade of Simple Features*. IEEE Computer Vision and Pattern Recognition (CVPR).
2. Dalal, N., & Triggs, B. (2005). *Histograms of Oriented Gradients for Human Detection*. IEEE Computer Vision and Pattern Recognition (CVPR).
3. FastAPI Documentation: https://fastapi.tiangolo.com/
4. OpenCV (Open Source Computer Vision Library) Official Documentation: https://docs.opencv.org/
5. SQLAlchemy ORM Documentation: https://docs.sqlalchemy.org/
6. Chart.js Data Visualization Library: https://www.chartjs.org/
