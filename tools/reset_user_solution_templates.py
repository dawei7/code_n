"""Reset existing personal LeetCode versions to current generated starters.

This is an intentionally destructive developer utility for test profiles. It
touches only existing version files below the selected ``CODEN_HOME`` and does
not modify progress, canonical packages, or unrelated legacy provider files.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


VERSION_FILE_RE = re.compile(
    r"^(python|cpp|java|csharp|javascript|go|kotlin)_v[123]\.[A-Za-z0-9]+$"
)
PROBLEM_DIR_RE = re.compile(r"^(\d+)_")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--user-data-root",
        type=Path,
        default=Path(".coden-data"),
        help="Profile root containing dsa/leetcode (default: .coden-data).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Perform the reset. Without this flag, only report targets.",
    )
    return parser


def main() -> int:
    args = _parser().parse_args()
    profile_root = args.user_data_root.resolve()
    solution_root = (profile_root / "dsa" / "leetcode").resolve()
    if solution_root != profile_root and profile_root not in solution_root.parents:
        raise RuntimeError("Resolved solution root escaped the selected profile")
    if not solution_root.is_dir():
        print(json.dumps({"profile": str(profile_root), "files": 0, "applied": False}))
        return 0

    # Configuration is resolved at import time, so select the profile first.
    os.environ["CODEN_HOME"] = str(profile_root)

    from challenges.registry import CHALLENGE_REGISTRY
    from server.app.routes.solutions import _get_starter

    targets: list[tuple[Path, str, str]] = []
    for solution_dir in solution_root.glob("*/user_solutions"):
        if not solution_dir.is_dir() or solution_dir.is_symlink():
            continue
        resolved_dir = solution_dir.resolve()
        if solution_root not in resolved_dir.parents:
            raise RuntimeError("User solution path escaped the selected profile")
        problem_match = PROBLEM_DIR_RE.match(solution_dir.parent.name)
        if problem_match is None:
            continue
        challenge_id = f"lc_{int(problem_match.group(1))}"
        if challenge_id not in CHALLENGE_REGISTRY:
            continue
        for path in solution_dir.iterdir():
            match = VERSION_FILE_RE.match(path.name)
            if path.is_file() and not path.is_symlink() and match:
                targets.append((path, challenge_id, match.group(1)))

    starters: dict[tuple[str, str], str] = {}
    if args.apply:
        for path, challenge_id, language in targets:
            key = (challenge_id, language)
            if key not in starters:
                starters[key] = _get_starter(
                    CHALLENGE_REGISTRY[challenge_id](),
                    language,
                )
            path.write_text(starters[key], encoding="utf-8")

        for state_path in solution_root.glob("*/user_solutions/versions.json"):
            if not state_path.is_file() or state_path.is_symlink():
                continue
            try:
                state = json.loads(state_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if not isinstance(state, dict):
                continue
            changed = False
            for language_state in state.values():
                if not isinstance(language_state, dict):
                    continue
                if language_state.get("active") != 1:
                    language_state["active"] = 1
                    changed = True
                if language_state.get("names"):
                    language_state["names"] = {}
                    changed = True
            if changed:
                state_path.write_text(
                    json.dumps(state, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )

    print(
        json.dumps(
            {
                "profile": str(profile_root),
                "files": len(targets),
                "challenge_languages": len(
                    {(challenge_id, language) for _path, challenge_id, language in targets}
                ),
                "applied": bool(args.apply),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
