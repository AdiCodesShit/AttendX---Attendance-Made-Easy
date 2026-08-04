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

Create a `.env` file in the project root:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

### 5. Start AttendX

```bash
streamlit run app.py
```

The application should open at:

```text
http://localhost:8501
```

---

## ⭐ Support

If you find AttendX interesting, consider giving the repository a ⭐ on GitHub.

**AttendX — Attendance, made easy.**
