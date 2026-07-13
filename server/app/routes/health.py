"""``GET /api/health`` startup probe.

The Electron main process polls this endpoint until it gets a 200 before
opening the BrowserWindow. Application startup preloads the canonical challenge
summary corpus first, so a successful probe means every selector view is ready.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "coden-server"}
