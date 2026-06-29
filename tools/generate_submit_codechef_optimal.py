"""Submit an authored Python3 CodeChef candidate and cache it if accepted.

The accepted source is cached for internal AST baselines only; it is not shown
in the UI and is not used as visible reference text.
"""

from __future__ import annotations

import argparse
import ast
import os
import sys
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from server.app.codechef_community import load_cached_solution, submit_python3_solution
from server.app.codechef_community import COOKIE_PATH


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", action="append", required=True, help="CodeChef problem code, e.g. BWFPF01. May be passed multiple times.")
    parser.add_argument("--submit", action="store_true", help="Actually submit authored source files to CodeChef.")
    parser.add_argument("--source-file", type=Path, required=True, help="Authored Python source to submit.")
    parser.add_argument("--force", action="store_true", help="Do not skip problems that already have a cached community/generated baseline.")
    parser.add_argument("--poll-timeout", type=float, default=120.0)
    args = parser.parse_args()

    if args.submit and not os.environ.get("CODECHEF_COOKIE", "").strip() and not COOKIE_PATH.is_file():
        raise SystemExit("Set CODECHEF_COOKIE or create docs/algorithms/codechef/.codechef_cookie before using --submit.")
    source = args.source_file.read_text(encoding="utf-8")
    ast.parse(source)

    codes = [code.upper() for code in args.code]
    for code in codes:
        challenge_id = f"cc_{code}"
        if not args.force and load_cached_solution(challenge_id):
            print(f"{code}: skipped, cached baseline already exists", flush=True)
            continue

        if not args.submit:
            print(f"{code}: authored candidate parses ({len(source)} chars). Re-run with --submit to post to CodeChef.", flush=True)
            continue

        try:
            result = submit_python3_solution(
                challenge_id,
                source,
                poll_timeout=args.poll_timeout,
            )
            verdict = result.get("verdict") or {}
            verdict_text = verdict.get("result_code") or verdict.get("message") or verdict.get("status")
            print(f"{code}: {'accepted' if result.get('accepted') else 'not accepted'} ({verdict_text})", flush=True)
            if result.get("source_url"):
                print(f"{code}: {result['source_url']}", flush=True)
        except (requests.RequestException, ValueError, SyntaxError) as exc:
            print(f"{code}: submit failed: {type(exc).__name__}: {exc}", flush=True)


if __name__ == "__main__":
    main()
