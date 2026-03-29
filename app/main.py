from fastapi import FastAPI
from app.api.auth_routes import router as auth_router

app = FastAPI(title="GitHub Connector")

app.include_router(auth_router)

from app.api.github_routes import router as github_router

app.include_router(github_router)