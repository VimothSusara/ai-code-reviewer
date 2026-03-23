from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from contextlib import asynccontextmanager

from app.api.v1.code_review import router as code_review_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME
)

API_BASE = f"{settings.API_PREFIX}{settings.API_VERSION}"

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    code_review_router,
    prefix=f"{API_BASE}/code_review",
    tags=["code_review"]
)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running..."
    }