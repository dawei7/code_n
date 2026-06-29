"""Submit authored CodeChef Python candidates and cache accepted ones.

This script never generates code. It submits files from
``docs/algorithms/codechef/authored_solutions`` to CodeChef and relies on
CodeChef's verdict before marking a candidate as an internal AST baseline.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import sys
import time
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from server.app.codechef_community import COOKIE_PATH, load_cached_solution, submit_python3_solution


AUTHORED_ROOT = ROOT / "docs" / "algorithms" / "codechef" / "authored_solutions"
EXEMPTIONS_PATH = ROOT / "docs" / "algorithms" / "codechef" / "baseline_exemptions.json"


def authored_files() -> list[Path]:
    if not AUTHORED_ROOT.is_dir():
        return []
    return sorted(AUTHORED_ROOT.glob("*.py"))


def baseline_exemptions() -> dict[str, str]:
    if not EXEMPTIONS_PATH.is_file():
        return {}
    data = json.loads(EXEMPTIONS_PATH.read_text(encoding="utf-8"))
    return {
        str(code).upper(): str(reason)
        for code, reason in data.get("exemptions", {}).items()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", action="append", help="Only submit this CodeChef code. May be passed multiple times.")
    parser.add_argument("--force", action="store_true", help="Submit even if an accepted baseline is already cached.")
    parser.add_argument("--poll-timeout", type=float, default=120.0)
    parser.add_argument("--submit-delay", type=float, default=3.2, help="Seconds to wait between submissions.")
    parser.add_argument("--pypy", action="store_true", help="Submit with PyPy 3 when CodeChef offers it.")
    args = parser.parse_args()

    if not os.environ.get("CODECHEF_COOKIE", "").strip() and not COOKIE_PATH.is_file():
        raise SystemExit("Set CODECHEF_COOKIE or create docs/algorithms/codechef/.codechef_cookie before submitting.")

    wanted = {code.upper() for code in args.code} if args.code else None
    files = [path for path in authored_files() if wanted is None or path.stem.upper() in wanted]
    if not files:
        raise SystemExit("No authored solution files matched.")

    exemptions = baseline_exemptions()
    last_submit_at = 0.0
    for path in files:
        code = path.stem.upper()
        challenge_id = f"cc_{code}"
        if code in exemptions:
            print(f"{code}: skipped, baseline-exempt ({exemptions[code]})", flush=True)
            continue
        if not args.force and load_cached_solution(challenge_id):
            print(f"{code}: skipped, cached baseline already exists", flush=True)
            continue
        source = path.read_text(encoding="utf-8")
        ast.parse(source)
        try:
            remaining_delay = args.submit_delay - (time.monotonic() - last_submit_at)
            if remaining_delay > 0:
                time.sleep(remaining_delay)
            result = submit_python3_solution(
                challenge_id,
                source,
                poll_timeout=args.poll_timeout,
                prefer_pypy=args.pypy,
            )
            last_submit_at = time.monotonic()
            verdict = result.get("verdict") or {}
            verdict_text = (
                verdict.get("result_code")
                or verdict.get("message")
                or ", ".join(str(error) for error in verdict.get("errors") or [])
                or verdict.get("status")
            )
            print(f"{code}: {'accepted' if result.get('accepted') else 'not accepted'} ({verdict_text})", flush=True)
            if result.get("source_url"):
                print(f"{code}: {result['source_url']}", flush=True)
        except (requests.RequestException, ValueError, SyntaxError) as exc:
            print(f"{code}: submit failed: {type(exc).__name__}: {exc}", flush=True)


if __name__ == "__main__":
    main()
