"""``POST /api/vscode/active`` — the cOde(n) → VSCode handoff.

The Electron renderer calls this when the user clicks the
"Open in VSCode" button, so the next time the user presses F5
in VSCode, the launch config defaults to the right challenge
id. The handoff file is ``solutions/.vscode-active`` — a
two-line JSON file the ``tools/run_solution.py`` script reads
when no id is passed on the command line.

The endpoint is intentionally tiny: it just writes a JSON
file and returns ``{ok: true}``. No validation beyond
"is this a real challenge id in the registry" (we don't
want a typo to silently leave the handoff at the wrong
value). The file is gitignored (per ``.gitignore``) so
each developer's local state stays out of the repo.
"""
from __future__ import annotations

import json
import logging

from fastapi import APIRouter
from pydantic import BaseModel

from challenges.registry import CHALLENGE_REGISTRY
from server.app.config import SOLUTIONS_DIR


log = logging.getLogger(__name__)


router = APIRouter()


_HANDOFF_FILE = ".vscode-active"
"""Name of the handoff file under ``solutions/``. A leading
dot makes it look like a hidden file (``ls -la`` / Windows
Explorer treats it as one). The file is gitignored; the
``tools/run_solution.py`` script reads it when no id is
passed on the command line."""


class ActiveChallengeRequest(BaseModel):
    challenge_id: str


class ActiveChallengeResponse(BaseModel):
    ok: bool
    path: str


@router.post("/vscode/active")
def set_active_challenge(body: ActiveChallengeRequest) -> ActiveChallengeResponse:
    """Write the active challenge id to ``solutions/_vscode-active.json``.

    Returns ``{ok: true, path: ...}`` on success. If the challenge
    id is not in the registry, returns 404 (the renderer should
    not be calling this for a non-existent challenge; this is
    a safety guard against typos).
    """
    if body.challenge_id not in CHALLENGE_REGISTRY:
        from fastapi import HTTPException
        raise HTTPException(
            status_code=404,
            detail=f"Challenge '{body.challenge_id}' not found",
        )
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    handoff_path = SOLUTIONS_DIR / _HANDOFF_FILE
    payload = json.dumps({"id": body.challenge_id}, indent=2)
    handoff_path.write_text(payload, encoding="utf-8")
    log.debug("wrote vscode active-challenge handoff: %s", handoff_path)
    return ActiveChallengeResponse(ok=True, path=str(handoff_path))
