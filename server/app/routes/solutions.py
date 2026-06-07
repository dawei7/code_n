"""``GET /api/solutions/{id}`` and ``PUT /api/solutions/{id}`` — read/write the player's source.

The on-disk file is ``solutions/{id}.py`` in ``CODEN_HOME``. The
web editor saves here when the player hits ``Cmd/Ctrl+S``, and the
``POST /api/challenges/{id}/run`` endpoint reads from the editor
state (not the file), so this endpoint is the durable backup.
"""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException

from challenges.registry import CHALLENGE_REGISTRY
from server.app.config import SOLUTIONS_DIR
from server.app.schemas import SolutionGet, SolutionPut


router = APIRouter()


def _solution_path(challenge_id: str) -> Path:
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    return SOLUTIONS_DIR / f"{challenge_id}.py"


@router.get("/solutions/{challenge_id}")
def get_solution(challenge_id: str) -> SolutionGet:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    path = _solution_path(challenge_id)
    if path.exists():
        return SolutionGet(challenge_id=challenge_id, source=path.read_text(encoding="utf-8"), exists=True)
    return SolutionGet(challenge_id=challenge_id, source="", exists=False)


@router.put("/solutions/{challenge_id}")
def put_solution(challenge_id: str, body: SolutionPut) -> SolutionGet:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    path = _solution_path(challenge_id)
    path.write_text(body.source, encoding="utf-8")
    return SolutionGet(challenge_id=challenge_id, source=body.source, exists=True)
