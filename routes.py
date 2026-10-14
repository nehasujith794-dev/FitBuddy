from pathlib import Path
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import get_db

def generate_updated_plan(name="Neha", goal="weight_gain"):
    diet = "2800 cal High Protein - Banana 4, Eggs 4, Milk 500ml"
    return {
        "workout_plan": {
            "Day 1 - Chest": {"Focus": "Chest", "Warm-up": "5 min", "Main Workout": "Push-ups 3x15", "Rest/Recovery": "Stretch", "Tips": diet},
            "Day 2 - Back": {"Focus": "Back", "Warm-up": "Jog", "Main Workout": "Pull-ups 3x10", "Rest/Recovery": "Roll", "Tips": diet},
            "Day 3 - Legs": {"Focus": "Legs", "Warm-up": "Squat", "Main Workout": "Squats 4x20", "Rest/Recovery": "Rest", "Tips": diet},
            "Day 4 - Rest": {"Focus": "Recovery", "Warm-up": "Yoga", "Main Workout": "Walk 30min", "Rest/Recovery": "Full Rest", "Tips": "Banana"},
            "Day 5 - Arms": {"Focus": "Arms", "Warm-up": "Skip", "Main Workout": "Curls 3x12", "Rest/Recovery": "Stretch", "Tips": "Eggs"},
            "Day 6 - Cardio": {"Focus": "Cardio", "Warm-up": "Run", "Main Workout": "Run 20min", "Rest/Recovery": "Breathe", "Tips": "PB"},
            "Day 7 - Full": {"Focus": "Full Body", "Warm-up": "Stretch", "Main Workout": "HIIT 30min", "Rest/Recovery": "8hr Sleep", "Tips": "Photo"}
        },
        "diet_tip": diet,
        "recovery_tip": "8hrs sleep, 3L water"
    }

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
router = APIRouter()

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/generate")
async def gen_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.get("/generate-workout")
async def gen_workout_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.post("/generate")
async def gen_post(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    name = str(form.get("name") or form.get("username") or "Neha")
    return templates.TemplateResponse("result.html", {"request": request, "name": name, "plan": generate_updated_plan(name)["workout_plan"], "diet_tip": "High Protein", "recovery_tip": "8hrs sleep"})

@router.post("/generate-workout")
async def gen_workout_post(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    name = str(form.get("name") or form.get("username") or "Neha")
    result = generate_updated_plan(name)
    return templates.TemplateResponse("result.html", {"request": request, "name": name, "plan": result["workout_plan"], "diet_tip": result["diet_tip"], "recovery_tip": result["recovery_tip"]})