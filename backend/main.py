from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routes import router

app = FastAPI(title="My PWA Project API")

# CORS for local development and PWA served from same origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static frontend files at root path
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Include API router under /api
app.include_router(router, prefix="/api")