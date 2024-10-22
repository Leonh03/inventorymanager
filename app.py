# app.py

from fastapi import FastAPI
from routes import fetch_routes  # Import the routes
from fastapi.middleware.cors import CORSMiddleware
from routes import userInteraction_routes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5000"],  # List your frontend origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(fetch_routes.router)
app.include_router(userInteraction_routes.router)
