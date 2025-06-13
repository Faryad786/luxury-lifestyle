# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.index import api_router

app = FastAPI(
    title="Sleep Village API",
    version="1.0.0",
    description="Backend for Sleep Village application."
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount your routes
app.include_router(api_router)
