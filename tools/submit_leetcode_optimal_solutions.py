"""Submit local Python LeetCode optimal solutions to the real LeetCode judge.

The script is intentionally opt-in:

* default mode is a dry run that fetches LeetCode metadata and builds the
  submitted source without posting it;
* real submissions require ``--submit`` plus a user-provided LeetCode cookie;
* only normal ``class Solution`` Python3 problems are adapted automatically.

Set either ``LEETCODE_COOKIE`` to a raw cookie header containing
``LEETCODE_SESSION`` and ``csrftoken``, or set ``LEETCODE_SESSION`` and
``LEETCODE_CSRF_TOKEN`` separately. As a local alternative, place the raw
cookie header in ``dsa/leetcode/_local/.leetcode_cookie``.

LeetCode submissions are paced conservatively: real submissions wait at least
10 seconds between posts, with a 15 second default cushion. The last submit
timestamp is kept in a local gitignored state file so resumed batches respect
the same cadence.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from challenges.registry import CHALLENGE_REGISTRY  # noqa: E402
from server.app.optimal_sources import organized_solution_path  # noqa: E402


GRAPHQL_URL = "https://leetcode.com/graphql"
BASE_URL = "https://leetcode.com"
COOKIE_PATH = ROOT / "dsa" / "leetcode" / "_local" / ".leetcode_cookie"
RESULTS_PATH = ROOT / "dsa" / "leetcode" / "_reports" / "leetcode_submission_results.jsonl"
SUBMIT_STATE_PATH = ROOT / "dsa" / "leetcode" / "_local" / ".leetcode_submit_state.json"
FREE_ACCOUNT_MIN_SUBMIT_DELAY_SECONDS = 10.0
DEFAULT_SUBMIT_DELAY_SECONDS = 15.0
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/149.0.0.0 Safari/537.36"
)

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    codeSnippets {
      lang
      langSlug
      code
    }
  }
}
"""


class LeetCodeSubmitError(RuntimeError):
    pass


class UnsupportedProblemShape(RuntimeError):
    pass


@dataclass(frozen=True)
class MethodInfo:
    name: str
    params: tuple[str, ...]


def _leetcode_sort_key(challenge_id: str) -> tuple[int, str]:
    try:
        return int(challenge_id.removeprefix("lc_")), challenge_id
    except ValueError:
        return 10**9, challenge_id


def _slug_from_url(url: str) -> str:
    match = re.search(r"/problems/([^/]+)/?", url)
    if not match:
        raise LeetCodeSubmitError(f"Could not read LeetCode slug from URL: {url!r}")
    return match.group(1)


def _cookie_header() -> str:
    raw = os.environ.get("LEETCODE_COOKIE", "").strip()
    if raw:
        return raw
    if COOKIE_PATH.is_file():
        return COOKIE_PATH.read_text(encoding="utf-8").strip()
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    if session and csrf:
        return f"LEETCODE_SESSION={session}; csrftoken={csrf}"
    return ""


def _csrf_from_cookie(cookie: str) -> str:
    env = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    if env:
        return env
    match = re.search(r"(?:^|;\s*)csrftoken=([^;]+)", cookie)
    return match.group(1) if match else ""


