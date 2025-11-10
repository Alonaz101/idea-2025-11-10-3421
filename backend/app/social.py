from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

router = APIRouter(prefix="/api/social", tags=["social"])

# Dummy in-memory data stores
posts_db = []
analytics_data = {}

class SocialPost(BaseModel):
    user_id: int
    content: str

class VoiceInput(BaseModel):
    user_id: int
    voice_text: str

@router.post("/share")
def share_post(post: SocialPost):
    posts_db.append(post.dict())
    return {"message": "Post shared", "post_id": len(posts_db)}

@router.get("/analytics")
def get_analytics():
    # Return dummy analytics data
    return analytics_data

@router.post("/voice-input")
def process_voice_input(voice_input: VoiceInput):
    # For demo, just echo the voice text
    return {"message": "Voice input received", "text": voice_input.voice_text}
