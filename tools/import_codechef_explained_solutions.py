"""Cache CodeChef's most popular explained Python3 solutions.

No AI generation is used here. The script reads CodeChef's public
``/api/annotations/top`` endpoint, chooses the Python3 row with the highest
Popularity score, fetches that submission source, and stores it for internal
AST baselines only.
"""

from __future__ import annotations

import argparse
import ast
import concurrent.futures
import json
import sys
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from server.app.codechef_community import (
    BASE_URL,
    _code_for_submission,
    _is_python3_language,
    _list_explained_solutions,
    _load_cache,
    _popularity,
    _ranked_candidates,
    _save_cache,
    _session,
)


INDEX_PATH = ROOT / "docs" / "algorithms" / "codechef" / "index.json"
DETAILS_PATH = ROOT / "docs" / "algorithms" / "codechef" / "problem_details.json"
TRANSLATIONS_PATH = ROOT / "docs" / "algorithms" / "codechef" / "translated_solutions.json"
EXEMPTIONS_PATH = ROOT / "docs" / "algorithms" / "codechef" / "baseline_exemptions.json"
PYTHON_TOKENS = ("PYTH", "PYTHON", "PYPY")


def visible_codes() -> list[str]:
    data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return [str(question["code"]) for question in data.get("questions", [])]


def _has_official_python(problem: dict[str, Any]) -> bool:
    return any(
        any(token in str(solution.get("language", "")).upper() for token in PYTHON_TOKENS)
        for solution in problem.get("official_solutions", [])
    )


def missing_baseline_codes() -> list[str]:
    problems = json.loads(DETAILS_PATH.read_text(encoding="utf-8"))["problems"]
    translations = {}
    if TRANSLATIONS_PATH.is_file():
        translations = json.loads(TRANSLATIONS_PATH.read_text(encoding="utf-8")).get("translations", {})
    community = _load_cache().get("solutions", {})
    exemptions = {}
    if EXEMPTIONS_PATH.is_file():
        exemptions = json.loads(EXEMPTIONS_PATH.read_text(encoding="utf-8")).get("exemptions", {})
    return [
        code for code in visible_codes()
        if not _has_official_python(problems.get(code, {}))
        and code not in translations
        and code not in community
        and code not in exemptions
    ]


def best_explained_python3_solution(code: str) -> tuple[str, dict[str, Any] | None, str]:
    session = _session()
    try:
        rows = _list_explained_solutions(session, code)
        candidates = _ranked_candidates(session, rows)
        last_error = "No explained Python3 solution"
        for row in candidates:
            submission_id = str(row.get("submission_id") or row.get("id") or "")
            if not submission_id:
                continue
            source, language = _code_for_submission(session, submission_id)
            if not _is_python3_language(language):
                continue
            try:
                ast.parse(source)
            except SyntaxError as exc:
                last_error = f"SyntaxError: {exc}"
                continue
            return code, {
                "language": language,
                "source": source.rstrip() + "\n",
                "submission_id": submission_id,
                "source_url": f"{BASE_URL}/viewsolution/{submission_id}",
                "selection": "most popular explained CodeChef Python3 solution",
                "popularity": _popularity(row),
                "upvotes": int(row.get("upvote_count") or 0),
                "points": _popularity(row),
            }, ""
        return code, None, last_error
    except Exception as exc:
        return code, None, f"{type(exc).__name__}: {exc}"


def save_result(code: str, solution: dict[str, Any] | None, error: str) -> None:
    cache = _load_cache()
    if solution:
        cache.setdefault("solutions", {})[code] = solution
        cache.setdefault("errors", {}).pop(code, None)
    else:
        cache.setdefault("errors", {})[code] = error
    _save_cache(cache)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", action="append", help="CodeChef problem code. May be passed multiple times.")
    parser.add_argument("--limit", type=int, help="Maximum number of visible problems to scan.")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between sequential CodeChef requests.")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--missing-baseline", action="store_true", help="Only scan visible problems with no official/translated/community AST baseline.")
    args = parser.parse_args()

    if args.code:
        codes = [code.upper() for code in args.code]
    elif args.missing_baseline:
        codes = missing_baseline_codes()
    else:
        codes = visible_codes()
    if args.limit is not None:
        codes = codes[: max(0, args.limit)]

    ok = 0
    missing = 0

    def handle(index: int, result: tuple[str, dict[str, Any] | None, str]) -> None:
        nonlocal ok, missing
        code, solution, error = result
        save_result(code, solution, error)
        if solution:
            ok += 1
            print(
                f"{index}/{len(codes)} {code}: {solution.get('submission_id')} "
                f"popularity={solution.get('popularity', 0)}",
                flush=True,
            )
        else:
            missing += 1
            print(f"{index}/{len(codes)} {code}: {error}", flush=True)

    if args.workers <= 1:
        for index, code in enumerate(codes, start=1):
            handle(index, best_explained_python3_solution(code))
            if args.delay and index < len(codes):
                time.sleep(args.delay)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            future_to_index = {
                pool.submit(best_explained_python3_solution, code): index
                for index, code in enumerate(codes, start=1)
            }
            for future in concurrent.futures.as_completed(future_to_index):
                handle(future_to_index[future], future.result())

    print(f"Cached: {ok}; missing: {missing}")


if __name__ == "__main__":
    main()
