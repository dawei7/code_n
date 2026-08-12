"""Importer tool for Project Euler problem packages.

Creates canonical challenge package folders in `dsa/euler/<0001_slug>/` with
metadata.json, reference docs, template.py, variants, cases.json, and solution_variants.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# Ensure project root is in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Reconfigure stdout to utf-8 if possible
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from server.app.config import EULER_ROOT




def create_euler_package(
    frontend_id: int | str,
    title: str,
    slug: str,
    description: str,
    difficulty: str = "Level 0 (5%)",
    euler_level: int = 0,
    category: str = "math",
    solution_code: str | None = None,
    approach_md: str | None = None,
    cases: list[dict[str, Any]] | None = None,
) -> Path:
    num_str = str(frontend_id).zfill(4)
    package_dir = EULER_ROOT / f"{num_str}_{slug}"
    package_dir.mkdir(parents=True, exist_ok=True)
    ref_dir = package_dir / "reference"
    ref_dir.mkdir(parents=True, exist_ok=True)
    variants_dir = package_dir / "variants" / "optimal" / "solutions"
    variants_dir.mkdir(parents=True, exist_ok=True)

    # 1. metadata.json
    metadata = {
        "challenge_id": f"euler_{int(frontend_id)}",
        "source": "euler",
        "frontend_id": str(frontend_id),
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "euler_level": euler_level,
        "category": category,
        "category_title": category.replace("-", " ").title(),
        "topics": [
            {"name": "Mathematics", "slug": "math"},
            {"name": "Project Euler", "slug": "euler"},
        ],
        "url": f"https://projecteuler.net/problem={frontend_id}",
        "supported_languages": ["python"],
        "primary_language": "python",
        "runnable_in_coden": True,
        "dataset": "euler",
        "solution_variants": {"manifest": "solution_variants.json"},
    }
    (package_dir / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")


    # 2. reference docs
    (ref_dir / "description.md").write_text(description.strip() + "\n", encoding="utf-8")
    (ref_dir / "contract.md").write_text("## Function Contract\n\n- `solve() -> int`\n", encoding="utf-8")
    (ref_dir / "examples.md").write_text("## Examples\n\n- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.\n", encoding="utf-8")

    (ref_dir / "constraints.md").write_text("## Constraints\n\n- Execution time MUST be strictly under 1 minute.\n", encoding="utf-8")

    # 3. doc.md
    doc_content = f"# {title}\n\n" + description.strip() + "\n"
    (package_dir / "doc.md").write_text(doc_content, encoding="utf-8")

    # 4. template.py
    template_code = "def solve() -> int:\n    \"\"\"Find the solution for this Project Euler problem.\"\"\"\n    pass\n"
    (package_dir / "template.py").write_text(template_code, encoding="utf-8")

    # 5. solution.py & approach.md
    sol = solution_code or "def solve() -> int:\n    return 0\n"
    (variants_dir / "solution.py").write_text(sol.strip() + "\n", encoding="utf-8")

    app_md = approach_md or f"# {title} — Optimal Approach\n\nMathematical approach executing in under 1 minute.\n"
    (package_dir / "variants" / "optimal" / "approach.md").write_text(app_md.strip() + "\n", encoding="utf-8")

    # 6. cases.json & solution_variants.json
    case_list = cases or []
    (package_dir / "cases.json").write_text(json.dumps({"challenge_id": f"euler_{int(frontend_id)}", "cases": case_list}, indent=2), encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "challenge_id": f"euler_{int(frontend_id)}",
        "default_variant": "optimal",
        "variants": [
            {
                "id": "optimal",
                "label": "Optimal Mathematical Closed-Form",
                "kind": "optimal",
                "directory": "variants/optimal",
                "summary": "Mathematical solution executing under 1 minute.",
                "time_complexity": "O(1)",
                "space_complexity": "O(1)",
            }
        ],
    }
    (package_dir / "solution_variants.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Created package: {package_dir}")
    return package_dir


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Project Euler challenge package")
    parser.add_argument("--id", required=True, type=int, help="Problem number (e.g. 2)")
    parser.add_argument("--title", required=True, type=str, help="Problem title")
    parser.add_argument("--slug", required=True, type=str, help="Problem slug")
    parser.add_argument("--description", required=True, type=str, help="Markdown problem description")
    args = parser.parse_args()

    create_euler_package(args.id, args.title, args.slug, args.description)
