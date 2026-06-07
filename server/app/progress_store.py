"""Server-side wrapper over :mod:`code_n.progress`.

A thin shim that re-exports the engine's progress API but with paths
resolved from :mod:`server.app.config`. This is the only place the
server talks to ``progress.json``; route handlers go through these
functions so we can swap in a different store (database, encrypted
file, etc.) later without touching the route code.
"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Optional

from code_n.progress import (
    LevelRecord,
    PlayerProgress,
    load_progress,
    save_progress,
)

from .config import PROGRESS_FILE


def load(path: Optional[Path] = None) -> PlayerProgress:
    """Load the player's progress, or return a fresh one if the file is missing."""
    target = path if path is not None else PROGRESS_FILE
    return load_progress(str(target))


def save(progress: PlayerProgress, path: Optional[Path] = None) -> None:
    """Atomic-save ``progress`` to the on-disk JSON file.

    Writes to ``progress.json.tmp`` first and then ``os.replace``s it
    into place, so a crash mid-write never leaves a half-written file
    the next launch could misread.
    """
    target = path if path is not None else PROGRESS_FILE
    target.parent.mkdir(parents=True, exist_ok=True)
    # Engine's save_progress writes via `open(path, "w")` directly,
    # not atomically. For the server we want atomicity, so we write
    # to a sibling tmpfile and replace. (The engine's path is left
    # untouched; the server can opt into the safer write.)
    tmp = str(target) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        import json
        json.dump(progress.to_dict(), f, indent=2)
    os.replace(tmp, str(target))


def mark(challenge_id: str, ops: int, complexity: str) -> PlayerProgress:
    """Mark a challenge done and persist the new progress."""
    progress = load()
    progress.complete(challenge_id, ops, complexity)
    save(progress)
    return progress


def fail(challenge_id: str) -> PlayerProgress:
    """Record a failure attempt and persist."""
    progress = load()
    progress.fail(challenge_id)
    save(progress)
    return progress


def reset() -> PlayerProgress:
    """Wipe all completion state and persist."""
    progress = load()
    progress.reset_statuses()
    save(progress)
    return progress


def to_out(progress: PlayerProgress) -> dict:
    """Convert to the API response shape (used by the progress route)."""
    return {
        "player_name": progress.player_name or "",
        "completed": sorted(progress.completed),
        "last_status": dict(progress.last_status),
        "records": {
            cid: {
                "challenge_id": rec.challenge_id,
                "best_ops": rec.best_ops,
                "complexity_achieved": rec.complexity_achieved,
                "attempts": rec.attempts,
            }
            for cid, rec in progress.records.items()
        },
    }
