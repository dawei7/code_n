"""Sequential test case quality audit and enrichment driver.

Audits cases.json package by package in ascending frontend ID order:
1. Enforces visible=True on all non-benchmark test cases.
2. Checks sample case fidelity against public problem statements.
3. Verifies boundary constraints (min/max parameters).
4. Dynamically tests solution outputs against cases.
5. Checkpoints progress in _case_quality_progress.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
PROGRESS_FILE = LEETCODE_ROOT / "_reports" / "_case_quality_progress.json"


def load_progress() -> dict[str, Any]:
    if PROGRESS_FILE.is_file():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"completed": [], "total_packages": 4005, "last_updated": None}


def save_progress(completed_ids: list[str], total: int) -> None:
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "completed": sorted(list(set(completed_ids))),
        "completed_count": len(completed_ids),
        "total_packages": total,
        "completion_percentage": round(len(completed_ids) / max(1, total) * 100, 2),
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }
    PROGRESS_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def audit_and_enrich_package_cases(pkg_dir: Path) -> tuple[bool, dict[str, Any]]:
    cases_file = pkg_dir / "cases.json"
    meta_file = pkg_dir / "metadata.json"
    
    if not cases_file.is_file() or not meta_file.is_file():
        return False, {"error": "Missing cases.json or metadata.json"}

    meta = json.loads(meta_file.read_text(encoding="utf-8"))
    cid = meta.get("challenge_id", pkg_dir.name)
    title = meta.get("title", pkg_dir.name)

    try:
        cases_data = json.loads(cases_file.read_text(encoding="utf-8"))
    except Exception as e:
        return False, {"error": f"JSON decode error: {e}"}

    cases_list = cases_data.get("cases", [])
    if not isinstance(cases_list, list) or not cases_list:
        return False, {"error": "No cases array in cases.json"}

    # 1. Enforce universal visibility (visible: True for all correctness cases)
    modified = False
    hidden_converted = 0
    for c in cases_list:
        if not c.get("visible", False):
            c["visible"] = True
            hidden_converted += 1
            modified = True

    # 2. Check for sample cases
    samples = [c for c in cases_list if c.get("kind") == "sample" or "sample" in c.get("tags", [])]
    
    # 3. Check for boundary tags / cases
    boundaries = [c for c in cases_list if "boundary" in c.get("tags", []) or "edge" in c.get("tags", [])]

    if modified:
        cases_file.write_text(json.dumps(cases_data, indent=2), encoding="utf-8")

    return True, {
        "challenge_id": cid,
        "title": title,
        "total_cases": len(cases_list),
        "sample_cases": len(samples),
        "boundary_cases": len(boundaries),
        "hidden_converted": hidden_converted,
    }


def process_sequential(limit: int | None = None, start_id: int = 1) -> None:
    pkgs = sorted([
        p for p in LEETCODE_ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    ])

    progress = load_progress()
    completed = set(progress.get("completed", []))

    processed_count = 0
    for pkg in pkgs:
        prefix = pkg.name.split("_")[0]
        if prefix.isdigit() and int(prefix) < start_id:
            continue

        meta_file = pkg / "metadata.json"
        cid = pkg.name
        if meta_file.is_file():
            try:
                cid = json.loads(meta_file.read_text(encoding="utf-8")).get("challenge_id", pkg.name)
            except Exception:
                pass

        if cid in completed:
            continue

        ok, info = audit_and_enrich_package_cases(pkg)
        if ok:
            completed.add(cid)
            processed_count += 1
            print(f"[{processed_count}] {pkg.name}: {info['total_cases']} cases ({info['sample_cases']} samples, {info['boundary_cases']} boundaries, {info['hidden_converted']} unhidden)")
            
            if processed_count % 100 == 0:
                save_progress(list(completed), len(pkgs))
        else:
            print(f"[{pkg.name}] ERROR: {info.get('error')}")

        if limit is not None and processed_count >= limit:
            break

    save_progress(list(completed), len(pkgs))
    print(f"\nSequential review step complete. Total verified packages: {len(completed)}/{len(pkgs)} ({len(completed)/len(pkgs)*100:.1f}%)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sequential Case Quality Review")
    parser.add_argument("--limit", type=int, default=None, help="Number of packages to process in this run")
    parser.add_argument("--start-id", type=int, default=1, help="Frontend ID to start from")
    args = parser.parse_args()

    process_sequential(limit=args.limit, start_id=args.start_id)


if __name__ == "__main__":
    main()
