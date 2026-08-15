"""Auditor and execution verification tool for problem test cases (cases.json).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"


def run_solution_on_case(solution_file: Path, case_input: dict[str, Any]) -> Any:
    spec = importlib.util.spec_from_file_location("solution_mod", solution_file)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {solution_file}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Check for Solution class
    if hasattr(mod, "Solution"):
        sol = mod.Solution()
        methods = [m for m in dir(sol) if not m.startswith("_") and callable(getattr(sol, m))]
        if not methods:
            raise RuntimeError(f"No public methods found in Solution class of {solution_file}")
        method = getattr(sol, methods[0])
        return method(**case_input)
    elif hasattr(mod, "solve"):
        return mod.solve(**case_input)
    else:
        # Look for any top-level function
        funcs = [getattr(mod, f) for f in dir(mod) if not f.startswith("_") and callable(getattr(mod, f))]
        if funcs:
            return funcs[0](**case_input)
        raise RuntimeError(f"No executable function found in {solution_file}")


def audit_package_cases(pkg_dir: Path, auto_fix_visibility: bool = True) -> tuple[bool, list[str]]:
    errors = []
    cases_file = pkg_dir / "cases.json"
    if not cases_file.is_file():
        return False, [f"Missing cases.json in {pkg_dir.name}"]

    try:
        data = json.loads(cases_file.read_text(encoding="utf-8"))
    except Exception as e:
        return False, [f"Invalid JSON in cases.json: {e}"]

    cases = data.get("cases", [])
    if not cases:
        return False, [f"No cases found in cases.json"]

    # 1. Check & Fix visibility
    visibility_fixed = False
    for i, c in enumerate(cases):
        if not c.get("visible", False):
            if auto_fix_visibility:
                c["visible"] = True
                visibility_fixed = True
            else:
                errors.append(f"Case {c.get('id', i)} has visible=False")

    if visibility_fixed:
        cases_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

    # 2. Check sample cases
    sample_cases = [c for c in cases if c.get("kind") == "sample" or "sample" in c.get("tags", [])]
    if not sample_cases:
        errors.append("No sample cases present")

    # 3. Dynamic execution test against solution.py
    sol_file = pkg_dir / "variants" / "optimal" / "solutions" / "solution.py"
    if not sol_file.is_file():
        sol_file = pkg_dir / "solution.py"

    if sol_file.is_file():
        for c in cases:
            cid = c.get("id", "unknown")
            inp = c.get("input", {})
            expected = c.get("expected")
            try:
                actual = run_solution_on_case(sol_file, inp)
                if actual != expected:
                    # Some cases might return lists in different order if allowed, but check exact first
                    errors.append(f"Case {cid} mismatch: expected {expected}, got {actual}")
            except Exception as e:
                errors.append(f"Case {cid} execution exception: {e}")

    return len(errors) == 0, errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit and verify problem cases.json")
    parser.add_argument("--package", type=str, help="Specific package directory path to audit")
    parser.add_argument("--all", action="store_true", help="Audit all packages in corpus")
    args = parser.parse_args()

    if args.package:
        pkg = Path(args.package)
        passed, errs = audit_package_cases(pkg)
        if passed:
            print(f"PASS: {pkg.name} - all cases visible and verified.")
        else:
            print(f"FAIL: {pkg.name} - issues found:")
            for e in errs:
                print(f"  - {e}")
        return

    if args.all:
        pkgs = sorted([p for p in LEETCODE_ROOT.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))])
        passed_count = 0
        failed_count = 0
        for pkg in pkgs:
            passed, errs = audit_package_cases(pkg, auto_fix_visibility=True)
            if passed:
                passed_count += 1
            else:
                failed_count += 1
                print(f"[{pkg.name}] FAIL: {errs}")

        print(f"\nCorpus audit summary: {passed_count} passed, {failed_count} failed out of {len(pkgs)} packages.")


if __name__ == "__main__":
    main()
