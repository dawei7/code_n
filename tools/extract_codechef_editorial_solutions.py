"""Extract CodeChef editorial code blocks for manual Python translation.

This helper does not translate or submit anything by itself.  It reads the
authenticated editorial text already imported into ``problem_details.json`` and
prints the best available official/setter/editorialist source block for each
requested problem.  Codex can then translate that source to Python, submit it
with ``submit_authored_codechef_solutions.py``, and only cache it after an
accepted verdict.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
DETAILS_PATH = ROOT / "docs" / "algorithms" / "codechef" / "problem_details.json"

from server.app.codechef_sources import best_codechef_source


def best_source(problem: dict[str, Any], *, prefer_python: bool = True) -> dict[str, str] | None:
    return best_codechef_source(problem, prefer_python=prefer_python)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", action="append", required=True, help="CodeChef problem code. May be passed multiple times.")
    parser.add_argument("--source-only", action="store_true", help="Print only the selected source for single-code usage.")
    args = parser.parse_args()

    data = json.loads(DETAILS_PATH.read_text(encoding="utf-8"))
    problems = data.get("problems") or {}
    results: dict[str, dict[str, str] | None] = {}
    for raw_code in args.code:
        code = raw_code.upper()
        problem = problems.get(code) or {}
        results[code] = best_source(problem)

    if args.source_only and len(results) == 1:
        selected = next(iter(results.values()))
        if not selected:
            raise SystemExit("No editorial/official source found.")
        sys.stdout.write(selected["source"])
        return

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
