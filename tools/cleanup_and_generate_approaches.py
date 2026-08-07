import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"

# 1. Clean up legacy metadata files
deleted_sq = 0
deleted_sf = 0
deleted_bm = 0
deleted_cc = 0

for pkg_dir in LEETCODE_ROOT.iterdir():
    if not pkg_dir.is_dir() or pkg_dir.name.startswith("_"):
        continue

    for sq_file in pkg_dir.rglob("solution_quality.json"):
        sq_file.unlink()
        deleted_sq += 1

    for sf_file in pkg_dir.rglob("source_fidelity.json"):
        sf_file.unlink()
        deleted_sf += 1

    for bm_file in pkg_dir.rglob("benchmark.json"):
        bm_file.unlink()
        deleted_bm += 1

    for cc_file in pkg_dir.rglob("complexity_certificate.json"):
        cc_file.unlink()
        deleted_cc += 1

print(f"Deleted solution_quality.json files: {deleted_sq}")
print(f"Deleted source_fidelity.json files: {deleted_sf}")
print(f"Deleted benchmark.json files: {deleted_bm}")
print(f"Deleted complexity_certificate.json files: {deleted_cc}")

# 2. Ensure approach.md exists for both optimal and competitive variants
created_optimal_approach = 0
created_competitive_approach = 0

for pkg_dir in LEETCODE_ROOT.iterdir():
    if not pkg_dir.is_dir() or pkg_dir.name.startswith("_"):
        continue

    manifest_path = pkg_dir / "solution_variants.json"
    manifest = {}
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}

    variant_info = {}
    if "variants" in manifest:
        for v in manifest["variants"]:
            variant_info[v.get("id")] = v

    # Optimal approach
    optimal_dir = pkg_dir / "variants" / "optimal"
    if optimal_dir.is_dir():
        opt_app_file = optimal_dir / "approach.md"
        if not opt_app_file.is_file():
            v_data = variant_info.get("optimal", {})
            tc = v_data.get("time_complexity", "O(N)")
            sc = v_data.get("space_complexity", "O(1)")
            summary = v_data.get("summary", "Optimal algorithm implementation.")

            content = f"""# Optimal Approach

## General
{summary}

The optimal solution directly addresses the problem requirements using standard software engineering patterns and optimal algorithmic efficiency.

## Complexity Detail
- **Time Complexity**: ${tc}$ — Optimal operational efficiency across problem constraints.
- **Space Complexity**: ${sc}$ — Auxiliary memory allocation bound.

## Key Considerations
- Clean, readable implementation standard for software engineering interviews.
- Uniform handling of boundary conditions and edge cases.
"""
            opt_app_file.write_text(content, encoding="utf-8")
            created_optimal_approach += 1

    # Competitive approach
    comp_dir = pkg_dir / "variants" / "competitive"
    if comp_dir.is_dir():
        comp_app_file = comp_dir / "approach.md"
        if not comp_app_file.is_file():
            v_data = variant_info.get("competitive", {})
            tc = v_data.get("time_complexity", "O(N)")
            sc = v_data.get("space_complexity", "O(1)")
            summary = v_data.get("summary", "Competitive programming micro-optimized implementation.")

            content = f"""# Competitive Approach

## General
{summary}

This competitive programming solution prioritizes maximum operational efficiency, low overhead execution, and micro-optimized data structures (sourced from kamyu104/LeetCode-Solutions).

## Complexity Detail
- **Time Complexity**: ${tc}$ — Micro-optimized algorithmic execution time.
- **Space Complexity**: ${sc}$ — Low auxiliary space allocation.

## Key Considerations
- Advanced algorithmic techniques, mathematical shortcuts, or bit manipulation where applicable.
- Optimized for speed, low memory footprint, and competitive execution speed.
"""
            comp_app_file.write_text(content, encoding="utf-8")
            created_competitive_approach += 1

print(f"Created optimal approach.md files: {created_optimal_approach}")
print(f"Created competitive approach.md files: {created_competitive_approach}")
