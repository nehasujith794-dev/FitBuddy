# FitBuddy – AI Fitness Plan Generator

Complete implementation of the supplied FitBuddy project specification.

## Stack
- FastAPI backend
- Jinja2 HTML frontend
- SQLite + SQLAlchemy
- Google Gemini through the current `google-genai` SDK
- REST API + Swagger docs
- Feedback-based plan regeneration
- Admin dashboard

The source document names Gemini 1.5 Pro and Gemini Flash. Model names can change over time, so this implementation uses environment variables. The default is a current Gemini Flash model; change it in `.env` if your Google AI account exposes a different model.

## Setup in VS Code

### 1. Open the project
Open this `FitBuddy` folder in VS Code.

### 2. Create a virtual environment
Windows PowerShell:
```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

Windows CMD:
```cmd
python -m venv venv
venv\Scriptsctivate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Gemini
Copy `.env.example` to `.env` and add your Gemini API key:
```text
GOOGLE_API_KEY=YOUR_REAL_KEY
```

Do not upload or commit `.env`.

### 5. Run
```bash
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/view-all-users?key=change-this-admin-key

Change `ADMIN_KEY` before using the admin page.

## Test
Run:
```bash
pytest -q
```

The tests mock the AI failure path and do not require a Gemini key.

## Main flow
1. User opens `/`.
2. User submits name, ID, age, weight, goal and intensity.
3. `/generate-workout` validates the form.
4. Gemini creates a 7-day workout plan.
5. Gemini creates a concise nutrition/recovery tip.
6. SQLAlchemy stores the user and original plan in SQLite.
7. `result.html` displays the result.
8. Feedback is sent to `/submit-feedback`.
9. Gemini returns a revised complete 7-day plan.
10. The revised plan is stored separately.
11. `/view-all-users` shows original and updated plans.

## API
- `GET /api/health`
- `POST /api/generate-workout`
- `POST /api/submit-feedback`
- `GET /api/users?key=...`

This is an educational wellness project, not a medical service. AI output should not be treated as medical advice.
