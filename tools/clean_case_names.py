"""Clean case names, kinds, tags, and IDs across all cases.json.

Normalizes:
1. 'name': strips 'hidden: ' prefix.
2. 'kind': converts 'real' to 'trial'.
3. 'tags': removes 'hidden' tag.
4. 'id': converts 'hidden-X' or 'real-X' to 'trial-X' (preserving uniqueness).
5. 'visible': enforces True.
"""
from __future__ import annotations

import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")


def clean_case_metadata():
    pkgs = sorted([
        p for p in LEETCODE_ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    ])

    total_cleaned = 0
    total_ids_cleaned = 0
    total_files_modified = 0

    for pkg in pkgs:
        cases_file = pkg / "cases.json"
        if not cases_file.is_file():
            continue

        try:
            data = json.loads(cases_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        cases = data.get("cases", [])
        modified = False

        existing_ids = {c.get("id") for c in cases if c.get("id")}

        for c in cases:
            # 1. Clean name
            name = c.get("name", "")
            if name.lower().startswith("hidden:"):
                c["name"] = name[7:].strip()
                modified = True
                total_cleaned += 1
            elif name.lower().startswith("hidden :"):
                c["name"] = name[8:].strip()
                modified = True
                total_cleaned += 1
            elif name.lower().startswith("real:"):
                c["name"] = name[5:].strip()
                modified = True
                total_cleaned += 1
            elif name.lower().startswith("real :"):
                c["name"] = name[6:].strip()
                modified = True
                total_cleaned += 1

            # 2. Clean kind
            if c.get("kind") == "real":
                c["kind"] = "trial"
                modified = True

            # 3. Enforce visibility
            if not c.get("visible", True):
                c["visible"] = True
                modified = True

            # 4. Clean tags
            tags = c.get("tags", [])
            if "hidden" in tags:
                new_tags = [t for t in tags if t.lower() != "hidden"]
                if not new_tags:
                    new_tags = ["trial"]
                c["tags"] = new_tags
                modified = True
                total_cleaned += 1

            # 5. Clean ID
            cid = c.get("id", "")
            if cid.startswith("hidden-") or cid.startswith("hidden_"):
                suffix = cid[7:]
                new_id = f"trial-{suffix}"
                if new_id in existing_ids and new_id != cid:
                    new_id = f"trial-ext-{suffix}"
                c["id"] = new_id
                existing_ids.add(new_id)
                modified = True
                total_ids_cleaned += 1
            elif cid.startswith("real-") or cid.startswith("real_"):
                suffix = cid[5:]
                new_id = f"trial-{suffix}"
                if new_id in existing_ids and new_id != cid:
                    new_id = f"trial-r-{suffix}"
                c["id"] = new_id
                existing_ids.add(new_id)
                modified = True
                total_ids_cleaned += 1

        if modified:
            cases_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
            total_files_modified += 1

    print(f"Cleanup complete: {total_cleaned} names/tags cleaned, {total_ids_cleaned} IDs normalized across {total_files_modified} packages.")


if __name__ == "__main__":
    clean_case_metadata()
