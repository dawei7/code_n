"""Translate official non-Python CodeChef solutions for internal AST baselines.

Translations are never returned to the UI. The script is resumable and uses
the Gemini key already configured in the local cOde(n) profile.
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import requests

from server.app import progress_store


DETAILS_PATH = ROOT / "docs" / "algorithms" / "codechef" / "problem_details.json"
OUTPUT_PATH = ROOT / "docs" / "algorithms" / "codechef" / "translated_solutions.json"
PYTHON_TOKENS = ("PYTH", "PYTHON", "PYPY")
CODE_LANGUAGES = ("C++17", "C++14", "C++", "C", "NODEJS", "C#", "JAVA")
MODELS = ("gemini-3.5-flash", "gemini-2.5-flash")


def _is_python(language: str) -> bool:
    upper = language.upper()
    return any(token in upper for token in PYTHON_TOKENS)


def _source_to_translate(problem: dict[str, Any]) -> dict[str, str] | None:
    solutions = list(problem.get("official_solutions") or [])
    if any(_is_python(str(solution.get("language", ""))) for solution in solutions):
        return None
    for wanted in CODE_LANGUAGES:
        for solution in solutions:
            if str(solution.get("language", "")).upper() == wanted:
                return solution
    return None


def _extract_code(text: str) -> str:
    match = re.search(r"```(?:python)?\s*([\s\S]*?)```", text, flags=re.IGNORECASE)
    source = match.group(1) if match else text
    source = source.strip()
    ast.parse(source)
    return source + "\n"


def translate(code: str, solution: dict[str, str], api_key: str) -> tuple[str, dict[str, str] | None, str | None]:
    language = str(solution.get("language") or "")
    prompt = f"""Translate this official {language} competitive-programming solution to Python 3.
Preserve the exact stdin/stdout behavior, algorithm, asymptotic time complexity, and asymptotic space complexity.
Do not explain anything. Return only complete executable Python source in one code fence.

Problem code: {code}

```text
{solution.get('source', '')}
```"""
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0, "maxOutputTokens": 8192},
    }
    last_error = "translation failed"
    for attempt in range(4):
        for model in MODELS:
            try:
                response = requests.post(
                    f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                    params={"key": api_key},
                    json=payload,
                    timeout=120,
                )
                if response.status_code in {429, 500, 502, 503, 504}:
                    last_error = f"HTTP {response.status_code}"
                    continue
                response.raise_for_status()
                data = response.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                source = _extract_code(text)
                return code, {
                    "language": f"PYTH 3 (translated from {language})",
                    "source": source,
                    "source_language": language,
                    "model": model,
                }, None
            except (requests.RequestException, KeyError, IndexError, ValueError, SyntaxError) as exc:
                last_error = f"{type(exc).__name__}: {exc}"
        time.sleep(2 ** attempt)
    return code, None, last_error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--delay", type=float, default=0.0, help="Seconds between requests")
    args = parser.parse_args()
    api_key = progress_store.load().gemini_api_key.strip()
    if not api_key:
        raise SystemExit("Configure a Gemini API key in the cOde(n) profile first.")
    problems = json.loads(DETAILS_PATH.read_text(encoding="utf-8"))["problems"]
    existing = {"translations": {}, "errors": {}}
    if OUTPUT_PATH.is_file():
        existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    translations = dict(existing.get("translations") or {})
    candidates = [
        (code, solution)
        for code, problem in problems.items()
        if code not in translations and (solution := _source_to_translate(problem)) is not None
    ]
    if args.limit:
        candidates = candidates[:args.limit]
    errors: dict[str, str] = dict(existing.get("errors") or {})

    def save_result(number: int, result: tuple[str, dict[str, str] | None, str | None]) -> None:
        code, translated, error = result
        if translated:
            translations[code] = translated
        else:
            errors[code] = error or "unknown error"
        OUTPUT_PATH.write_text(json.dumps({
            "source": "Translations of official CodeChef solutions for internal AST analysis only",
            "translations": translations,
            "errors": errors,
        }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{number}/{len(candidates)} {code}: {'ok' if translated else error}", flush=True)

    if args.workers == 1:
        for number, (code, solution) in enumerate(candidates, start=1):
            result = translate(code, solution, api_key)
            save_result(number, result)
            if result[2] == "HTTP 429":
                print("Gemini is rate-limiting translation requests; stopping early so the remaining candidates stay resumable.", flush=True)
                break
            if args.delay and number < len(candidates):
                time.sleep(args.delay)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
            futures = [pool.submit(translate, code, solution, api_key) for code, solution in candidates]
            for number, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                save_result(number, future.result())
    print(f"Translations: {len(translations)}; errors: {len(errors)}")


if __name__ == "__main__":
    main()
