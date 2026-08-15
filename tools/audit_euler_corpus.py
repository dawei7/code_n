"""Corpus Audit and Verification Report Generator for Project Euler."""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from server.app.config import EULER_ROOT

ANSWERS_FILE = EULER_ROOT / "solutions_answers.json"
REPORT_JSON = EULER_ROOT / "_reports" / "euler_corpus_report.json"
REPORT_MD = EULER_ROOT / "_reports" / "euler_corpus_report.md"


def load_answers() -> dict[str, str]:
    if not ANSWERS_FILE.is_file():
        return {}
    return json.loads(ANSWERS_FILE.read_text(encoding="utf-8"))


def analyze_ast(sol_file: Path) -> dict:
    if not sol_file.is_file():
        return {"has_solution_file": False, "is_real_algorithm": False, "reason": "MISSING_FILE"}

    try:
        content = sol_file.read_text(encoding="utf-8")
        tree = ast.parse(content)
    except Exception as err:
        return {"has_solution_file": True, "is_real_algorithm": False, "reason": f"AST_PARSE_ERROR: {err}"}

    solve_def = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "solve":
            solve_def = node
            break

    if not solve_def:
        return {"has_solution_file": True, "is_real_algorithm": False, "reason": "NO_SOLVE_FUNCTION"}

    # Remove docstrings and pass statements
    meaningful_stmts = []
    for stmt in solve_def.body:
        if isinstance(stmt, ast.Pass):
            continue
        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str):
            continue
        meaningful_stmts.append(stmt)

    if not meaningful_stmts:
        return {"has_solution_file": True, "is_real_algorithm": False, "reason": "EMPTY_OR_STUB"}

    # Single return constant check
    if len(meaningful_stmts) == 1 and isinstance(meaningful_stmts[0], ast.Return):
        ret_val = meaningful_stmts[0].value
        if isinstance(ret_val, ast.Constant):
            return {"has_solution_file": True, "is_real_algorithm": False, "reason": "DIRECT_RETURN_CONSTANT"}
        if isinstance(ret_val, ast.UnaryOp) and isinstance(ret_val.operand, ast.Constant):
            return {"has_solution_file": True, "is_real_algorithm": False, "reason": "DIRECT_RETURN_CONSTANT"}

    return {"has_solution_file": True, "is_real_algorithm": True, "reason": "VALID_ALGORITHM"}


def verify_solution(p_id: int, sol_file: Path, expected_answer: str, timeout_sec: float = 60.0) -> dict:
    if not sol_file.is_file():
        return {"status": "MISSING_SOLUTION", "passed": False, "elapsed_seconds": 0.0}

    spec = importlib.util.spec_from_file_location(f"euler_eval_{p_id}", sol_file)
    if not spec or not spec.loader:
        return {"status": "IMPORT_ERROR", "passed": False, "elapsed_seconds": 0.0}

    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as err:
        return {"status": "IMPORT_FAILED", "error": str(err), "passed": False, "elapsed_seconds": 0.0}

    solve_fn = getattr(module, "solve", None)
    if not callable(solve_fn):
        return {"status": "NO_SOLVE_FN", "passed": False, "elapsed_seconds": 0.0}

    t0 = time.perf_counter()
    try:
        result = solve_fn()
        elapsed = time.perf_counter() - t0
        res_str = str(result).strip() if result is not None else ""

        if elapsed > timeout_sec:
            return {
                "status": "TIMEOUT_EXCEEDED",
                "passed": False,
                "result": res_str,
                "expected": expected_answer,
                "elapsed_seconds": round(elapsed, 4),
            }

        passed = (res_str == expected_answer.strip()) if expected_answer else False
        return {
            "status": "PASS" if passed else "WRONG_ANSWER",
            "passed": passed,
            "result": res_str,
            "expected": expected_answer,
            "elapsed_seconds": round(elapsed, 4),
        }
    except Exception as err:
        elapsed = time.perf_counter() - t0
        return {
            "status": "RUNTIME_ERROR",
            "error": str(err),
            "passed": False,
            "elapsed_seconds": round(elapsed, 4),
        }


def check_approach_quality(app_file: Path) -> dict:
    if not app_file.is_file():
        return {"status": "MISSING", "line_count": 0, "has_latex": False}

    content = app_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    line_count = len(lines)
    has_latex = bool(re.search(r"\$.*?\$", content))

    is_extensive = (line_count >= 30) and has_latex
    return {
        "status": "EXTENSIVE" if is_extensive else "BASIC",
        "line_count": line_count,
        "word_count": len(content.split()),
        "has_latex": has_latex,
    }


