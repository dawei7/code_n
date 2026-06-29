"""Download normalized statements, samples, editorials, and official solutions.

The importer is resumable: each successful response is cached independently
before the final compact ``problem_details.json`` file is assembled.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import html
import json
import os
import re
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CODECHEF_ROOT = ROOT / "docs" / "algorithms" / "codechef"
INDEX_PATH = CODECHEF_ROOT / "index.json"
OUTPUT_PATH = CODECHEF_ROOT / "problem_details.json"
CACHE_ROOT = CODECHEF_ROOT / ".problem_cache"
COOKIE_PATH = CODECHEF_ROOT / ".codechef_cookie"


class _MarkdownParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hrefs: list[str | None] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag in {"p", "div", "section", "blockquote", "table", "tr"}:
            self.parts.append("\n\n")
        elif tag in {"br", "hr"}:
            self.parts.append("\n")
        elif tag in {"li"}:
            self.parts.append("\n- ")
        elif tag in {"h1", "h2", "h3", "h4"}:
            self.parts.append(f"\n\n{'#' * int(tag[1])} ")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("*")
        elif tag in {"code", "pre"}:
            self.parts.append("`")
        elif tag == "a":
            self.parts.append("[")
            self.hrefs.append(values.get("href"))

    def handle_endtag(self, tag: str) -> None:
        if tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("*")
        elif tag in {"code", "pre"}:
            self.parts.append("`")
        elif tag == "a":
            href = self.hrefs.pop() if self.hrefs else None
            self.parts.append(f"]({href})" if href else "]")
        elif tag in {"p", "div", "section", "blockquote", "li", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def to_markdown(value: Any) -> str:
    text = str(value or "").replace("\r", "")
    if "<" in text and ">" in text:
        parser = _MarkdownParser()
        parser.feed(text)
        text = "".join(parser.parts)
    text = html.unescape(text).replace("\u00a0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _solutions(raw: Any) -> list[dict[str, str]]:
    rows = raw.values() if isinstance(raw, dict) else raw if isinstance(raw, list) else []
    result = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("solution"):
            continue
        result.append({
            "language": str(row.get("language") or "Text"),
            "source": str(row["solution"]).replace("\r\n", "\n"),
        })
    preferred = {"PYTH 3": 0, "PYTHON": 0, "C++17": 1, "C++14": 2, "C++": 3}
    return sorted(result, key=lambda row: preferred.get(row["language"].upper(), 20))


def _fallback_editorial_from_solution(raw: Any) -> str:
    rows = raw.values() if isinstance(raw, dict) else raw if isinstance(raw, list) else []
    for row in rows:
        if not isinstance(row, dict):
            continue
        language = str(row.get("language") or "").strip().lower()
        source = str(row.get("solution") or "").strip()
        if not source or language not in {"default", "text", "explanation"}:
            continue
        if re.search(
            r"\b(?:#include|using\s+namespace|int\s+main|public\s+class|class\s+Solution|def\s+solve|import\s+sys)\b",
            source,
            flags=re.IGNORECASE,
        ):
            continue
        return to_markdown(source)
    return ""


def _cookie_header() -> str:
    """Return an authenticated CodeChef cookie header when configured.

    Some practice-course editorials are omitted from anonymous API responses
    even when the same user can see them in the browser.  The importer keeps
    working anonymously, but automatically uses the local CodeChef session
    cookie when it is available.
    """
    value = os.environ.get("CODECHEF_COOKIE", "").strip()
    if value:
        return value
    if COOKIE_PATH.is_file():
        return COOKIE_PATH.read_text(encoding="utf-8").strip()
    return ""


def _needs_authenticated_refresh(detail: dict[str, Any], cookie_header: str) -> bool:
    return bool(cookie_header) and not str(detail.get("editorial") or "").strip()


def normalize(payload: dict[str, Any]) -> dict[str, Any]:
    components = payload.get("problemComponents") or {}
    samples = []
    for sample in components.get("sampleTestCases") or []:
        if not isinstance(sample, dict) or sample.get("isDeleted"):
            continue
        samples.append({
            "input": str(sample.get("input") or "").strip(),
            "output": str(sample.get("output") or "").strip(),
            "explanation": to_markdown(sample.get("explanation")),
        })
    statement = to_markdown(components.get("statement"))
    if not statement:
        statement = to_markdown(payload.get("body"))
    editorial = to_markdown(payload.get("text_editorial_body"))
    if not editorial:
        editorial = _fallback_editorial_from_solution(payload.get("solution"))
    return {
        "code": str(payload.get("problem_code") or ""),
        "name": str(payload.get("problem_name") or ""),
        "statement": statement,
        "input_format": to_markdown(components.get("inputFormat")),
        "output_format": to_markdown(components.get("outputFormat")),
        "constraints": to_markdown(components.get("constraints")),
        "samples": samples[:3],
        "editorial": editorial,
        "official_solutions": _solutions(payload.get("solution")),
        "difficulty_rating": payload.get("difficulty_rating"),
        "author": str(payload.get("problem_author") or ""),
    }


def fetch(question: dict[str, Any], attempts: int = 4) -> tuple[str, dict[str, Any] | None, str | None]:
    code = str(question["code"])
    cached = CACHE_ROOT / f"{code}.json"
    cookie_header = _cookie_header()
    if cached.is_file():
        try:
            cached_detail = json.loads(cached.read_text(encoding="utf-8"))
            if not _needs_authenticated_refresh(cached_detail, cookie_header):
                return code, cached_detail, None
        except (OSError, json.JSONDecodeError):
            pass
    contest = str(question.get("contest_code") or "PRACTICE")
    url = f"https://www.codechef.com/api/contests/{contest}/problems/{code}?ref="
    for attempt in range(attempts):
        try:
            headers = {
                "Accept": "application/json",
                "Referer": str(question.get("url") or "https://www.codechef.com/practice"),
                "User-Agent": "cOde(n) CodeChef reference importer/1.0",
            }
            if cookie_header:
                headers["Cookie"] = cookie_header
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.load(response)
            if payload.get("status") != "success":
                raise ValueError(str(payload.get("message") or "CodeChef API error"))
            detail = normalize(payload)
            cached.write_text(json.dumps(detail, ensure_ascii=False), encoding="utf-8")
            return code, detail, None
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            if attempt + 1 == attempts:
                return code, None, str(exc)
            time.sleep(1.5 * (2 ** attempt))
    return code, None, "unreachable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", action="append", help="CodeChef problem code to refresh. May be passed multiple times.")
    parser.add_argument("--missing-editorial", action="store_true", help="Refresh only visible problems whose cached editorial is empty.")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    questions = list(index.get("questions", []))
    partial_update = bool(args.code or args.limit or args.missing_editorial)
    if args.code:
        wanted = {code.upper() for code in args.code}
        questions = [question for question in questions if str(question.get("code", "")).upper() in wanted]
    if args.missing_editorial:
        existing = {}
        if OUTPUT_PATH.is_file():
            existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8")).get("problems") or {}
        questions = [
            question for question in questions
            if not str(existing.get(str(question.get("code") or ""), {}).get("editorial") or "").strip()
        ]
    if args.limit:
        questions = questions[:args.limit]
    details: dict[str, dict[str, Any]] = {}
    errors: dict[str, str] = {}
    if partial_update and OUTPUT_PATH.is_file():
        existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        details.update(existing.get("problems") or {})
        errors.update(existing.get("errors") or {})
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        for number, (code, detail, error) in enumerate(pool.map(fetch, questions), start=1):
            if detail is not None:
                details[code] = detail
                errors.pop(code, None)
            else:
                errors[code] = error or "unknown error"
            if number % 100 == 0 or number == len(questions):
                print(f"{number}/{len(questions)} fetched; {len(errors)} errors", flush=True)
    OUTPUT_PATH.write_text(json.dumps({
        "source": "CodeChef official problem API",
        "total_problems": len(details),
        "errors": errors,
        "problems": details,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(details)} details to {OUTPUT_PATH}; errors={len(errors)}")


if __name__ == "__main__":
    main()
