#!/usr/bin/env python3
"""Migrate all challenge packages to a single canonical solution layout.

This script:
1. Locates the optimal solution in variants/optimal/ and moves it to package root `solution.<ext>`.
2. Moves variants/optimal/approach.md to package root `approach.md`.
3. Moves variants/optimal/submission.json to package root `submission.json` (if present).
4. Deletes the variants/ directory (including any simplified variants).
5. Deletes solution_variants.json.
6. Removes "solution_variants" from metadata.json.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

# Ensure project root in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine.languages import language_extension, normalize_language


def migrate_single_package(pkg_path: Path) -> dict[str, str]:
    if not pkg_path.is_dir():
        return {"status": "skipped", "reason": "not a directory"}

    metadata_path = pkg_path / "metadata.json"
    if not metadata_path.is_file():
        return {"status": "skipped", "reason": "no metadata.json"}

    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"status": "error", "reason": f"invalid metadata: {exc}"}

    primary_lang = metadata.get("primary_language", "python")
    try:
        lang_id = normalize_language(primary_lang)
    except Exception:
        lang_id = "python"
    ext = language_extension(lang_id)

    variants_dir = pkg_path / "variants"
    optimal_dir = variants_dir / "optimal"

    # 1. Locate and migrate solution
    sol_moved = False
    target_sol = pkg_path / f"solution.{ext}"

    possible_sol_paths = [
        optimal_dir / "solutions" / f"solution.{ext}",
        optimal_dir / f"solution.{ext}",
        optimal_dir / "solutions" / "solve.py",
        optimal_dir / "solutions" / f"leetcode.{ext}",
        optimal_dir / "solutions" / "leetcode_sqlite.sql",
        optimal_dir / "solutions" / "leetcode.sql",
    ]

    for cand in possible_sol_paths:
        if cand.is_file():
            target_sol.write_text(cand.read_text(encoding="utf-8"), encoding="utf-8")
            sol_moved = True
            break

    if not sol_moved and not target_sol.is_file():
        # Check any solution.* in optimal_dir
        if optimal_dir.is_dir():
            for f in optimal_dir.glob("solution.*"):
                if f.is_file():
                    target_sol.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
                    sol_moved = True
                    break
            if not sol_moved:
                for f in (optimal_dir / "solutions").glob("*"):
                    if f.is_file():
                        target_sol.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
                        sol_moved = True
                        break

    # 2. Locate and migrate approach.md
    approach_src = optimal_dir / "approach.md"
    target_approach = pkg_path / "approach.md"
    if approach_src.is_file():
        target_approach.write_text(approach_src.read_text(encoding="utf-8"), encoding="utf-8")

    # 3. Locate and migrate submission.json
    sub_src = optimal_dir / "submission.json"
    target_sub = pkg_path / "submission.json"
    if sub_src.is_file():
        target_sub.write_text(sub_src.read_text(encoding="utf-8"), encoding="utf-8")

    # 4. Remove variants/ directory
    if variants_dir.exists():
        shutil.rmtree(variants_dir, ignore_errors=True)

    # 5. Remove solution_variants.json
    manifest_path = pkg_path / "solution_variants.json"
    if manifest_path.exists():
        manifest_path.unlink(missing_ok=True)

    # 6. Update metadata.json
    if "solution_variants" in metadata:
        del metadata["solution_variants"]
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    return {
        "status": "migrated",
        "pkg": pkg_path.name,
        "solution": str(target_sol.name),
        "has_approach": str(target_approach.is_file()),
    }


def main():
    root = Path("dsa/leetcode")
    packages = sorted([p for p in root.iterdir() if p.is_dir() and (p / "metadata.json").is_file()])
    print(f"Migrating {len(packages)} packages to single canonical solution layout...")

    migrated_count = 0
    for i, pkg in enumerate(packages, 1):
        res = migrate_single_package(pkg)
        if res["status"] == "migrated":
            migrated_count += 1
        if i % 500 == 0 or i == len(packages):
            print(f"Progress: {i}/{len(packages)} packages processed...")

    # Also check Euler if present
    euler_root = Path("dsa/euler")
    if euler_root.is_dir():
        euler_packages = sorted([p for p in euler_root.iterdir() if p.is_dir() and (p / "metadata.json").is_file()])
        print(f"Migrating {len(euler_packages)} Euler packages...")
        for pkg in euler_packages:
            migrate_single_package(pkg)

    print(f"\nMigration complete! Total packages migrated: {migrated_count}")


if __name__ == "__main__":
    main()
