#!/usr/bin/env python3
"""High-speed parallel auditor for all 4,005 packages' test cases vs optimal solutions."""

from __future__ import annotations

import concurrent.futures
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any

# Ensure project root is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Configure logging to suppress noisy debug logs
logging.basicConfig(level=logging.ERROR)
for logger_name in ("server.app.engine_runner", "server.app.special_environments", "httpx"):
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)

from server.app.challenge_packages import (
    leetcode_variant_solution_path,
)
from server.app.engine_runner import run_player_code
from server.app.validated_cases import load_case_suite


def audit_single_package(pkg_path_str: str, timeout_seconds: float = 10.0) -> dict[str, Any]:
    try:
        sys.setrecursionlimit(500_000)
    except Exception:
        pass
    pkg_path = Path(pkg_path_str)
    metadata_path = pkg_path / "metadata.json"
    if not metadata_path.is_file():
        return {"status": "skipped", "pkg": pkg_path.name, "reason": "no metadata"}

    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"status": "failed", "pkg": pkg_path.name, "reason": f"invalid metadata: {exc}"}

    fid = int(metadata.get("frontend_id", 0))
    cid = f"lc_{fid}"
    primary_lang = metadata.get("primary_language", "python")
    category = metadata.get("category", "algorithms")

    cases_path = pkg_path / "cases.json"
    if not cases_path.is_file():
        return {"status": "failed", "cid": cid, "pkg": pkg_path.name, "reason": "missing cases.json"}

    # Load all correctness cases from cases.json
    try:
        suite = load_case_suite(cid)
        cases = [c for c in suite if c.kind != "benchmark"]
    except Exception as exc:
        return {"status": "failed", "cid": cid, "pkg": pkg_path.name, "reason": f"cannot load cases: {exc}"}

    if not cases:
        return {"status": "failed", "cid": cid, "pkg": pkg_path.name, "reason": "empty cases list"}

    # Locate optimal solution
    opt_solution = leetcode_variant_solution_path(cid, "optimal", primary_lang)
    if opt_solution is None or not opt_solution.is_file():
        return {"status": "failed", "cid": cid, "pkg": pkg_path.name, "reason": f"missing optimal solution ({primary_lang})"}

    try:
        source = opt_solution.read_text(encoding="utf-8")
    except Exception as exc:
        return {"status": "failed", "cid": cid, "pkg": pkg_path.name, "reason": f"cannot read solution: {exc}"}

    failed_cases = []
    error_message = ""

    try:
        resp = run_player_code(
            challenge_id=cid,
            source=source,
            language=primary_lang,
            mode="audit",
            run_cases=cases,
            benchmark_cases=[],
        )
        if not resp.correct:
            for cr in resp.case_results:
                if not cr.correct:
                    failed_cases.append({
                        "id": cr.id,
                        "name": cr.name,
                        "error": cr.message or "failed",
                        "returned": cr.return_value_repr,
                        "expected": cr.expected_repr,
                    })
            if not failed_cases:
                error_message = resp.message or "run failed"
    except Exception as exc:
        error_message = str(exc)

    if failed_cases or error_message:
        return {
            "status": "failed",
            "cid": cid,
            "pkg": pkg_path.name,
            "category": category,
            "failed_cases": failed_cases,
            "error": error_message,
            "total_cases": len(cases),
        }

    return {
        "status": "passed",
        "cid": cid,
        "pkg": pkg_path.name,
        "total_cases": len(cases),
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Audit test cases vs optimal solutions")
    parser.add_argument("target", nargs="?", default=None, help="Target package name or frontend id")
    parser.add_argument("--start", type=int, default=0, help="Start package index")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of packages")
    args = parser.parse_args()

    leetcode_dir = Path("dsa/leetcode")

    if args.target and args.target.isdigit():
        target_fid = int(args.target)
        packages = [
            str(p) for p in leetcode_dir.iterdir()
            if p.is_dir() and p.name.startswith(f"{target_fid:04d}_")
        ]
    elif args.target and args.target.startswith("lc_"):
        target_fid = int(args.target.split("_")[1])
        packages = [
            str(p) for p in leetcode_dir.iterdir()
            if p.is_dir() and p.name.startswith(f"{target_fid:04d}_")
        ]
    elif args.target and (leetcode_dir / args.target).is_dir():
        packages = [str(leetcode_dir / args.target)]
    else:
        all_pkgs = sorted([
            str(p) for p in leetcode_dir.iterdir()
            if p.is_dir() and (p / "metadata.json").is_file()
        ])
        start = args.start
        end = start + args.limit if args.limit is not None else len(all_pkgs)
        packages = all_pkgs[start:end]

    total_packages = len(packages)
    max_workers = min(16, os.cpu_count() or 4)
    print(f"Starting audit across {total_packages} packages using {max_workers} worker threads...", flush=True)
    start_time = time.time()

    passed_count = 0
    failed_results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(audit_single_package, pkg): pkg for pkg in packages}
        done_count = 0
        for future in concurrent.futures.as_completed(futures):
            done_count += 1
            if done_count % 250 == 0 or done_count == total_packages:
                print(f"Progress: {done_count}/{total_packages} packages processed ({time.time() - start_time:.1f}s)...", flush=True)
            try:
                res = future.result(timeout=15.0)
                if res["status"] == "passed":
                    passed_count += 1
                else:
                    failed_results.append(res)
            except Exception as exc:
                failed_results.append({"status": "failed", "pkg": futures[future], "reason": str(exc)})

    elapsed = time.time() - start_time
    print("=" * 60, flush=True)
    print(f"AUDIT COMPLETE in {elapsed:.2f}s", flush=True)
    print(f"Total Packages: {total_packages}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {len(failed_results)}")
    print("=" * 60)

    # Save failures report
    failures_file = Path("audit_cases_failures.json")
    failures_file.write_text(json.dumps(failed_results, indent=2), encoding="utf-8")
    print(f"Saved failure details to {failures_file.name}")


if __name__ == "__main__":
    main()
