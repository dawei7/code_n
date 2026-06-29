"""Internal CodeChef community-solution baselines.

These sources are never returned to the frontend. They are used only as an
optional AST baseline when CodeChef exposes an accepted Python solution through
the authenticated submissions APIs.
"""

from __future__ import annotations

import ast
import json
import os
import re
import time
import threading
from functools import lru_cache
from pathlib import Path
from typing import Any

import requests


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CACHE_PATH = PROJECT_ROOT / "docs" / "algorithms" / "codechef" / "community_optimal_solutions.json"
COOKIE_PATH = PROJECT_ROOT / "docs" / "algorithms" / "codechef" / ".codechef_cookie"
INDEX_PATH = PROJECT_ROOT / "docs" / "algorithms" / "codechef" / "index.json"
OPTIMAL_CODECHEF_ROOT = PROJECT_ROOT / "optimal_solutions" / "codechef"
BASE_URL = "https://www.codechef.com"
PYTHON_LANGUAGE_TOKENS = ("PYTH", "PYPY", "PYTHON")
_LOCK = threading.Lock()


def _problem_code(challenge_id: str) -> str:
    return challenge_id[3:] if challenge_id.startswith("cc_") else challenge_id


def _is_python3_language(value: Any) -> bool:
    if isinstance(value, dict):
        text = " ".join(str(v) for v in value.values())
    else:
        text = str(value or "")
    upper = text.upper()
    if "PYTH" in upper or "PYTHON" in upper:
        return "2" not in upper
    return "PYPY3" in upper or upper == "PYPY"


def _submission_id(row: dict[str, Any]) -> str:
    for key in ("id", "submission_id", "submissionId", "submissionID"):
        value = row.get(key)
        if value:
            return str(value)
    return ""


def _numeric(row: dict[str, Any], *keys: str) -> float:
    for key in keys:
        value = row.get(key)
        if value is None:
            continue
        try:
            return float(value)
        except (TypeError, ValueError):
            continue
    return 0.0


def _looks_accepted(row: dict[str, Any]) -> bool:
    result_code = row.get("result_code")
    try:
        # CodeChef uses different result-code vocabularies in different
        # endpoints: explained-solution rows use 1 for Accepted, while the
        # status filter uses 15.
        if int(result_code) in {1, 15}:
            return True
    except (TypeError, ValueError):
        pass
    haystack = " ".join(str(value) for value in row.values()).lower()
    if "partial_accepted" in haystack or "partially accepted" in haystack:
        return False
    return bool(re.search(r"\b(?:accepted|ac)\b", haystack))


def _popularity(row: dict[str, Any]) -> float:
    return _numeric(row, "score", "popularity", "upvotes", "upvote_count", "_community_upvotes")


def _session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 cOde(n) CodeChef community baseline/1.0",
        "Accept": "application/json, text/plain, */*",
        "Origin": BASE_URL,
        "Referer": f"{BASE_URL}/practice",
        "X-Requested-With": "XMLHttpRequest",
    })
    cookie = os.environ.get("CODECHEF_COOKIE", "").strip()
    if not cookie and COOKIE_PATH.is_file():
        cookie = COOKIE_PATH.read_text(encoding="utf-8").strip()
    if cookie:
        session.headers["Cookie"] = cookie
    return session


def _contest_code_for(problem_code: str, fallback: str = "PRACTICE") -> str:
    if INDEX_PATH.is_file():
        try:
            payload = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
            problems = None
            if isinstance(payload, dict):
                problems = payload.get("problems") or payload.get("questions")
            if isinstance(problems, list):
                for row in problems:
                    if not isinstance(row, dict):
                        continue
                    if str(row.get("code") or "").upper() != problem_code.upper():
                        continue
                    contest_code = str(row.get("contest_code") or "").strip()
                    if contest_code:
                        return contest_code
                    url = str(row.get("url") or "")
                    match = re.search(r"/course/[^/]+/([^/]+)/problems/", url)
                    if match:
                        return match.group(1)
                    break
        except (OSError, json.JSONDecodeError):
            pass
    return fallback


