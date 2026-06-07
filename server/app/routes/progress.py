"""``GET /api/progress`` and ``PUT /api/progress`` — read/write the player's save.

The on-disk file is ``progress.json`` in ``CODEN_HOME`` (default: the
project root). The engine's :mod:`code_n.progress` already handles
the JSON shape; this module wraps it with the API contract.
"""
from __future__ import annotations

from fastapi import APIRouter

from server.app import progress_store
from server.app.schemas import ProgressOut, ProgressUpdate


router = APIRouter()


def _to_out(progress) -> ProgressOut:
    data = progress_store.to_out(progress)
    return ProgressOut(**data)


@router.get("/progress")
def get_progress() -> ProgressOut:
    """Return the current progress, or a fresh empty one if no save exists."""
    return _to_out(progress_store.load())


@router.put("/progress")
def update_progress(body: ProgressUpdate) -> ProgressOut:
    """Apply one update action: mark, fail, or reset. Exactly one should be set."""
    if body.mark is not None:
        progress = progress_store.mark(
            challenge_id=body.mark["challenge_id"],
            ops=int(body.mark["ops"]),
            complexity=body.mark["complexity"],
        )
    elif body.fail is not None:
        progress = progress_store.fail(body.fail)
    elif body.reset:
        progress = progress_store.reset()
    else:
        # No-op update (or a player_name change alone). Still persist
        # player_name if provided.
        progress = progress_store.load()
        if body.player_name is not None:
            progress.player_name = body.player_name
            progress_store.save(progress)
    return _to_out(progress)
