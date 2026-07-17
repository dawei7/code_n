"""Profile-scoped custom LeetCode problem-set storage."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from server.app import progress_store
from server.app.custom_problem_sets import (
    CUSTOM_PROBLEM_SETS_VERSION,
    CustomProblemSetValidationError,
    normalize_custom_problem_sets,
    safely_normalize_saved_custom_problem_sets,
)
from server.app.schemas import CustomProblemSetsOut, CustomProblemSetsUpdate


router = APIRouter()


def _to_out(raw_sets: object) -> CustomProblemSetsOut:
    return CustomProblemSetsOut(
        version=CUSTOM_PROBLEM_SETS_VERSION,
        sets=safely_normalize_saved_custom_problem_sets(raw_sets),
    )


@router.get("/custom-problem-sets")
def get_custom_problem_sets() -> CustomProblemSetsOut:
    """Return the active profile's ordered custom problem-set trees."""

    return _to_out(progress_store.load().custom_problem_sets)


@router.put("/custom-problem-sets")
def replace_custom_problem_sets(body: CustomProblemSetsUpdate) -> CustomProblemSetsOut:
    """Validate and atomically replace the active profile's custom sets."""

    try:
        normalized = normalize_custom_problem_sets(body.sets)
    except CustomProblemSetValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    progress = progress_store.load()
    progress.custom_problem_sets = normalized
    progress_store.save(progress)
    return CustomProblemSetsOut(
        version=CUSTOM_PROBLEM_SETS_VERSION,
        sets=normalized,
    )
