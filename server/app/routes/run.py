"""``POST /api/challenges/{id}/run`` — execute a player's solution.

This is the load-bearing endpoint. The body is a :class:`RunRequest`;
the response is a :class:`RunResponse` (or a 4xx with a structured
error). The actual execution is delegated to
:mod:`server.app.engine_runner` so this module stays focused on
HTTP-level concerns: input validation, error→status mapping, and
forwarding the result.
"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from server.app.engine_runner import (
    ChallengeNotFound,
    NTooLarge,
    NoSolveFunction,
    PlayerSyntaxError,
    run_player_code,
)
from server.app.schemas import RunRequest, RunResponse


router = APIRouter()


@router.post("/challenges/{challenge_id}/run")
def run_challenge(challenge_id: str, body: RunRequest) -> RunResponse:
    """Run the player's source against the named challenge."""
    try:
        return run_player_code(
            challenge_id=challenge_id,
            source=body.source,
            n=body.n,
            seed=body.seed,
        )
    except ChallengeNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except NTooLarge as exc:
        raise HTTPException(
            status_code=422,
            detail={"error": "n_too_large", "requested": exc.requested, "maximum": exc.maximum},
        )
    except PlayerSyntaxError as exc:
        raise HTTPException(
            status_code=422,
            detail={"error": "syntax", "message": str(exc)},
        )
    except NoSolveFunction as exc:
        raise HTTPException(status_code=400, detail={"error": "no_solve", "message": str(exc)})
