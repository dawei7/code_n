"""Generate static CodeChef markdown reference docs.

The application normally serves challenge references from files under
``docs/algorithms``.  CodeChef initially used a dynamic route backed by
``problem_details.json`` while the dataset was being imported.  This tool
materializes those references as ordinary markdown files so CodeChef behaves
like LeetCode, NeetCode, and GeeksforGeeks.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from server.app.routes.docs import generate_codechef_reference


CODECHEF_ROOT = PROJECT_ROOT / "docs" / "algorithms" / "codechef"
INDEX_PATH = CODECHEF_ROOT / "index.json"
DETAILS_PATH = CODECHEF_ROOT / "problem_details.json"


@dataclass
class CodeChefDocSpec:
    name: str
    description: str
    source_url: str
    difficulty_label: str
    inputs: dict[str, str]
    returns: str
    reference_metadata: dict[str, Any]


def _slugify(value: str) -> str:
    slug = value.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-") or "problem"


def _doc_category_folder(category: str) -> str:
    prefix = "codechef_"
    return category.removeprefix(prefix) if category.startswith(prefix) else category


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _merged_metadata(question: dict[str, Any], detail: dict[str, Any]) -> dict[str, Any]:
    merged = dict(detail)
    for key in (
        "code",
        "name",
        "url",
        "difficulty",
        "difficulty_level",
        "difficulty_rating",
        "difficulty_type",
        "path_group",
        "path_level",
        "path_slug",
        "lesson",
        "lesson_order",
        "contest_code",
    ):
        if question.get(key) not in (None, ""):
            merged[key] = question[key]
    return merged


def _build_spec(question: dict[str, Any], detail: dict[str, Any]) -> CodeChefDocSpec:
    metadata = _merged_metadata(question, detail)
    return CodeChefDocSpec(
        name=str(question.get("name") or detail.get("name") or question["code"]),
        description=str(detail.get("statement") or ""),
        source_url=str(question.get("url") or ""),
        difficulty_label=str(question.get("difficulty") or ""),
        inputs={"input_data": str(detail.get("input_format") or "")},
        returns=str(detail.get("output_format") or ""),
        reference_metadata=metadata,
    )


def generate_docs(*, clean: bool = False) -> dict[str, int]:
    index = _load_json(INDEX_PATH)
    details = _load_json(DETAILS_PATH).get("problems", {})
    questions = list(index.get("questions") or [])

    if clean:
        for markdown in CODECHEF_ROOT.rglob("cc_*.md"):
            markdown.unlink()

    written_paths: set[Path] = set()
    written_problems: set[str] = set()
    skipped = 0

    for question in questions:
        code = str(question.get("code") or "").strip()
        if not code:
            skipped += 1
            continue
        detail = dict(details.get(code) or {})
        spec = _build_spec(question, detail)
        content = generate_codechef_reference(spec)
        filename = f"cc_{code}_{_slugify(spec.name)}.md"
        categories = list(question.get("categories") or [question.get("category")])
        categories = [str(category) for category in categories if category]
        if not categories:
            skipped += 1
            continue
        for category in dict.fromkeys(categories):
            target_dir = CODECHEF_ROOT / _doc_category_folder(category)
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / filename
            target.write_text(content, encoding="utf-8")
            written_paths.add(target)
        written_problems.add(code)

    return {
        "questions": len(questions),
        "written_problems": len(written_problems),
        "written_files": len(written_paths),
        "skipped": skipped,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing generated cc_*.md files before writing.",
    )
    args = parser.parse_args()

    result = generate_docs(clean=args.clean)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
