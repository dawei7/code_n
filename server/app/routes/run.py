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

from fastapi import APIRouter, BackgroundTasks, HTTPException

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
def run_challenge(challenge_id: str, body: RunRequest, background_tasks: BackgroundTasks) -> RunResponse:
    """Run the player's source against the named challenge.

    In ``real_test`` mode, ``body.n`` and ``body.seed`` are ignored
    and the server picks its own (deterministic-feeling but fresh)
    values. The response always reports the actual ``n`` used.

    The real-test n is ``min(64, challenge.max_n)`` — a 2D-DP
    challenge with max_n=35 will run at n=35, not 64. The cap is
    a ceiling, not a target.
    """
    from server.app import progress_store
    progress = progress_store.load()
    if progress.active_set in {"neetcode", "codechef"}:
        from server.app.routes.challenges import codechef_has_practice_track, get_unlocked_challenges
        all_challenges = [cls() for cls in CHALLENGE_REGISTRY.values()]
        unlocked_set = get_unlocked_challenges(progress, all_challenges)
        if challenge_id not in unlocked_set:
            if progress.active_set == "codechef" and codechef_has_practice_track(challenge_id):
                pass
            else:
                raise HTTPException(status_code=403, detail="Challenge is locked in Career Mode.")

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
        result = run_player_code(
            challenge_id=challenge_id,
            source=body.source,
            n=n,
            seed=seed,
            mode=body.mode,
        )
        if result.passed and challenge_id.startswith("cc_"):
            from server.app.codechef_community import refresh_best_python3_solution
            background_tasks.add_task(refresh_best_python3_solution, challenge_id)
        return result
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


import requests
from server.app.schemas import AnalyzeRequest, AnalyzeResponse

@router.post("/challenges/{challenge_id}/analyze")
def analyze_error(challenge_id: str, body: AnalyzeRequest) -> AnalyzeResponse:
    from server.app import progress_store
    progress = progress_store.load()
    api_key = progress.gemini_api_key.strip()
    if not api_key:
        raise HTTPException(
            status_code=400,
            detail="Please configure your Gemini API Key in the Profile settings first."
        )

    # Resolve challenge description
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found.")
    challenge = challenge_cls()
    description = challenge.info.description

    # Prepare inputs text
    inputs_text = ""
    for name, value in body.inputs.items():
        inputs_text += f"- {name}: {value}\n"

    # Prepare prompt for Gemini 1.5 Flash
    prompt = f"""You are a brilliant computer science professor and algorithm tutor.
Analyze the following bug in a solution for the challenge '{challenge_id}'.

Challenge Description:
{description}

Input Variables:
{inputs_text}

User's Code:
```python
{body.source}
```

Execution Details:
- Input size (n): {body.n}
- RNG Seed: {body.seed}
- What User's Code Returned: {body.returned}
- What was Expected (Correct Return Value): {body.expected}

Explain clearly:
1. Why the user's solution returned the incorrect value. Be precise and locate the exact line/logic issue.
2. How to fix it (give a concise explanation, do NOT write the full correct code, just guide them on what to change so they learn).

Be extremely concise, structured, and helpful. Use markdown.
"""

    headers = {
        "Content-Type": "application/json"
    }

    models_to_try = [
        "gemma-4-31b-it",
        "gemma-4-26b-a4b-it",
        "gemini-3.5-flash",
        "gemini-2.5-flash"
    ]

    last_error_msg = ""
    last_status_code = 500

    for model in models_to_try:
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.1
            }
        }

        try:
            try:
                import urllib3.util.connection as connection
                connection.HAS_IPV6 = False
            except Exception:
                pass
            
            response = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=60,
                proxies={"http": None, "https": None}
            )
            if response.status_code == 200:
                data = response.json()
                try:
                    parts = data["candidates"][0]["content"]["parts"]
                    # Filter out thinking steps (i.e. where thought is True) to get only the final answer
                    analysis_text = "".join(part["text"] for part in parts if not part.get("thought"))
                    if not analysis_text.strip():
                        # Fallback to concatenate all parts if somehow empty
                        analysis_text = "".join(part["text"] for part in parts)
                except Exception as exc:
                    analysis_text = data["candidates"][0]["content"]["parts"][0]["text"]

                return AnalyzeResponse(analysis=analysis_text)
            else:
                try:
                    error_msg = response.json().get("error", {}).get("message", response.text)
                except Exception:
                    error_msg = response.text
                last_error_msg = f"Model '{model}' failed ({response.status_code}): {error_msg}"
                last_status_code = response.status_code
        except Exception as e:
            last_error_msg = f"Model '{model}' connection failed: {e}"
            last_status_code = 500

    raise HTTPException(
        status_code=last_status_code,
        detail=f"Gemini API returned an error: {last_error_msg}"
    )
