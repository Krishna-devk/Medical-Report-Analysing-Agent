from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import config
from routes import router as MedRouter


app = FastAPI(
    title="QuickCare AI",
    description="AI-powered medical report analysis using Google Gemini",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(MedRouter)