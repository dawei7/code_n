"""``GET /api/progress`` and ``PUT /api/progress`` — read/write the player's save.

The on-disk file is ``progress.json`` in ``CODEN_HOME`` (default: the
project root). The engine's :mod:`code_n.progress` already handles
the JSON shape; this module wraps it with the API contract.
"""
from __future__ import annotations

from fastapi import APIRouter

from server.app import progress_store
from server.app.challenge_sets import normalize_algorithm_set
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
        # No-op update (or a player_name/settings change). Still persist if changed.
        progress = progress_store.load()
        changed = False
        if body.player_name is not None:
            progress.player_name = body.player_name
            changed = True
        if body.career_mode is not None:
            progress.career_mode = body.career_mode
            changed = True
        if body.leetcode_username is not None:
            progress.leetcode_username = body.leetcode_username
            changed = True
        if body.gemini_api_key is not None:
            progress.gemini_api_key = body.gemini_api_key
            changed = True
        if body.active_set is not None:
            progress.active_set = normalize_algorithm_set(body.active_set)
            changed = True
        if changed:
            progress_store.save(progress)
    return _to_out(progress)


from server.app.schemas import VerifyLeetCodeRequest, VerifyLeetCodeResponse
from server.app.leetcode_verification import check_leetcode_solved
from server.app.leetcode_mapping import LEETCODE_MAPPING

@router.post("/progress/verify-leetcode")
def verify_leetcode(body: VerifyLeetCodeRequest) -> VerifyLeetCodeResponse:
    """Auto-verify LeetCode for any challenge since LeetCode integration is disabled."""
    challenge_id = body.challenge_id
    progress = progress_store.load()
    
    if challenge_id not in progress.unlocked_leetcode:
        progress.unlocked_leetcode.append(challenge_id)
        progress_store.save(progress)
        
    return VerifyLeetCodeResponse(
        success=True,
        message="LeetCode verification is disabled. Auto-verified!",
        unlocked_leetcode=list(progress.unlocked_leetcode),
        milestones=list(progress.milestones),
    )
