"""Server-side wrapper over :mod:`engine.progress` with multi-profile support.

This is the only place the server talks to ``progress.json``.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Optional

from engine.progress import (
    PlayerProgress,
)
from server.app.challenge_sets import normalize_algorithm_set

from .config import PROGRESS_FILE


def load_profiles_data() -> dict:
    """Load profiles from progress.json, or migrate legacy single-profile data."""
    if not PROGRESS_FILE.exists():
        # fresh default
        return {
            "active_profile": "Default",
            "profiles": {
                "Default": PlayerProgress(player_name="").to_dict()
            }
        }
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {
            "active_profile": "Default",
            "profiles": {
                "Default": PlayerProgress(player_name="").to_dict()
            }
        }

    if "profiles" in data:
        # already updated schema
        return data
    else:
        # legacy single-player format migration
        try:
            legacy_progress = PlayerProgress.from_dict(data)
            return {
                "active_profile": "Default",
                "profiles": {
                    "Default": legacy_progress.to_dict()
                }
            }
        except Exception:
            return {
                "active_profile": "Default",
                "profiles": {
                    "Default": PlayerProgress(player_name="").to_dict()
                }
            }


def save_profiles_data(data: dict) -> None:
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = str(PROGRESS_FILE) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, str(PROGRESS_FILE))


def load(path: Optional[Path] = None) -> PlayerProgress:
    """Load the active profile's progress."""
    data = load_profiles_data()
    active = data.get("active_profile", "Default")
    profiles = data.get("profiles", {})
    if active not in profiles:
        if not profiles:
            profiles["Default"] = PlayerProgress(player_name="").to_dict()
            active = "Default"
        else:
            active = list(profiles.keys())[0]
        data["active_profile"] = active
        data["profiles"] = profiles
        save_profiles_data(data)
    
    progress = PlayerProgress.from_dict(profiles[active])
    progress.active_set = normalize_algorithm_set(progress.active_set)
    return progress


def save(progress: PlayerProgress, path: Optional[Path] = None) -> None:
    """Save the progress for the active profile."""
    # Recalculate milestones before saving
    update_milestones(progress)
    
    data = load_profiles_data()
    active = data.get("active_profile", "Default")
    if "profiles" not in data:
        data["profiles"] = {}
    data["profiles"][active] = progress.to_dict()
    save_profiles_data(data)


def update_milestones(progress: PlayerProgress) -> list[str]:
    """Discard milestones from the retired pre-LeetCode progression model."""
    progress.milestones = []
    return []


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


def reset(
    challenge_ids: list[str] | None = None,
    scope: str = "all",
) -> PlayerProgress:
    """Clear selected progress for the active profile and persist."""
    progress = load()
    progress.reset_statuses(challenge_ids, scope)
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
        "career_mode": progress.career_mode,
        "leetcode_username": progress.leetcode_username,
        "leetcode_solved": list(progress.leetcode_solved),
        "leetcode_submissions": dict(progress.leetcode_submissions),
        "unlocked_leetcode": list(progress.unlocked_leetcode),
        "milestones": list(progress.milestones),
        "gemini_api_key": progress.gemini_api_key,
        "active_set": progress.active_set,
        "active_custom_set_id": progress.active_custom_set_id,
        "sidebar_width": progress.sidebar_width,
        "sidebar_position": progress.sidebar_position,
        "sidebar_collapsed": progress.sidebar_collapsed,
        "pane_font_scales": dict(progress.pane_font_scales),
        "pane_sizes": dict(progress.pane_sizes),
        "accent_colors": dict(progress.accent_colors),
    }
