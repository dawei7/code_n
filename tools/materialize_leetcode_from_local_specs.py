"""Fill LeetCode docs from local cOde(n) specs when a safe match exists.

This script upgrades the metadata-only LeetCode scaffolds with original local
descriptions, examples, and complexity for problems that are
already represented in :mod:`challenges.registry`.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from challenges.registry import CHALLENGE_REGISTRY  # noqa: E402
from server.app.leetcode_mapping import LEETCODE_MAPPING  # noqa: E402


LEETCODE_ROOT = REPO_ROOT / "docs" / "algorithms" / "leetcode"
NEETCODE_ROOT = REPO_ROOT / "docs" / "algorithms" / "neetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
REPORT_PATH = LEETCODE_ROOT / "_materialization_report.json"
SCAFFOLD_MARKERS = (
    "Write an original local summary",
    "TODO",
)
CANONICAL_SECTION_RE = re.compile(
    r"\n---\s*\n\s*## Canonical Solution Notes\s*\n[\s\S]*$",
    re.IGNORECASE,
)


def url_slug(url: str) -> str:
    match = re.search(r"leetcode\.com/problems/([^/?#]+)/?", url)
    return match.group(1) if match else ""


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def load_index() -> list[dict[str, Any]]:
    data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return list(data["questions"])


def question_path(question: dict[str, Any]) -> Path:
    topics = question.get("topics") or []
    topic = slugify(topics[0]["slug"]) if topics else "uncategorized"
    return LEETCODE_ROOT / topic / f"{question['frontend_id']}_{question['slug']}.md"


def can_overwrite(path: Path) -> bool:
    """Only refresh generated/scaffold files; preserve hand-authored docs."""
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8")
    return any(marker in text for marker in SCAFFOLD_MARKERS)


def local_doc_path(challenge_id: str) -> Path | None:
    matches = list(NEETCODE_ROOT.glob(f"**/{challenge_id}_*.md"))
    return matches[0] if matches else None


def clean_description(description: str) -> str:
    text = re.sub(
        r"\n+##\s+GeeksforGeeks Reference\s*\n[\s\S]*?(?=\n+##\s+|$)",
        "",
        description,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\n+##\s+Example\s*\n[\s\S]*?(?=\n+##\s+|$)",
        "",
        text,
        flags=re.IGNORECASE,
    )
    return text.strip()


def strip_canonical_notes(text: str) -> str:
    text = CANONICAL_SECTION_RE.sub("", text)
    text = re.sub(
        r"\n## Canonical Solution Notes\s*\n[\s\S]*$",
        "",
        text,
        flags=re.IGNORECASE,
    )
    return text.strip()


def format_samples(spec) -> str:
    samples = list(spec.samples[:3])
    if len(samples) < 3:
        return (
            "_This local spec has fewer than three authored examples. Add original "
            "examples before marking this reference complete._"
        )

    blocks = []
    for i, sample in enumerate(samples, start=1):
        blocks.append(
            f"**Example {i}**\n\n"
            f"- Input: `{sample.input_repr}`\n"
            f"- Output: `{sample.output_repr}`"
        )
    return "\n\n".join(blocks)


def generated_reference(spec) -> str:
    inputs = "\n".join(
        f"- `{name}`: {spec.inputs.get(name, 'input value')}"
        for name in spec.params
    )
    examples = format_samples(spec)
    complexity = (
        spec.required_complexity.value
        if hasattr(spec.required_complexity, "value")
        else str(spec.required_complexity)
    )
    return f"""## Problem Description & Examples
### Goal
{clean_description(spec.description)}

### Function Contract
**Inputs**

{inputs}

**Return value**

{spec.returns}

### Examples
{examples}

---

## Underlying Base Algorithm(s)
{spec.category}

---

## Complexity Analysis
- **Time Complexity**: `{complexity}`
- **Space Complexity**: `TODO`
"""


def metadata_header(question: dict[str, Any], source_id: str) -> str:
    topics = ", ".join(tag["name"] for tag in question.get("topics", [])) or "Uncategorized"
    return f"""# {question['title']}

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `{source_id}` |
| Frontend ID | {question['frontend_id']} |
| Difficulty | {question['difficulty']} |
| Topics | {topics} |
| Official Link | [{question['slug']}]({question['url']}) |

"""


def reference_body(challenge_id: str, spec) -> str:
    doc = local_doc_path(challenge_id)
    if doc is not None:
        return strip_canonical_notes(doc.read_text(encoding="utf-8-sig"))
    return strip_canonical_notes(generated_reference(spec))


def build_slug_map() -> dict[str, str]:
    slug_to_id: dict[str, str] = {}
    for challenge_id, leetcode in LEETCODE_MAPPING.items():
        slug = url_slug(leetcode.get("url", ""))
        if not slug or challenge_id not in CHALLENGE_REGISTRY:
            continue
        current = slug_to_id.get(slug)
        if current is None or (challenge_id.startswith("nc_") and not current.startswith("nc_")):
            slug_to_id[slug] = challenge_id
    return slug_to_id


def main() -> int:
    questions = load_index()
    slug_to_id = build_slug_map()
    materialized: list[dict[str, str]] = []
    missing: list[dict[str, str]] = []

    for question in questions:
        challenge_id = slug_to_id.get(question["slug"])
        if challenge_id is None:
            missing.append({"slug": question["slug"], "title": question["title"]})
            continue

        spec = CHALLENGE_REGISTRY[challenge_id]()._spec
        path = question_path(question)
        if not can_overwrite(path):
            materialized.append(
                {
                    "slug": question["slug"],
                    "title": question["title"],
                    "challenge_id": challenge_id,
                    "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
                    "status": "preserved_manual",
                }
            )
            continue

        path.parent.mkdir(parents=True, exist_ok=True)
        content = (
            metadata_header(question, challenge_id)
            + reference_body(challenge_id, spec).rstrip()
            + "\n"
        )
        path.write_text(content, encoding="utf-8")
        materialized.append(
            {
                "slug": question["slug"],
                "title": question["title"],
                "challenge_id": challenge_id,
                "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "status": "refreshed_from_local_spec",
            }
        )

    REPORT_PATH.write_text(
        json.dumps(
            {
                "materialized_count": len(materialized),
                "missing_count": len(missing),
                "materialized": materialized,
                "missing": missing,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Materialized {len(materialized)} LeetCode docs from local specs.")
    print(f"Left {len(missing)} metadata-only docs for original authoring.")
    print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
