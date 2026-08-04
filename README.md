# AttendX — AI-Powered Attendance System

> **Attendance, made easy.**

AttendX is an AI-assisted attendance management system designed to make classroom attendance faster, smarter, and easier to manage. It combines **face recognition** and **voice recognition** with a modern teacher/student workflow, allowing teachers to manage subjects and attendance while students can enroll in subjects and track their attendance.

---

## ✨ Features

### 👨‍🏫 Teacher Dashboard
- Create and manage subjects.
- Generate/share subject enrollment codes.
- View enrolled students.
- Mark attendance using AI-assisted recognition.
- View attendance records and logs.
- Manage classroom attendance from a centralized dashboard.

### 👨‍🎓 Student Dashboard
- Join subjects using a teacher-provided subject code.
- View enrolled subjects.
- Track attendance records.
- Access attendance information through a simple dashboard.

### 🤖 AI-Assisted Attendance
AttendX is built around two recognition pipelines:

- **Face Recognition** — identifies students from captured images.
- **Voice Recognition** — provides an additional identity-verification method using speaker embeddings.

The system is designed so that attendance can be verified using biometric signals instead of relying entirely on manual roll calls.

### 🗄️ Cloud Database
AttendX uses **Supabase** for backend data storage and management, including:
- User information
- Subject information
- Student enrollments
- Attendance logs
- Subject codes and relationships

### 🎨 Modern Interface
The application includes:
- Separate teacher and student experiences
- Responsive dashboard layouts
- Custom UI styling
- Interactive dialogs
- Landing page explaining the teacher and student journeys
- Clean, classroom-focused design

---

## 🏗️ Project Architecture

```text
AttendX
│
├── app.py                  # Main Streamlit application
│
├── pages/
│   ├── teacher.py          # Teacher dashboard/workflows
│   └── student.py          # Student dashboard/workflows
│
├── face_pipeline.py        # Face recognition pipeline
├── voice_pipeline.py       # Voice recognition pipeline
│
├── assets/
│   ├── images/
│   └── ...
│
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

> File names may vary depending on the current version of the project. The structure above represents the main logical components of AttendX.

---

## 🔄 How AttendX Works

### Teacher Journey

```text
Teacher
   │
   ▼
Create / Manage Subject
   │
   ▼
Generate Subject Code
   │
   ▼
Share Code with Students
   │
   ▼
Students Enroll
   │
   ▼
Start Attendance Session
   │
   ▼
AI-Assisted Recognition
   │
   ▼
Attendance Recorded
   │
   ▼
View Attendance Records
```

### Student Journey

```text
Student
   │
   ▼
Login / Open Dashboard
   │
   ▼
Enter Subject Code
   │
   ▼
Join Subject
   │
   ▼
View Enrolled Subjects
   │
   ▼
Participate in Attendance
   │
   ▼
Track Attendance
```

---

## 🧠 AI / ML Components

### Face Recognition

The face pipeline processes an image, detects/encodes faces, and compares the resulting representation against registered student data.

The project uses the `face_recognition` ecosystem for facial embeddings.

Conceptually:

```text
Camera / Image
      │
      ▼
Face Detection
      │
      ▼
Face Encoding
      │
      ▼
Compare with Registered Encodings
      │
      ▼
Student Identity
      │
      ▼
Attendance
```

### Voice Recognition

The voice pipeline uses speaker embeddings to compare a student's voice against registered voice representations.

The project has experimented with **SpeechBrain** and **Resemblyzer**, with Resemblyzer being used as the direction for the rewritten voice pipeline.

Conceptually:

```text
Audio Input
    │
    ▼
Audio Preprocessing
    │
    ▼
Speaker Embedding
    │
    ▼
Compare with Registered Voice Embeddings
    │
    ▼
Speaker Identity
    │
    ▼
