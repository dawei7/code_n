"""``.vscode/get_active_challenge.py`` — read the cOde(n) active-challenge
handoff file and print its id (no id → empty string).

Used by the ``launch.json`` / ``tasks.json`` ``command``-type
``challengeId`` input so VSCode can auto-select the most recently edited
versioned user solution.

Reads ``.coden-data/active-challenge.json`` and falls back to scanning the
writable LeetCode overlay. Always prints exactly one line.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parent.parent
_USER_HOME = _REPO_ROOT / ".coden-data"
_HANDOFF = _USER_HOME / "active-challenge.json"
_USER_LEETCODE_ROOT = _USER_HOME / "dsa" / "leetcode"


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
    if not _USER_LEETCODE_ROOT.is_dir():
        return None
    candidates = list(_USER_LEETCODE_ROOT.glob("*/user_solutions/python_v[123].py"))
    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    frontend_id = candidates[0].parent.parent.name.split("_", 1)[0]
    return f"lc_{frontend_id}" if frontend_id.isdigit() else None


def main() -> int:
    cid = _from_handoff() or _from_most_recent_solution()
    print(cid or "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
