"""Runner and verifier for Project Euler optimal Python solutions."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path

# Ensure project root in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from server.app.config import EULER_ROOT

ANSWERS_FILE = EULER_ROOT / "solutions_answers.json"
REPORT_FILE = EULER_ROOT / "verification_report.json"


def load_answers() -> dict[str, str]:
    if not ANSWERS_FILE.is_file():
        return {}
    return json.loads(ANSWERS_FILE.read_text(encoding="utf-8"))


def get_package_dir(p_id: int) -> Path | None:
    num_str = str(p_id).zfill(4)
    matches = list(EULER_ROOT.glob(f"{num_str}_*"))
    return matches[0] if matches else None


from tools.run_euler_protected import run_solution_protected


def verify_problem(p_id: int, expected_answer: str) -> dict:
    pkg_dir = get_package_dir(p_id)
    if not pkg_dir:
        return {"id": p_id, "status": "MISSING_PACKAGE", "passed": False}

    sol_file = pkg_dir / "variants" / "optimal" / "solutions" / "solution.py"
    if not sol_file.is_file():
        return {"id": p_id, "status": "MISSING_SOLUTION", "passed": False}

    # Run solution in protected isolated process with 8GB RAM limit & 300s timeout
    res = run_solution_protected(sol_file, solve_fn_name="solve")
    status = res.get("status")

    if status == "SUCCESS":
        res_str = str(res.get("result", "")).strip()
        passed = (res_str == expected_answer.strip())
        return {
            "id": p_id,
            "status": "PASS" if passed else "WRONG_ANSWER",
            "passed": passed,
            "result": res_str,
            "expected": expected_answer,
            "elapsed_seconds": res.get("elapsed_seconds", 0.0),
            "peak_memory_mb": res.get("peak_memory_mb", 0.0),
        }
    else:
        return {
            "id": p_id,
            "status": status or "RUNTIME_ERROR",
            "error": res.get("error", "Unknown error"),
            "passed": False,
            "elapsed_seconds": res.get("elapsed_seconds", 0.0),
            "peak_memory_mb": res.get("peak_memory_mb", 0.0),
        }


def main():
    parser = argparse.ArgumentParser(description="Verify Project Euler Python solutions.")
    parser.add_argument("--start", type=int, default=1, help="Start problem ID")
    parser.add_argument("--end", type=int, default=50, help="End problem ID")
    args = parser.parse_args()

    answers = load_answers()
    print(f"Loaded {len(answers)} target answers.")
    print(f"Verifying Project Euler problems {args.start} to {args.end}...")

    results = []
    passed_count = 0
    failed_count = 0

    for p_id in range(args.start, args.end + 1):
        expected = answers.get(str(p_id), "")
        res = verify_problem(p_id, expected)
        results.append(res)
        if res["passed"]:
            passed_count += 1
            print(f"Problem {p_id:04d}: PASS ({res['elapsed_seconds']}s, RAM: {res.get('peak_memory_mb', 0)}MB)")
        else:
            failed_count += 1
            reason = res.get('error') or f"Got {res.get('result')}, Expected {res.get('expected')}"
            print(f"Problem {p_id:04d}: {res['status']} ({reason}) (RAM: {res.get('peak_memory_mb', 0)}MB)")

    print(f"\nVerification summary for {args.start}-{args.end}: {passed_count} PASSED, {failed_count} FAILED.")


if __name__ == "__main__":
    main()
