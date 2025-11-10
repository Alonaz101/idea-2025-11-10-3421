from fastapi import FastAPI
from .main import app as main_app
from .user import router as user_router
from .social import router as social_router

app = FastAPI(title="Complete Mood-Based Recipe Recommendation API")

app.include_router(main_app.router)
app.include_router(user_router)
app.include_router(social_router)
