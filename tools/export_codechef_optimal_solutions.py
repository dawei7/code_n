"""Export internal CodeChef Python baselines to ``optimal_solutions/codechef``.

CodeChef solutions are stdin/stdout programs, so this exporter normalizes every
source file to expose a top-level ``def solve()`` entrypoint while preserving the
program as an internal AST baseline.  These files are not displayed to the
frontend as official answers.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from server.app.codechef_sources import best_codechef_source, is_python_language

CODECHEF_ROOT = ROOT / "docs" / "algorithms" / "codechef"
INDEX_PATH = CODECHEF_ROOT / "index.json"
DETAILS_PATH = CODECHEF_ROOT / "problem_details.json"
COMMUNITY_PATH = CODECHEF_ROOT / "community_optimal_solutions.json"
TRANSLATIONS_PATH = CODECHEF_ROOT / "translated_solutions.json"
EXEMPTIONS_PATH = CODECHEF_ROOT / "baseline_exemptions.json"
AUTHORED_ROOT = CODECHEF_ROOT / "authored_solutions"
OUTPUT_ROOT = ROOT / "optimal_solutions" / "codechef"
REPORT_PATH = OUTPUT_ROOT / "_completion_report.json"


def _load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _safe_segment(value: str) -> str:
    value = value.strip().lower().replace("__", "/")
    parts = []
    for part in value.split("/"):
        slug = re.sub(r"[^a-z0-9]+", "-", part).strip("-")
        if slug:
            parts.append(slug)
    return "/".join(parts) or "uncategorized"


def _has_function(tree: ast.Module, name: str) -> bool:
    return any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name for node in tree.body)


def _looks_like_main_guard(node: ast.AST) -> bool:
    if not isinstance(node, ast.If):
        return False
    try:
        return ast.unparse(node.test).replace("'", '"') == '__name__ == "__main__"'
    except Exception:
        return False


def _strip_main_guard(source: str) -> str:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source
    if not tree.body or not _looks_like_main_guard(tree.body[-1]):
        return source
    tree.body = tree.body[:-1]
    return ast.unparse(tree) + "\n"


def _rename_main_to_solve(source: str) -> str:
    source = _strip_main_guard(source)
    source = re.sub(r"(?m)^def\s+main\s*\(", "def solve(", source, count=1)
    return source.rstrip() + '\n\n\nif __name__ == "__main__":\n    solve()\n'


def _wrap_script_source(source: str) -> str:
    source = source.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not source:
        return "def solve():\n    pass\n"

    try:
        tree = ast.parse(source)
    except SyntaxError:
        raise

    if _has_function(tree, "solve"):
        return _strip_main_guard(source).rstrip() + '\n\n\nif __name__ == "__main__":\n    solve()\n'
    if _has_function(tree, "main"):
        return _rename_main_to_solve(source)

    lines = source.splitlines()
    prefix: list[str] = []
    body = lines[:]
    while body:
        stripped = body[0].strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("import ") or stripped.startswith("from "):
            prefix.append(body.pop(0))
            continue
        break

    indented = ["    " + line if line.strip() else "" for line in body]
    if not indented:
        indented = ["    pass"]
    return "\n".join(prefix).rstrip() + "\n\n\ndef solve():\n" + "\n".join(indented) + '\n\n\nif __name__ == "__main__":\n    solve()\n'


def _normalize_source(source: str) -> str:
    normalized = _wrap_script_source(source)
    ast.parse(normalized)
    return normalized.rstrip() + "\n"


def _visible_questions() -> dict[str, dict[str, Any]]:
    payload = _load_json(INDEX_PATH)
    return {
        str(question.get("code") or "").upper(): question
        for question in payload.get("questions", [])
        if question.get("code")
    }


def _baseline_sources() -> dict[str, dict[str, str]]:
    sources: dict[str, dict[str, str]] = {}

    community = _load_json(COMMUNITY_PATH).get("solutions", {})
    for code, row in community.items():
        source = str(row.get("source") or "")
        if source.strip():
            sources[str(code).upper()] = {
                "source": source,
                "kind": "community",
            }

    translations = _load_json(TRANSLATIONS_PATH).get("translations", {})
    for code, row in translations.items():
        source = str(row.get("source") or "")
        if source.strip():
            sources.setdefault(str(code).upper(), {
                "source": source,
                "kind": "translation",
            })

    problems = _load_json(DETAILS_PATH).get("problems", {})
    for code, problem in problems.items():
        if not isinstance(problem, dict):
            continue
        candidate = best_codechef_source(problem, prefer_python=True)
        if not candidate or not is_python_language(candidate.get("language", "")):
            continue
        source = str(candidate.get("source") or "")
        if source.strip():
            sources.setdefault(str(code).upper(), {
                "source": source,
                "kind": "official_python",
            })

    return sources


def solution_path(question: dict[str, Any]) -> Path:
    category = str(question.get("category") or "uncategorized")
    code = str(question["code"]).upper()
    return OUTPUT_ROOT / _safe_segment(category) / f"{code}.py"


def export(*, clean: bool) -> dict[str, Any]:
    questions = _visible_questions()
    exemptions = {
        str(code).upper()
        for code in _load_json(EXEMPTIONS_PATH).get("exemptions", {})
    }
    sources = _baseline_sources()

    if clean and OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, Any]] = []
    counts = {
        "exported": 0,
        "missing_source": 0,
        "baseline_exempt": 0,
        "syntax_error": 0,
    }

    for code, question in sorted(questions.items()):
        target = solution_path(question)
        if code in exemptions:
            counts["baseline_exempt"] += 1
            entries.append({"code": code, "status": "baseline_exempt"})
            continue
        row = sources.get(code)
        if not row:
            counts["missing_source"] += 1
            entries.append({"code": code, "status": "missing_source"})
            continue
        try:
            normalized = _normalize_source(row["source"])
        except SyntaxError as exc:
            counts["syntax_error"] += 1
            entries.append({"code": code, "status": "syntax_error", "error": str(exc)})
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(normalized, encoding="utf-8")
        counts["exported"] += 1
        entries.append({
            "code": code,
            "status": "exported",
            "source_kind": row["kind"],
            "path": str(target.relative_to(ROOT)).replace("\\", "/"),
        })

    REPORT_PATH.write_text(
        json.dumps(
            {
                "source": "Exported CodeChef optimal solutions for internal AST baselines",
                "counts": counts,
                "entries": entries,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return {"counts": counts, "report": str(REPORT_PATH.relative_to(ROOT)).replace("\\", "/")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true", help="Remove existing exported CodeChef files before writing.")
    args = parser.parse_args()
    print(json.dumps(export(clean=args.clean), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
