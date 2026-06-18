"""``.vscode/get_active_challenge.py`` — read the cOde(n) active-challenge
handoff file and print its id (no id → empty string).

Used by the ``launch.json`` / ``tasks.json`` ``command``-type
``challengeId`` input so VSCode auto-selects the right
``solutions/<id>.py`` for F5 without showing a prompt.

Reads ``solutions/.vscode-active`` (the file cOde(n)'s
"Open in VSCode" button writes). Falls back to scanning
``solutions/*.py`` for the most-recently-modified file if the
handoff is missing (e.g. the user opened VSCode directly
without going through cOde(n) first). Always prints exactly
one line so the ``command`` input captures it cleanly.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parent.parent
_HANDOFF = _REPO_ROOT / "solutions" / ".vscode-active"
_SOLUTIONS_DIR = _REPO_ROOT / "solutions"


def _from_handoff() -> str | None:
    if not _HANDOFF.is_file():
        return None
    try:
        payload = json.loads(_HANDOFF.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    cid = payload.get("id") if isinstance(payload, dict) else None
    return cid if isinstance(cid, str) and cid else None


def _from_most_recent_solution() -> str | None:
    if not _SOLUTIONS_DIR.is_dir():
        return None
    candidates = [
        p for p in _SOLUTIONS_DIR.iterdir()
        if p.is_file() and p.suffix == ".py" and not p.name.startswith(".")
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0].stem


def main() -> int:
    cid = _from_handoff() or _from_most_recent_solution()
    print(cid or "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())