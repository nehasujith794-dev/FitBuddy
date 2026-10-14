def generate_updated_plan(username, age, weight, goal, intensity, user_id=None, name=None):
    diet = "2800 cal, 110g protein, Banana 4, Eggs 4, Milk 500ml, Peanut Butter daily!"
    return {
        "workout_plan": {
            "Day 1 - Chest": {"Focus": "Chest", "Warm-up": "Jacks 5 min", "Main Workout": "Push-ups 3x15", "Rest/Recovery": "Stretch", "Tips": diet},
            "Day 2 - Back": {"Focus": "Back", "Warm-up": "Jog", "Main Workout": "Pull-ups 3x10", "Rest/Recovery": "Roll", "Tips": diet},
            "Day 3 - Legs": {"Focus": "Legs", "Warm-up": "Squats", "Main Workout": "Squats 4x20", "Rest/Recovery": "Rest", "Tips": "Banana"},
            "Day 4 - Rest": {"Focus": "Recovery", "Warm-up": "Yoga", "Main Workout": "Walk 30 min", "Rest/Recovery": "Full rest", "Tips": "Sleep"},
            "Day 5 - Arms": {"Focus": "Arms", "Warm-up": "Skip", "Main Workout": "Curls 3x12", "Rest/Recovery": "Stretch", "Tips": "Eggs"},
            "Day 6 - Cardio": {"Focus": "Cardio", "Warm-up": "Run", "Main Workout": "Run 20 min", "Rest/Recovery": "Breath", "Tips": "PB"},
            "Day 7 - Full": {"Focus": "Full Body", "Warm-up": "Stretch", "Main Workout": "HIIT 30 min", "Rest/Recovery": "Rest", "Tips": "Photo"}
        },
        "diet_tip": diet,
        "recovery_tip": "8hrs sleep, 3L water"
    }

def generate_workout_gemini(*a, **k): return generate_updated_plan(*a, **k)
def generate_fitness_plan(*a, **k): return generate_updated_plan(*a, **k)
def generate_nutrition_tip_with_flash(*a, **k): return "High protein diet 2800 cal daily!"