def _session(cookie: str = "") -> requests.Session:
    session = requests.Session()
    user_agent = os.environ.get("LEETCODE_USER_AGENT", "").strip() or DEFAULT_USER_AGENT
    session.headers.update(
        {
            "User-Agent": user_agent,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Origin": BASE_URL,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }
    )
    if cookie:
        session.headers["Cookie"] = cookie
    return session


def fetch_question(session: requests.Session, slug: str) -> dict[str, Any]:
    headers = {"Referer": f"{BASE_URL}/problems/{slug}/"}
    response = session.post(
        GRAPHQL_URL,
        json={"query": QUESTION_QUERY, "variables": {"titleSlug": slug}},
        headers=headers,
        timeout=25,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("errors"):
        raise LeetCodeSubmitError(json.dumps(payload["errors"], ensure_ascii=False))
    question = (payload.get("data") or {}).get("question")
    if not question:
        raise LeetCodeSubmitError(f"LeetCode did not return metadata for {slug!r}")
    return question


def _python3_snippet(question: dict[str, Any]) -> str:
    for snippet in question.get("codeSnippets") or []:
        if snippet.get("langSlug") == "python3":
            return str(snippet.get("code") or "")
    raise UnsupportedProblemShape("LeetCode did not provide a Python3 snippet.")


def _solution_method_from_snippet(snippet: str) -> MethodInfo:
    if not re.search(r"(?m)^class\s+Solution\s*:", snippet):
        raise UnsupportedProblemShape(
            "This is not a normal class Solution problem."
        )

    matches = re.findall(
        r"(?m)^\s+def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?:->\s*[^:]+)?\s*:",
        snippet,
    )
    matches = [(name, params) for name, params in matches if not name.startswith("_")]
    if len(matches) != 1:
        raise UnsupportedProblemShape("Expected exactly one public method in class Solution.")
    name, raw_params = matches[0]
    params = []
    for raw in raw_params.split(","):
        raw = raw.strip()
        if not raw or raw in {"self", "*"}:
            continue
        raw = raw.lstrip("*")
        param = re.split(r"\s*[:=]\s*", raw, maxsplit=1)[0].strip()
        if param:
            params.append(param)
    return MethodInfo(name, tuple(params))


def _solve_params(source: str) -> tuple[str, ...]:
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "solve":
            if node.args.vararg or node.args.kwarg or node.args.kwonlyargs:
                raise UnsupportedProblemShape("solve() must use plain positional parameters.")
            return tuple(arg.arg for arg in node.args.args)
    raise UnsupportedProblemShape("Local optimal source does not define solve(...).")


def _submission_prelude() -> str:
    return (
        "from typing import *\n"
        "from collections import *\n"
        "from functools import *\n"
        "from heapq import *\n"
        "from bisect import *\n"
        "from math import *\n\n"
        "from builtins import pow as pow\n\n"
    )


def _strip_future_imports(source: str) -> str:
    """Remove local ``__future__`` imports before submitting to LeetCode.

    LeetCode may prepend its own judge scaffolding before the submitted source,
    especially for object problems such as TreeNode/ListNode. A future import
    can then be rejected even when it is the first line of our generated code.
    """
    kept_lines: list[str] = []
    pattern = re.compile(r"^\s*from\s+__future__\s+import\s+(.+?)(?:\s*#.*)?$")
    for line in source.splitlines():
        if not pattern.match(line):
            kept_lines.append(line)
    return "\n".join(kept_lines).strip()


def _strip_leetcode_definition_classes(source: str, snippet: str) -> str:
    """Drop local copies of LeetCode-provided node classes before submission."""
    provided_names = {
        name
        for name in ("ListNode", "TreeNode", "Node")
        if re.search(rf"\bclass\s+{name}\b|\b{name}\b", snippet)
    }
    if not provided_names:
        return source

    tree = ast.parse(source)
    removal_lines: set[int] = set()
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name in provided_names:
            end_lineno = getattr(node, "end_lineno", node.lineno)
            removal_lines.update(range(node.lineno, end_lineno + 1))

    if not removal_lines:
        return source
    return "\n".join(
        line for line_no, line in enumerate(source.splitlines(), start=1) if line_no not in removal_lines
    ).strip()


def _top_level_class_names(source: str) -> list[str]:
    tree = ast.parse(source)
    return [node.name for node in tree.body if isinstance(node, ast.ClassDef)]


def _design_class_from_snippet(snippet: str) -> str:
    class_names = [
        name
        for name in re.findall(r"(?m)^class\s+([A-Za-z_]\w*)\s*(?:\([^)]*\))?\s*:", snippet)
        if name not in {"ListNode", "TreeNode", "Node"}
    ]
    if "Solution" in class_names:
        raise UnsupportedProblemShape("Normal Solution snippets should use solve() wrapping.")
    if len(class_names) != 1:
        raise UnsupportedProblemShape(
            "Expected exactly one LeetCode design class in the Python3 snippet."
        )
    return class_names[0]


def _strip_top_level_functions(source: str, names: set[str]) -> str:
    if not names:
        return source
    tree = ast.parse(source)
    removal_lines: set[int] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
            end_lineno = getattr(node, "end_lineno", node.lineno)
            removal_lines.update(range(node.lineno, end_lineno + 1))
    if not removal_lines:
        return source
    return "\n".join(
        line for line_no, line in enumerate(source.splitlines(), start=1) if line_no not in removal_lines
    ).strip()


def _build_design_submission_source(local_source: str, snippet: str) -> str:
    design_class = _design_class_from_snippet(snippet)
    source = _strip_future_imports(local_source)
    if design_class not in _top_level_class_names(source):
        raise UnsupportedProblemShape(
            f"LeetCode expects class {design_class}, but local source does not define it."
        )
    source = _strip_top_level_functions(source, {"solve"})
    wrapped = f"{_submission_prelude()}{source}\n"
    ast.parse(wrapped)
    return wrapped


def build_submission_source(local_source: str, snippet: str) -> str:
    if not re.search(r"(?m)^class\s+Solution\s*:", snippet):
        return _build_design_submission_source(local_source, snippet)

    method = _solution_method_from_snippet(snippet)
    solve_params = _solve_params(local_source)
    if len(method.params) != len(solve_params):
        raise UnsupportedProblemShape(
            "Parameter count differs between local solve() and LeetCode's Python3 method: "
            f"{len(solve_params)} local vs {len(method.params)} LeetCode."
        )

    method_args = ", ".join(method.params)
    if set(method.params) == set(solve_params):
        call_args = ", ".join(f"{param}={param}" for param in solve_params)
    else:
        call_args = ", ".join(method.params)
    if method_args:
        signature = f"self, {method_args}"
    else:
        signature = "self"

    source = _strip_future_imports(local_source)
    source = _strip_leetcode_definition_classes(source, snippet)
    wrapped = (
        _submission_prelude()
        +
        f"{source}\n\n\n"
        "class Solution:\n"
        f"    def {method.name}({signature}):\n"
        f"        return solve({call_args})\n"
    )
    ast.parse(wrapped)
    return wrapped


def _challenge_source(challenge_id: str) -> tuple[str, Path]:
    path = organized_solution_path(challenge_id, "python")
    if path is None or not path.is_file():
        raise LeetCodeSubmitError(f"{challenge_id}: no file-backed Python optimal source found.")
    return path.read_text(encoding="utf-8"), path


def _challenge_slug(challenge_id: str) -> str:
    if challenge_id not in CHALLENGE_REGISTRY:
        raise LeetCodeSubmitError(f"Unknown challenge id: {challenge_id}")
    spec = CHALLENGE_REGISTRY[challenge_id]()._spec
    if not spec.source_url:
        raise LeetCodeSubmitError(f"{challenge_id}: missing LeetCode source URL.")
    return _slug_from_url(spec.source_url)


def prepare_submission(challenge_id: str, session: requests.Session) -> dict[str, Any]:
    slug = _challenge_slug(challenge_id)
    local_source, path = _challenge_source(challenge_id)
    question = fetch_question(session, slug)
    snippet = _python3_snippet(question)
    typed_code = build_submission_source(local_source, snippet)
    return {
        "challenge_id": challenge_id,
        "source_path": str(path.relative_to(ROOT)),
        "slug": slug,
        "question_id": str(question["questionId"]),
        "frontend_id": str(question["questionFrontendId"]),
        "title": str(question["title"]),
        "typed_code": typed_code,
    }


def submit_prepared(
    prepared: dict[str, Any],
    session: requests.Session,
    csrf_token: str,
    poll_timeout: float,
) -> dict[str, Any]:
    slug = prepared["slug"]
    submit_url = f"{BASE_URL}/problems/{slug}/submit/"
    headers = {
        "Referer": f"{BASE_URL}/problems/{slug}/",
        "X-CSRFToken": csrf_token,
    }
    payload = {
        "lang": "python3",
        "question_id": prepared["question_id"],
        "typed_code": prepared["typed_code"],
    }
    response = session.post(submit_url, json=payload, headers=headers, timeout=30)
    if response.status_code >= 400:
        detail = response.text.strip().replace("\n", " ")[:500]
        raise LeetCodeSubmitError(f"submit HTTP {response.status_code}: {detail}")
    data = response.json()
    submission_id = data.get("submission_id")
    if not submission_id:
        raise LeetCodeSubmitError(f"Submit response did not contain submission_id: {data}")

    deadline = time.monotonic() + poll_timeout
    check_url = f"{BASE_URL}/submissions/detail/{submission_id}/check/"
    last = {}
    while time.monotonic() < deadline:
        check = session.get(
            check_url,
            headers={"Referer": f"{BASE_URL}/submissions/detail/{submission_id}/"},
            timeout=30,
        )
        if check.status_code >= 400:
            detail = check.text.strip().replace("\n", " ")[:500]
            raise LeetCodeSubmitError(f"poll HTTP {check.status_code}: {detail}")
        last = check.json()
        state = last.get("state")
        if state == "SUCCESS":
            return {
                "submission_id": submission_id,
                "accepted": last.get("status_msg") == "Accepted",
                "verdict": last,
                "source_url": f"{BASE_URL}/submissions/detail/{submission_id}/",
            }
        if state == "FAILURE":
            return {
                "submission_id": submission_id,
                "accepted": False,
                "verdict": last,
                "source_url": f"{BASE_URL}/submissions/detail/{submission_id}/",
            }
        time.sleep(1.5)
    raise LeetCodeSubmitError(f"Timed out waiting for submission {submission_id}: {last}")


def append_result(result: dict[str, Any]) -> None:
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with RESULTS_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")


def _load_last_submit_epoch(path: Path = SUBMIT_STATE_PATH) -> float:
    if not path.is_file():
        return 0.0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        return float(payload.get("last_submit_epoch") or 0.0)
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return 0.0


def _save_last_submit_epoch(epoch: float, path: Path = SUBMIT_STATE_PATH) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = path.with_name(path.name + ".tmp")
        temp_path.write_text(
            json.dumps({"last_submit_epoch": epoch}, sort_keys=True),
            encoding="utf-8",
        )
        temp_path.replace(path)
    except OSError as exc:
        print(f"Warning: could not update LeetCode submit state: {exc}", flush=True)


def _effective_submit_delay(requested_delay: float) -> float:
    return max(requested_delay, FREE_ACCOUNT_MIN_SUBMIT_DELAY_SECONDS)


def _wait_for_submit_slot(last_submit_epoch: float, submit_delay: float, challenge_id: str) -> None:
    remaining_delay = submit_delay - (time.time() - last_submit_epoch)
    if remaining_delay > 0:
        print(
            f"{challenge_id}: waiting {remaining_delay:.1f}s for LeetCode submit pacing.",
            flush=True,
        )
        time.sleep(remaining_delay)


def _is_rate_or_block_error(exc: BaseException) -> bool:
    message = str(exc).lower()
    return (
        "http 429" in message
        or "http 403" in message
        or "cloudflare" in message
        or "just a moment" in message
    )


def _accepted_ids_from_results(path: Path = RESULTS_PATH) -> set[str]:
    accepted: set[str] = set()
    if not path.is_file():
        return accepted
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("accepted") and record.get("challenge_id"):
            accepted.add(str(record["challenge_id"]))
    return accepted


def _all_python_optimal_ids() -> list[str]:
    ids: list[str] = []
    for challenge_id in CHALLENGE_REGISTRY:
        if not challenge_id.startswith("lc_"):
            continue
        path = organized_solution_path(challenge_id, "python")
        if path is not None and path.is_file():
            ids.append(challenge_id)
    return sorted(ids, key=_leetcode_sort_key)


def _ids_from_file(path: Path) -> list[str]:
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        cleaned = line.strip()
        if not cleaned or cleaned.startswith("#"):
            continue
        ids.append(cleaned.split()[0].strip(","))
    return ids


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", action="append", dest="ids", help="Challenge id to check, e.g. lc_1. Repeatable.")
    parser.add_argument("--id-file", type=Path, help="Text file with one challenge id per line.")
    parser.add_argument("--all-ready", action="store_true", help="Use every LeetCode challenge that has a Python optimal file.")
    parser.add_argument("--skip-accepted", action="store_true", help="Skip ids already accepted in leetcode_submission_results.jsonl.")
    parser.add_argument("--start-after", help="Skip ids through and including this challenge id.")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of ids to process after filtering.")
    parser.add_argument("--submit", action="store_true", help="Actually submit to LeetCode. Default is dry-run only.")
    parser.add_argument("--poll-timeout", type=float, default=120.0)
    parser.add_argument("--initial-delay", type=float, default=0.0, help="Seconds to wait before the first real submit.")
    parser.add_argument(
        "--submit-delay",
        type=float,
        default=DEFAULT_SUBMIT_DELAY_SECONDS,
        help=(
            "Seconds between real LeetCode submissions. Defaults to 15.0 and "
            "values below 10.0 are clamped for pacing."
        ),
    )
    parser.add_argument("--write-results", action="store_true", help="Append real submission results to a gitignored jsonl file.")
    parser.add_argument("--print-code", action="store_true", help="Print generated LeetCode source in dry-run mode.")
    parser.add_argument(
        "--continue-after-rate-limit",
        action="store_true",
        help="Keep submitting after HTTP 429/403 responses. Default stops the batch.",
    )
    args = parser.parse_args()

    ids: list[str] = []
    if args.all_ready:
        ids.extend(_all_python_optimal_ids())
    if args.id_file:
        ids.extend(_ids_from_file(args.id_file))
    if args.ids:
        ids.extend(args.ids)
    ids = list(dict.fromkeys(ids))
    if args.start_after:
        try:
            start_index = ids.index(args.start_after)
            ids = ids[start_index + 1 :]
        except ValueError:
            pass
    if args.skip_accepted:
        accepted = _accepted_ids_from_results()
        ids = [challenge_id for challenge_id in ids if challenge_id not in accepted]
    if args.limit is not None:
        ids = ids[: max(0, args.limit)]

    if not ids:
        raise SystemExit(
            "No challenge ids selected. Pass --id lc_1, --id-file ids.txt, or --all-ready."
        )

    cookie = _cookie_header()
    csrf = _csrf_from_cookie(cookie)
    if args.submit and (not cookie or not csrf):
        raise SystemExit(
            "Real submissions require LEETCODE_COOKIE or dsa/leetcode/_local/.leetcode_cookie "
            "with LEETCODE_SESSION and csrftoken."
        )

    session = _session(cookie)
    last_submit_epoch = 0.0
    submit_delay = _effective_submit_delay(args.submit_delay)
    if args.submit:
        if submit_delay != args.submit_delay:
            print(
                f"Requested --submit-delay {args.submit_delay:.1f}s is below LeetCode pacing; "
                f"using {submit_delay:.1f}s.",
                flush=True,
            )
        print(f"LeetCode submit pacing: {submit_delay:.1f}s minimum between real submissions.", flush=True)
        last_submit_epoch = _load_last_submit_epoch()
    if args.submit and args.initial_delay > 0:
        print(f"Waiting {args.initial_delay:.1f}s before first submit.", flush=True)
        time.sleep(args.initial_delay)
    print(f"Selected {len(ids)} challenge(s).", flush=True)
    for challenge_id in ids:
        prepared: dict[str, Any] | None = None
        try:
            prepared = prepare_submission(challenge_id, session)
            print(
                f"{challenge_id}: prepared LeetCode {prepared['frontend_id']} "
                f"{prepared['slug']} from {prepared['source_path']}",
                flush=True,
            )
            if args.print_code and not args.submit:
                print(prepared["typed_code"])
            if not args.submit:
                continue

            last_submit_epoch = max(last_submit_epoch, _load_last_submit_epoch())
            _wait_for_submit_slot(last_submit_epoch, submit_delay, challenge_id)
            try:
                submitted = submit_prepared(prepared, session, csrf, args.poll_timeout)
            finally:
                last_submit_epoch = time.time()
                _save_last_submit_epoch(last_submit_epoch)
            verdict = submitted["verdict"].get("status_msg") or submitted["verdict"].get("state")
            print(
                f"{challenge_id}: {'accepted' if submitted['accepted'] else 'not accepted'} "
                f"({verdict}) {submitted['source_url']}",
                flush=True,
            )
            result = {
                **{key: prepared[key] for key in ("challenge_id", "source_path", "slug", "frontend_id", "title")},
                **submitted,
            }
            if args.write_results:
                append_result(result)
        except (requests.RequestException, LeetCodeSubmitError, UnsupportedProblemShape, SyntaxError) as exc:
            print(f"{challenge_id}: skipped/failed: {type(exc).__name__}: {exc}", flush=True)
            if args.submit and args.write_results and prepared is not None and isinstance(exc, LeetCodeSubmitError):
                append_result(
                    {
                        **{
                            key: prepared[key]
                            for key in ("challenge_id", "source_path", "slug", "frontend_id", "title")
                        },
                        "accepted": False,
                        "submission_id": "",
                        "source_url": "",
                        "verdict": {"status_msg": "Submit Error", "state": "FAILURE"},
                        "error": str(exc),
                    }
                )
            if args.submit and _is_rate_or_block_error(exc) and not args.continue_after_rate_limit:
                print("Stopping batch after LeetCode rate-limit/block response.", flush=True)
                break


if __name__ == "__main__":
    main()
