"""``POST /api/challenges/{id}/run`` — execute a player's solution.

This is the load-bearing endpoint. The body is a :class:`RunRequest`;
the response is a :class:`RunResponse` (or a 4xx with a structured
error). The actual execution is delegated to
:mod:`server.app.engine_runner` so this module stays focused on
HTTP-level concerns: input validation, error→status mapping, and
forwarding the result.
"""
from __future__ import annotations

import random

from fastapi import APIRouter, HTTPException

from challenges.registry import CHALLENGE_REGISTRY

from server.app.engine_runner import (
    ChallengeNotFound,
    NTooLarge,
    NoSolveFunction,
    PlayerSyntaxError,
    run_player_code,
)
from server.app.schemas import RunRequest, RunResponse


router = APIRouter()


# Cap for the server-picked n in real-test mode. Most algorithms
# have a reasonable runtime at n=64; larger n would only slow the
# server without changing the test outcome (a wrong algorithm
# is wrong at any n; the right one is fast at n=64).
_REAL_TEST_N_CAP = 64


@router.post("/challenges/{challenge_id}/run")
def run_challenge(challenge_id: str, body: RunRequest) -> RunResponse:
    """Run the player's source against the named challenge.

    In ``real_test`` mode, ``body.n`` and ``body.seed`` are ignored
    and the server picks its own (deterministic-feeling but fresh)
    values. The response always reports the actual ``n`` used.

    The real-test n is ``min(64, challenge.max_n)`` — a 2D-DP
    challenge with max_n=35 will run at n=35, not 64. The cap is
    a ceiling, not a target.
    """
    n = body.n
    seed = body.seed
    if body.mode == "real_test":
        challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
        if challenge_cls is None:
            # 404 below; let the engine_runner surface the error
            # for consistency with the practice path.
            pass
        else:
            max_n = challenge_cls().max_n
            n = min(_REAL_TEST_N_CAP, max_n)
        seed = random.randint(0, (1 << 30) - 1)
    try:
        return run_player_code(
            challenge_id=challenge_id,
            source=body.source,
            n=n,
            seed=seed,
            mode=body.mode,
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
