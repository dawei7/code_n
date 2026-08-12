"""Build aggregated dsa/euler/index.json for fast server startup."""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Ensure project root in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from server.app.config import EULER_ROOT


INDEX_FILE = EULER_ROOT / "index.json"


def build_euler_index():
    questions = []
    for pkg_dir in sorted(EULER_ROOT.iterdir()):
        if not pkg_dir.is_dir():
            continue
        meta_file = pkg_dir / "metadata.json"
        if not meta_file.is_file():
            continue

        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            questions.append({
                "frontend_id": str(meta.get("frontend_id", "")),
                "title": str(meta.get("title", "")),
                "slug": str(meta.get("slug", "")),
                "difficulty": str(meta.get("difficulty", "Level 0")),
                "euler_level": int(meta.get("euler_level", 0)),
                "category": str(meta.get("category", "math")),
                "category_title": str(meta.get("category_title", "Mathematics")),
                "topics": meta.get("topics", []),
                "url": str(meta.get("url", "")),
                "package_name": pkg_dir.name,
            })
        except Exception as err:
            print(f"Error indexing {pkg_dir.name}: {err}")

    questions.sort(key=lambda q: int(q["frontend_id"]) if q["frontend_id"].isdigit() else 99999)

    index_data = {
        "source": "https://projecteuler.net/",
        "count": len(questions),
        "questions": questions,
    }

    INDEX_FILE.write_text(json.dumps(index_data, indent=2), encoding="utf-8")
    print(f"Built {INDEX_FILE} with {len(questions)} Project Euler questions.")


if __name__ == "__main__":
    build_euler_index()