Attendance Verification
```

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Frontend / UI | Streamlit |
| Backend | Python |
| Database | Supabase / PostgreSQL |
| Face Recognition | face_recognition |
| Voice Recognition | Resemblyzer |
| ML / AI | PyTorch, NumPy |
| Data Processing | Pandas |
| Version Control | Git / GitHub |
| Development | VS Code |

---

## 📋 Requirements

Recommended environment:

- **Python 3.12.x**
- Git
- A Supabase project
- Webcam/microphone access for recognition features

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

AttendX requires your Supabase project credentials.

Create a `.env` file in the project root:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

For Streamlit deployment, add the same values through your deployment platform's environment/secrets configuration rather than committing them to GitHub.

### ⚠️ Never commit secrets

Do **not** upload:

```text
.env
secrets.toml
API keys
service-role keys
private credentials
```

Make sure they are included in `.gitignore`.

---

## 🗃️ Database

AttendX uses Supabase as its cloud database.

The database is responsible for storing application data such as:

```text
Users
 │
 ├── Teachers
 └── Students

Subjects
 │
 ├── Subject details
 ├── Subject code
 └── Teacher relationship

Enrollments
 │
 └── Student ↔ Subject

Attendance Logs
 │
 ├── Student
 ├── Subject
 ├── Date / Time
 └── Attendance status
```

A typical relationship looks like:

```text
Teacher
   │
   └──────< Subject
               │
               ├──────< Enrollment >────── Student
               │
               └──────< Attendance Log
```

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AttendX.git
cd AttendX
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Supabase

Add your Supabase URL and API key using environment variables or Streamlit secrets.

### 5. Start AttendX

```bash
streamlit run app.py
```

The application should open at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

AttendX can be deployed using platforms that support Streamlit/Python applications.

For deployment:

1. Push the project to GitHub.
2. Connect the repository to your deployment platform.
3. Select `app.py` as the main application.
4. Configure the required Supabase secrets/environment variables.
5. Install dependencies from `requirements.txt`.
6. Deploy the application.

### Streamlit Cloud

If deploying through Streamlit Community Cloud, add your secrets through the application's **Secrets** configuration instead of storing them in the repository.

Example:

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
```

---

## 🔐 Security Considerations

AttendX handles identity-related information, so security is important.

Recommended practices:

- Never expose Supabase service-role keys in frontend code.
- Never commit API keys to GitHub.
- Use environment variables / Streamlit secrets.
- Validate subject enrollment codes on the server/database side.
- Restrict database access using appropriate Supabase Row Level Security (RLS) policies.
- Avoid storing raw biometric data when an embedding-based approach is sufficient.
- Use HTTPS in production.
- Carefully control who can create, modify, or view attendance records.

---

## 📁 Suggested Git Workflow

```bash
git status
git add .
git commit -m "Update AttendX"
git push origin main
```

Before pushing, verify that sensitive files are not staged:

```bash
git status
```

---

## 🧪 Development

AttendX is actively developed as a student software/AI project.

The project combines multiple areas of development:

- Full-stack application development
- Database design
- Computer vision
- Speaker recognition
- Machine learning
- UI/UX
- Cloud deployment

This makes AttendX a practical project demonstrating how AI can be integrated into a real-world educational workflow.

---

## 🗺️ Future Improvements

Potential future features include:

- 📊 Advanced attendance analytics
- 📈 Attendance trend visualizations
- 📱 Mobile-friendly student experience
- 🔔 Attendance notifications
- 📥 Export attendance to CSV/Excel
- 🧑‍💼 Improved teacher administration
- 🔒 Stronger authentication and authorization
- 🎙️ Improved speaker verification
- 👤 Improved face-recognition robustness
- ⚡ Faster attendance processing
- 📝 Automated attendance reports
- 🏫 Support for multiple institutions/classes
- 🧠 More robust anti-spoofing/liveness verification

---

## 🎯 Project Goal

Traditional attendance systems can be repetitive, time-consuming, and prone to manual errors.

**AttendX aims to simplify this process by combining AI-assisted identity recognition with a centralized attendance management system.**

The goal is simple:

> **Spend less time taking attendance and more time teaching.**

---

## 👨‍💻 Contributors

Developed as a B.Tech student project.

If you are interested in contributing, feel free to fork the repository, create a feature branch, and submit a pull request.

```bash
git checkout -b feature/your-feature
git add .
git commit -m "Add your feature"
git push origin feature/your-feature
```

---

## 📄 License

Add your preferred open-source license here.

For example:

```text
MIT License
```

If you intend to make AttendX open source, create a `LICENSE` file in the repository and select the appropriate license for your project.

---

## ⭐ Support

If you find AttendX interesting, consider giving the repository a ⭐ on GitHub.

**AttendX — Attendance, made easy.**
