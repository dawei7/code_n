"""``GET /api/health`` startup probe.

The Electron main process polls this endpoint until it gets a 200
before opening the BrowserWindow. The endpoint does NOT warm the
engine registry; the FastAPI lifespan hook does that so the first
/api/challenges call is fast.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "coden-server"}
