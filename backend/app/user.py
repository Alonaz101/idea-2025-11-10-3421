from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

router = APIRouter(prefix="/api/users", tags=["users"])

# Simulated in-memory user store
user_db = {}

class UserProfile(BaseModel):
    id: int
    name: str
    dietary_preferences: List[str] = []
    mood_history: List[str] = []


@router.post("/")
def create_user(user: UserProfile):
    if user.id in user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    user_db[user.id] = user
    return {"message": "User created", "user_id": user.id}


@router.get("/{user_id}/preferences")
def get_preferences(user_id: int) -> List[str]:
    user = user_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.dietary_preferences


@router.post("/{user_id}/mood-history")
def add_mood_history(user_id: int, mood: str):
    user = user_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.mood_history.append(mood)
    return {"message": "Mood added to history"}