def _csrf_token(session: requests.Session, problem_code: str) -> str:
    response = session.get(f"{BASE_URL}/submit/{problem_code}", timeout=30)
    response.raise_for_status()
    match = re.search(r"window\.csrfToken\s*=\s*\"([^\"]+)\"", response.text)
    return match.group(1) if match else ""


def _load_cache() -> dict[str, Any]:
    if not CACHE_PATH.is_file():
        return {
            "source": "Best accepted CodeChef community Python3 submissions for internal AST analysis only",
            "solutions": {},
            "errors": {},
        }
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {
            "source": "Best accepted CodeChef community Python3 submissions for internal AST analysis only",
            "solutions": {},
            "errors": {},
        }


def _save_cache(cache: dict[str, Any]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_cached_solution(challenge_id: str) -> dict[str, Any] | None:
    """Return a cached community baseline for ``challenge_id``, if present."""
    cache = _load_cache()
    solution = (cache.get("solutions") or {}).get(_problem_code(challenge_id))
    return solution if isinstance(solution, dict) else None


@lru_cache(maxsize=4096)
def _load_exported_source(problem_code: str) -> str:
    if not problem_code or not OPTIMAL_CODECHEF_ROOT.is_dir():
        return ""
    for path in OPTIMAL_CODECHEF_ROOT.rglob(f"{problem_code}.py"):
        try:
            return path.read_text(encoding="utf-8")
        except OSError:
            return ""
    return ""


def load_cached_source(challenge_id: str) -> str:
    """Return cached Python source for ``challenge_id`` or an empty string."""
    exported = _load_exported_source(_problem_code(challenge_id).upper())
    if exported:
        return exported
    solution = load_cached_solution(challenge_id)
    if solution:
        return str(solution.get("source") or "")
    return ""


def _list_submissions(session: requests.Session, problem_code: str, contest_code: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for page in range(3):
        response = session.get(
            f"{BASE_URL}/api/submissions/{contest_code}/{problem_code}",
            params={
                "limit": 20,
                "page": page,
                "language": "PYTH 3",
                "status": "accepted",
            },
            timeout=20,
        )
        response.raise_for_status()
        payload = response.json()
        data = payload.get("data") or payload.get("submissions") or []
        if not isinstance(data, list):
            break
        rows.extend(row for row in data if isinstance(row, dict))
        if len(data) < 20:
            break
    return rows


def _list_explained_solutions(session: requests.Session, problem_code: str) -> list[dict[str, Any]]:
    response = session.get(
        f"{BASE_URL}/api/annotations/top",
        params={"problemCode": problem_code},
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    rows = payload.get("annotations") or payload.get("data") or []
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def _annotation_votes(session: requests.Session, submission_id: str) -> int:
    try:
        response = session.get(
            f"{BASE_URL}/api/annotations",
            params={"submission_id": submission_id},
            timeout=10,
        )
        if response.status_code >= 400:
            return 0
        payload = response.json()
        return int(payload.get("upvote_count") or 0)
    except (requests.RequestException, ValueError, TypeError, json.JSONDecodeError):
        return 0


def _code_for_submission(session: requests.Session, submission_id: str) -> tuple[str, str]:
    response = session.get(f"{BASE_URL}/api/submission-code/{submission_id}", timeout=20)
    response.raise_for_status()
    payload = response.json()
    data = payload.get("data") or payload
    source = str(data.get("code") or data.get("source") or "")
    language = data.get("language") or data.get("lang") or "PYTH 3"
    if isinstance(language, dict):
        language = str(language.get("name") or language.get("short_name") or language)
    return source, str(language)


def _python3_language_id(session: requests.Session, problem_code: str, contest_code: str, *, prefer_pypy: bool = False) -> str:
    response = session.get(
        f"{BASE_URL}/api/ide/{contest_code}/languages/{problem_code}",
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    languages = payload.get("languages") or []
    pypy_candidate = ""
    python_candidate = ""
    for language in languages:
        if not isinstance(language, dict):
            continue
        label = " ".join(str(language.get(key) or "") for key in ("short_name", "short_qualified_name", "full_name"))
        if not _is_python3_language(label):
            continue
        language_id = str(language.get("id") or "")
        if not language_id:
            continue
        if "PYPY" in label.upper() or "PYP3" in label.upper():
            pypy_candidate = pypy_candidate or language_id
        else:
            python_candidate = python_candidate or language_id
    if prefer_pypy and pypy_candidate:
        return pypy_candidate
    if python_candidate:
        return python_candidate
    if pypy_candidate:
        return pypy_candidate
    raise ValueError(f"CodeChef did not advertise a Python3 language for {problem_code}.")


def _cache_solution(problem_code: str, solution: dict[str, Any]) -> dict[str, Any]:
    cache = _load_cache()
    cache.setdefault("solutions", {})[problem_code] = solution
    cache.setdefault("errors", {}).pop(problem_code, None)
    _save_cache(cache)
    return solution


def _ranked_candidates(session: requests.Session, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    candidates = [
        row for row in rows
        if _submission_id(row)
        and _looks_accepted(row)
        and (
            _is_python3_language(row.get("language"))
            or _is_python3_language(row.get("language_name"))
            or _is_python3_language(row.get("languageName"))
        )
    ]
    for row in candidates[:20]:
        if _popularity(row) <= 0:
            row["_community_upvotes"] = _annotation_votes(session, _submission_id(row))
    return sorted(
        candidates,
        key=lambda row: (
            _popularity(row),
            _numeric(row, "points", "score"),
            -_numeric(row, "time", "execution_time", "cpu_time"),
            -_numeric(row, "memory", "memory_used"),
        ),
        reverse=True,
    )


def refresh_best_python3_solution(challenge_id: str, contest_code: str = "PRACTICE") -> dict[str, Any] | None:
    """Fetch and cache the highest-ranked accepted Python3 community solution.

    The request needs an authenticated CodeChef session. The app reads it from
    ``CODECHEF_COOKIE`` when available. Without that cookie CodeChef currently
    responds with 403, which is recorded as a non-fatal cache error.
    """
    problem_code = _problem_code(challenge_id)
    with _LOCK:
        cache = _load_cache()
        session = _session()
        try:
            rows = _list_explained_solutions(session, problem_code)
            selection = "most popular explained CodeChef Python3 solution"
            if not rows:
                rows = _list_submissions(session, problem_code, contest_code)
                selection = "most popular accepted Python3 community submission"
            candidates = _ranked_candidates(session, rows)
            last_syntax_error = ""
            for row in candidates:
                submission_id = _submission_id(row)
                source, language = _code_for_submission(session, submission_id)
                if not _is_python3_language(language):
                    continue
                try:
                    ast.parse(source)
                except SyntaxError as exc:
                    last_syntax_error = f"SyntaxError: {exc}"
                    continue
                solution = {
                    "language": language,
                    "source": source.rstrip() + "\n",
                    "submission_id": submission_id,
                    "source_url": f"{BASE_URL}/viewsolution/{submission_id}",
                    "selection": selection,
                    "popularity": _popularity(row),
                    "upvotes": int(row.get("_community_upvotes") or row.get("upvote_count") or 0),
                    "points": _numeric(row, "points", "score"),
                }
                return _cache_solution(problem_code, solution)
            cache.setdefault("errors", {})[problem_code] = last_syntax_error or "No accepted Python3 community submission found."
            _save_cache(cache)
        except (requests.RequestException, json.JSONDecodeError, ValueError) as exc:
            message = re.sub(r"\s+", " ", str(exc)).strip()
            cache.setdefault("errors", {})[problem_code] = message or type(exc).__name__
            _save_cache(cache)
    return None


def submit_python3_solution(
    challenge_id: str,
    source: str,
    contest_code: str | None = None,
    *,
    poll_timeout: float = 120.0,
    poll_interval: float = 3.0,
    prefer_pypy: bool = False,
) -> dict[str, Any]:
    """Submit Python3 source to CodeChef and cache it if accepted.

    This intentionally performs an external account action. It requires an
    authenticated CodeChef session through ``CODECHEF_COOKIE``.
    """
    ast.parse(source)
    problem_code = _problem_code(challenge_id)
    resolved_contest_code = contest_code or _contest_code_for(problem_code)
    session = _session()
    language_id = _python3_language_id(
        session,
        problem_code,
        resolved_contest_code,
        prefer_pypy=prefer_pypy,
    )
    csrf_token = _csrf_token(session, problem_code)
    submit_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    if csrf_token:
        submit_headers["X-CSRF-Token"] = csrf_token

    response = session.post(
        f"{BASE_URL}/api/ide/submit",
        data={
            "sourceCode": source,
            "language": language_id,
            "problemCode": problem_code,
            "contestCode": resolved_contest_code,
        },
        headers=submit_headers,
        timeout=30,
    )
    response.raise_for_status()
    initial = response.json()
    if initial.get("status") == "error":
        if _looks_accepted(initial):
            cached = _cache_solution(problem_code, {
                "language": "PYTH 3",
                "source": source.rstrip() + "\n",
                "submission_id": "",
                "source_url": "",
                "selection": "generated Python3 solution accepted by CodeChef",
                "upvotes": 0,
                "points": _numeric(initial, "points", "score"),
            })
            return {
                "accepted": True,
                "problem_code": problem_code,
                "contest_code": resolved_contest_code,
                "initial": initial,
                "verdict": initial,
                "cached": cached,
            }
        return {
            "accepted": False,
            "problem_code": problem_code,
            "contest_code": resolved_contest_code,
            "initial": initial,
            "verdict": initial,
        }

    submission_id = str(initial.get("upid") or initial.get("solution_id") or initial.get("id") or "")
    if not submission_id:
        if _looks_accepted(initial):
            cached = _cache_solution(problem_code, {
                "language": "PYTH 3",
                "source": source.rstrip() + "\n",
                "submission_id": "",
                "source_url": "",
                "selection": "generated Python3 solution accepted by CodeChef",
                "upvotes": 0,
                "points": _numeric(initial, "points", "score"),
            })
            return {
                "accepted": True,
                "problem_code": problem_code,
                "contest_code": resolved_contest_code,
                "initial": initial,
                "verdict": initial,
                "cached": cached,
            }
        return {
            "accepted": False,
            "problem_code": problem_code,
            "contest_code": resolved_contest_code,
            "initial": initial,
            "verdict": initial,
            "error": "CodeChef response did not include a submission id.",
        }

    deadline = time.monotonic() + poll_timeout
    verdict = initial
    while time.monotonic() < deadline:
        time.sleep(poll_interval)
        poll = session.get(
            f"{BASE_URL}/api/ide/submit",
            params={"solution_id": submission_id},
            timeout=30,
        )
        poll.raise_for_status()
        verdict = poll.json()
        result_code = str(verdict.get("result_code") or verdict.get("message") or "").lower()
        if result_code not in {"wait", "pending", "queued", ""}:
            break

    result_code = str(verdict.get("result_code") or verdict.get("message") or "").lower()
    accepted = result_code == "accepted" or _looks_accepted(verdict)
    result = {
        "accepted": accepted,
        "problem_code": problem_code,
        "contest_code": resolved_contest_code,
        "submission_id": submission_id,
        "source_url": f"{BASE_URL}/viewsolution/{submission_id}",
        "initial": initial,
        "verdict": verdict,
    }
    if accepted:
        result["cached"] = _cache_solution(problem_code, {
            "language": "PYTH 3",
            "source": source.rstrip() + "\n",
            "submission_id": submission_id,
            "source_url": f"{BASE_URL}/viewsolution/{submission_id}",
            "selection": "generated Python3 solution accepted by CodeChef",
            "upvotes": 0,
            "points": _numeric(verdict, "points", "score"),
        })
    return result
