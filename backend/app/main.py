from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Mood-Based Recipe Recommendation API")

# In-memory data stores for demonstration
recipe_db = {
    1: {"id": 1, "name": "Chocolate Cake", "moods": ["happy", "celebration"]},
    2: {"id": 2, "name": "Caesar Salad", "moods": ["healthy", "neutral"]},
    3: {"id": 3, "name": "Spicy Curry", "moods": ["adventurous", "excited"]},
}


class MoodInput(BaseModel):
    mood: str


@app.post("/api/recommendations")
def recommend_recipes(mood_input: MoodInput) -> List[Dict]:
    # Return recipes matching the mood
    mood = mood_input.mood.lower()
    matched = [r for r in recipe_db.values() if mood in r["moods"]]
    if not matched:
        raise HTTPException(status_code=404, detail="No recipes found for the given mood")
    return matched


@app.get("/api/recipes/{recipe_id}")
def get_recipe(recipe_id: int) -> Dict:
    recipe = recipe_db.get(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


# Run with: uvicorn main:app --reload