def audit_corpus(start_id: int = 1, end_id: int = 1007, run_solver: bool = True) -> dict:
    answers = load_answers()
    pkgs = sorted([p for p in EULER_ROOT.glob("*_*") if p.is_dir()])

    results = []
    summary = {
        "total_packages": 0,
        "real_algo_verified": 0,
        "pending_real_algorithm": 0,
        "failed_verification": 0,
        "timeout_exceeded": 0,
        "extensive_approach_docs": 0,
        "basic_approach_docs": 0,
    }

    for pkg in pkgs:
        pid_str = pkg.name.split("_")[0]
        try:
            p_id = int(pid_str)
        except ValueError:
            continue

        if not (start_id <= p_id <= end_id):
            continue

        summary["total_packages"] += 1

        sol_file = pkg / "variants" / "optimal" / "solutions" / "solution.py"
        app_file = pkg / "variants" / "optimal" / "approach.md"
        expected = answers.get(str(p_id), "")

        ast_res = analyze_ast(sol_file)
        app_res = check_approach_quality(app_file)

        if app_res["status"] == "EXTENSIVE":
            summary["extensive_approach_docs"] += 1
        else:
            summary["basic_approach_docs"] += 1

        if not ast_res["is_real_algorithm"]:
            summary["pending_real_algorithm"] += 1
            results.append({
                "id": p_id,
                "name": pkg.name,
                "status": "PENDING_REAL_ALGORITHM",
                "ast_reason": ast_res["reason"],
                "approach_quality": app_res["status"],
                "approach_lines": app_res["line_count"],
            })
            continue

        if run_solver:
            ver_res = verify_solution(p_id, sol_file, expected)
            if ver_res["passed"]:
                summary["real_algo_verified"] += 1
                status = "REAL_ALGO_VERIFIED"
            elif ver_res["status"] == "TIMEOUT_EXCEEDED":
                summary["timeout_exceeded"] += 1
                status = "TIMEOUT_EXCEEDED"
            else:
                summary["failed_verification"] += 1
                status = "FAILED_VERIFICATION"

            results.append({
                "id": p_id,
                "name": pkg.name,
                "status": status,
                "elapsed_seconds": ver_res.get("elapsed_seconds", 0.0),
                "expected": expected,
                "got": ver_res.get("result", ""),
                "approach_quality": app_res["status"],
                "approach_lines": app_res["line_count"],
            })
        else:
            summary["real_algo_verified"] += 1
            results.append({
                "id": p_id,
                "name": pkg.name,
                "status": "REAL_ALGO_UNTESTED",
                "approach_quality": app_res["status"],
                "approach_lines": app_res["line_count"],
            })

    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": summary,
        "packages": results,
    }

    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(output, indent=2), encoding="utf-8")
    
    # Write Markdown summary
    md_content = f"""# Project Euler Corpus Audit & Status Report

Generated: `{output['timestamp']}`

## Summary Statistics

| Metric | Count | Percentage |
| :--- | :---: | :---: |
| **Total Evaluated Packages** | **{summary['total_packages']}** | 100.0% |
| **Real Algorithmic Solutions (Verified)** | **{summary['real_algo_verified']}** | {summary['real_algo_verified']/max(1, summary['total_packages'])*100:.1f}% |
| **Pending Real Algorithm (Purged/Stubs)** | **{summary['pending_real_algorithm']}** | {summary['pending_real_algorithm']/max(1, summary['total_packages'])*100:.1f}% |
| **Failed Verification / Wrong Answer** | **{summary['failed_verification']}** | {summary['failed_verification']/max(1, summary['total_packages'])*100:.1f}% |
| **Timeout Exceeded (>60s Limit)** | **{summary['timeout_exceeded']}** | {summary['timeout_exceeded']/max(1, summary['total_packages'])*100:.1f}% |
| **Extensive Approach Docs (>=30 lines + LaTeX)** | **{summary['extensive_approach_docs']}** | {summary['extensive_approach_docs']/max(1, summary['total_packages'])*100:.1f}% |
| **Basic Approach Docs (<30 lines)** | **{summary['basic_approach_docs']}** | {summary['basic_approach_docs']/max(1, summary['total_packages'])*100:.1f}% |
"""
    REPORT_MD.write_text(md_content, encoding="utf-8")
    return output


def main():
    parser = argparse.ArgumentParser(description="Audit Project Euler corpus.")
    parser.add_argument("--start", type=int, default=1, help="Start problem ID")
    parser.add_argument("--end", type=int, default=1007, help="End problem ID")
    parser.add_argument("--no-solver", action="store_true", help="Skip running solve() verifier")
    args = parser.parse_args()

    print(f"Auditing Project Euler corpus (problems {args.start} to {args.end})...")
    res = audit_corpus(args.start, args.end, run_solver=not args.no_solver)
    sum_data = res["summary"]

    print("\n--- Audit Summary ---")
    print(f"Total Packages: {sum_data['total_packages']}")
    print(f"Real Algorithmic Solutions Verified: {sum_data['real_algo_verified']}")
    print(f"Pending Real Algorithm (Stubs): {sum_data['pending_real_algorithm']}")
    print(f"Failed Verification: {sum_data['failed_verification']}")
    print(f"Timeout Exceeded (>60s): {sum_data['timeout_exceeded']}")
    print(f"Extensive Approach Docs: {sum_data['extensive_approach_docs']}")
    print(f"Basic Approach Docs: {sum_data['basic_approach_docs']}")


if __name__ == "__main__":
    main()
