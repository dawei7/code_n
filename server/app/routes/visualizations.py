"""Read-only endpoints for canonical algorithm visualizations."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from challenges.registry import CHALLENGE_REGISTRY
from server.app.visualizations import VisualizationDefinition, load_visualization


router = APIRouter()


@router.get("/visualizations/{challenge_id}")
def get_visualization(challenge_id: str) -> VisualizationDefinition:
    """Return a validated visual lesson for one canonical challenge."""
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found")
    try:
        definition = load_visualization(challenge_id)
    except (OSError, ValueError, ValidationError) as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid visualization for '{challenge_id}': {exc}",
        ) from exc
    if definition is None:
        raise HTTPException(
            status_code=404,
            detail=f"No visual walkthrough is authored for '{challenge_id}'",
        )
    return definition
