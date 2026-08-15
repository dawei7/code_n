"""Clean case names and kinds across all cases.json.

Strips 'hidden: ' prefixes from case names and converts 'real' kind to 'trial'
so all cases cleanly display in the runner UI.
"""
from __future__ import annotations

import json
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")


def clean_case_names():
    pkgs = sorted([
        p for p in LEETCODE_ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    ])

    total_cleaned = 0
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

        for c in cases:
            name = c.get("name", "")
            if name.lower().startswith("hidden:"):
                c["name"] = name[7:].strip()
                modified = True
                total_cleaned += 1
            elif name.lower().startswith("hidden :"):
                c["name"] = name[8:].strip()
                modified = True
                total_cleaned += 1

            if c.get("kind") == "real":
                c["kind"] = "trial"
                modified = True

            if not c.get("visible", True):
                c["visible"] = True
                modified = True

        if modified:
            cases_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
            total_files_modified += 1

    print(f"Cleanup complete: {total_cleaned} case names cleaned across {total_files_modified} packages.")


if __name__ == "__main__":
    clean_case_names()
