#!/usr/bin/env python3
"""Rigorous 1-by-1 problem instruction, constraint, and test case alignment auditor.

Compares every problem's instructions, mathematical constraints, and official examples
against cases.json across problems 1 to 4005. Never modifies solution code.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
REPORT_FILE = LEETCODE_ROOT / "_reports" / "instruction_case_violations.json"


def eval_math_expr(s: str) -> int:
    s = s.strip()
    is_neg = False
    if s.startswith("-"):
        is_neg = True
        s = s[1:].strip()
    elif s.startswith("+"):
        s = s[1:].strip()

    s = s.replace(" ", "")
    m_mul = re.match(r"^(\d+)\*(?:10\^(\d+))$", s)
    if m_mul:
        val = int(m_mul.group(1)) * (10 ** int(m_mul.group(2)))
        return -val if is_neg else val

    m_pow = re.match(r"^(\d+)\^(\d+)$", s)
    if m_pow:
        val = int(m_pow.group(1)) ** int(m_pow.group(2))
        return -val if is_neg else val

    m_pow_sub = re.match(r"^(\d+)\^(\d+)-1$", s)
    if m_pow_sub:
        val = (int(m_pow_sub.group(1)) ** int(m_pow_sub.group(2))) - 1
        return -val if is_neg else val

    val = int(s)
    return -val if is_neg else val


def extract_problem_spec(pkg_dir: Path) -> dict[str, Any]:
    desc_file = pkg_dir / "reference" / "description.md"
    if not desc_file.is_file():
        desc_file = pkg_dir / "doc.md"
    if not desc_file.is_file():
        return {"error": "Missing description/doc markdown"}

    text = desc_file.read_text(encoding="utf-8")

    # Extract official examples
    examples = []
    ex_blocks = re.split(r"####?\s*Example\s*\d+", text, flags=re.I)
    for block in ex_blocks[1:]:
        m_inp = re.search(r"Input:\*?\*?\s*(.+?)(?=\n|\r|\*?\*?Output)", block, re.I)
        m_out = re.search(r"Output:\*?\*?\s*(.+?)(?=\n|\r|\*?\*?Explanation|\Z)", block, re.I)
        if m_inp and m_out:
            examples.append({
                "input_raw": m_inp.group(1).strip(),
                "output_raw": m_out.group(1).strip(),
            })

    # Extract constraint lines
    constraints = []
    m_cons = re.search(r"###\s*(?:\d+\.\s*)?Constraints\b(.*?)(?=###|\Z)", text, re.DOTALL | re.I)
    if not m_cons:
        m_cons = re.search(r"\bConstraints:?\b(.*?)(?=\bExample|\bFollow-up|\Z)", text, re.DOTALL | re.I)
    if m_cons:
        for line in m_cons.group(1).split("\n"):
            line = line.strip()
            if line.startswith("-") or line.startswith("*"):
                c = line.lstrip("-* ").strip()
                if c:
                    constraints.append(c)

    return {
        "text": text,
        "examples": examples,
        "constraints": constraints,
    }


def parse_numeric_bounds(constraint_str: str) -> list[dict[str, Any]]:
    bounds = []
    s = constraint_str.replace("$", "").replace("`", "")
    s = s.replace("\\le", "<=").replace("\\ge", ">=").replace("\\leq", "<=").replace("\\geq", ">=")
    s = s.replace("\\cdot", "*").replace("\\times", "*").replace("×", "*").replace("✕", "*")
    s = s.replace("^{", "^").replace("}", "")

    # Pattern: MIN <= VAR <= MAX
    p1 = re.compile(
        r"(-?\s*\d+(?:\s*\*\s*10\^\d+|\^\d+(?:\s*-\s*1)?)?)\s*<=\s*([a-zA-Z0-9_.\[\]]+)\s*<=\s*(-?\s*\d+(?:\s*\*\s*10\^\d+|\^\d+(?:\s*-\s*1)?)?)"
    )
    for m in p1.finditer(s):
        try:
            min_v = eval_math_expr(m.group(1))
            var_name = m.group(2).strip()
            max_v = eval_math_expr(m.group(3))
            bounds.append({"var": var_name, "min": min_v, "max": max_v})
        except Exception:
            pass

    # Pattern: MIN <= VAR1 <= VAR2 <= MAX (chain bounds with powers/math)
    expr_pat = r"(-?\s*\d+(?:\s*\*\s*10\^\d+|\^\d+(?:\s*-\s*1)?)?)"
    p_chain = re.compile(rf"{expr_pat}\s*<=\s*([a-zA-Z0-9_]+)\s*<=\s*([a-zA-Z0-9_]+)\s*<=\s*{expr_pat}")
    for m in p_chain.finditer(s):
        try:
            min_v = eval_math_expr(m.group(1))
            var1 = m.group(2).strip()
            var2 = m.group(3).strip()
            max_v = eval_math_expr(m.group(4))
            bounds.append({"var": var1, "min": min_v, "max": max_v})
            bounds.append({"var": var2, "min": min_v, "max": max_v})
        except Exception:
            pass

    return bounds


def audit_single_package(pkg_dir: Path) -> dict[str, Any]:
    cases_file = pkg_dir / "cases.json"
    meta_file = pkg_dir / "metadata.json"
    if not cases_file.is_file() or not meta_file.is_file():
        return {"status": "error", "pkg": pkg_dir.name, "message": "missing cases.json or metadata.json"}

    try:
        cases_data = json.loads(cases_file.read_text(encoding="utf-8"))
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
    except Exception as e:
        return {"status": "error", "pkg": pkg_dir.name, "message": f"corrupt json: {e}"}

    cases = cases_data.get("cases", [])
    if not cases:
        return {"status": "error", "pkg": pkg_dir.name, "message": "empty cases array"}

    spec = extract_problem_spec(pkg_dir)
    if "error" in spec:
        return {"status": "error", "pkg": pkg_dir.name, "message": spec["error"]}

    violations = []
    coverage_warnings = []

    # 1. Parse numeric length & value bounds
    length_bounds = {}
    value_bounds = {}
    for c_text in spec["constraints"]:
        for b in parse_numeric_bounds(c_text):
            vname = b["var"].lower()
            if "length" in vname or "len" in vname or vname in ("n", "m", "sz", "k"):
                length_bounds[vname] = b
            else:
                value_bounds[vname] = b

    # 2. Extract semantic constraints with specific parameter scoping
    text = spec["text"]
    
    # Specific parameter lowercase check (strictly only lowercase, no spaces or special symbols)
    lowercase_params = set()
    for m in re.finditer(r"`?([a-zA-Z0-9_]+)`?\s+(?:consists|contains) of only lowercase English letters(?:\.|\s*\Z)", text, re.I):
        lowercase_params.add(m.group(1))
    for m in re.finditer(r"`?([a-zA-Z0-9_]+)`?\s+contains? only lowercase English letters(?:\.|\s*\Z)", text, re.I):
        lowercase_params.add(m.group(1))

    # Binary string parameter check
    binary_params = set()
    for m in re.finditer(r"`?([a-zA-Z0-9_]+)`?\s+is a binary string|consists of (?:only )?'0' and '1'", text, re.I):
        binary_params.add(m.group(1))

    # Unique / distinct check
    unique_params = set()
    for m in re.finditer(r"all (?:the )?integers in `?([a-zA-Z0-9_]+)`? are (?:unique|distinct)", text, re.I):
        unique_params.add(m.group(1))
    for m in re.finditer(r"all elements in `?([a-zA-Z0-9_]+)`? are (?:unique|distinct)", text, re.I):
        unique_params.add(m.group(1))

    # Strictly positive check
    positive_params = set()
    for m in re.finditer(r"`?([a-zA-Z0-9_]+)`? is a positive integer", text, re.I):
        positive_params.add(m.group(1))

    # 3. Check each case against instructions & constraints
    for c in cases:
        cid = c.get("id", "unknown")
        inp = c.get("input", {})

        # Length checks
        for param_name, val in inp.items():
            if isinstance(val, (list, str)):
                actual_len = len(val)
                p_lower = param_name.lower()
                for lb_name, lb in length_bounds.items():
                    applies = False
                    if lb_name in (f"{p_lower}.length", f"len({p_lower})", f"length({p_lower})") or f"{p_lower}.length" in lb_name:
                        applies = True
                    elif lb_name in ("n", "m", "sz", "k") and (
                        f"{lb_name} == {p_lower}.length" in text.lower() or
                        f"{lb_name} = {p_lower}.length" in text.lower() or
                        f"{p_lower}.length == {lb_name}" in text.lower() or
                        f"{p_lower}.length = {lb_name}" in text.lower() or
                        (lb_name == "sz" and p_lower == "head" and "number of nodes" in text.lower())
                    ):
                        applies = True

                    if applies:
                        if actual_len < lb["min"]:
                            violations.append({
                                "case_id": cid,
                                "type": "length_underflow",
                                "param": param_name,
                                "actual": actual_len,
                                "min_allowed": lb["min"],
                                "rule": f"{lb['min']} <= len({param_name})",
                            })
                        elif actual_len > lb["max"]:
                            violations.append({
                                "case_id": cid,
                                "type": "length_overflow",
                                "param": param_name,
                                "actual": actual_len,
                                "max_allowed": lb["max"],
                                "rule": f"len({param_name}) <= {lb['max']}",
                            })

        # Value bounds checks
        for param_name, val in inp.items():
            p_lower = param_name.lower()
            if isinstance(val, int) and not isinstance(val, bool):
                for vb_name, vb in value_bounds.items():
                    if p_lower == vb_name:
                        if val < vb["min"]:
                            violations.append({
                                "case_id": cid,
                                "type": "value_underflow",
                                "param": param_name,
                                "actual": val,
                                "min_allowed": vb["min"],
                                "rule": f"{vb['min']} <= {param_name}",
                            })
                        elif val > vb["max"]:
                            violations.append({
                                "case_id": cid,
                                "type": "value_overflow",
                                "param": param_name,
                                "actual": val,
                                "max_allowed": vb["max"],
                                "rule": f"{param_name} <= {vb['max']}",
                            })

            elif isinstance(val, list) and val and isinstance(val[0], int) and not isinstance(val[0], bool):
                for vb_name, vb in value_bounds.items():
                    if vb_name in (p_lower, f"{p_lower}[i]", f"{p_lower}[j]", f"{p_lower}[k]") or f"{p_lower}[" in vb_name:
                        for idx, item in enumerate(val):
                            if item < vb["min"]:
                                violations.append({
                                    "case_id": cid,
                                    "type": "array_element_underflow",
                                    "param": f"{param_name}[{idx}]",
                                    "actual": item,
                                    "min_allowed": vb["min"],
                                    "rule": f"{vb['min']} <= {param_name}[i]",
                                })
                                break
                            elif item > vb["max"]:
                                violations.append({
                                    "case_id": cid,
                                    "type": "array_element_overflow",
                                    "param": f"{param_name}[{idx}]",
                                    "actual": item,
                                    "max_allowed": vb["max"],
                                    "rule": f"{param_name}[i] <= {vb['max']}",
                                })
                                break

        # Parameter-specific charset check
        for p_name in lowercase_params:
            if p_name in inp and isinstance(inp[p_name], str) and inp[p_name]:
                val = inp[p_name]
                if not val.islower() or not val.isalpha():
                    violations.append({
                        "case_id": cid,
                        "type": "charset_violation",
                        "param": p_name,
                        "actual": val,
                        "rule": f"{p_name} must consist only of lowercase English letters",
                    })

        # Binary string check
        for p_name in binary_params:
            if p_name in inp and isinstance(inp[p_name], str):
                val = inp[p_name]
                if not all(ch in "01" for ch in val):
                    violations.append({
                        "case_id": cid,
                        "type": "binary_charset_violation",
                        "param": p_name,
                        "actual": val,
                        "rule": f"{p_name} must be a binary string ('0' and '1')",
                    })

        # Uniqueness check
        for p_name in unique_params:
            if p_name in inp and isinstance(inp[p_name], list) and inp[p_name]:
                val = inp[p_name]
                if len(val) != len(set(val)):
                    violations.append({
                        "case_id": cid,
                        "type": "uniqueness_violation",
                        "param": p_name,
                        "actual": f"duplicates in list of len {len(val)}",
                        "rule": f"all elements in {p_name} must be unique",
                    })

        # Strictly positive check
        for p_name in positive_params:
            if p_name in inp and isinstance(inp[p_name], int) and not isinstance(inp[p_name], bool):
                val = inp[p_name]
                if val <= 0:
                    violations.append({
                        "case_id": cid,
                        "type": "positive_integer_violation",
                        "param": p_name,
                        "actual": val,
                        "rule": f"{p_name} must be a positive integer (> 0)",
                    })

    # Check for empty boundary coverage
    for lb_name, lb in length_bounds.items():
        if lb["min"] == 0:
            def check_val(v):
                if isinstance(v, (list, str)) and len(v) == 0:
                    return True
                if isinstance(v, int) and not isinstance(v, bool) and v == 0:
                    return True
                if isinstance(v, list):
                    return any(check_val(item) for item in v)
                return False

            has_empty = any(
                any(check_val(v) for v in c.get("input", {}).values())
                for c in cases
            )
            if not has_empty:
                coverage_warnings.append({
                    "type": "missing_empty_boundary",
                    "rule": f"0 <= {lb_name} allows empty input, but no empty input case exists in cases.json",
                })

    # Check official example count
    sample_cases = [c for c in cases if c.get("kind") == "sample" or "sample" in c.get("tags", [])]
    if len(spec["examples"]) > len(sample_cases):
        coverage_warnings.append({
            "type": "missing_official_example",
            "rule": f"Problem description specifies {len(spec['examples'])} examples, but cases.json only has {len(sample_cases)} sample cases",
        })

    return {
        "status": "passed" if not violations else "violations_found",
        "pkg": pkg_dir.name,
        "frontend_id": meta.get("frontend_id"),
        "category": meta.get("category"),
        "total_cases": len(cases),
        "sample_cases": len(sample_cases),
        "constraints_count": len(spec["constraints"]),
        "violations": violations,
        "coverage_warnings": coverage_warnings,
    }


def run_sequential_audit(start_id: int = 1, limit: int | None = None) -> None:
    all_pkgs = sorted([
        p for p in LEETCODE_ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    ])

    pkgs_to_run = []
    for p in all_pkgs:
        prefix = p.name.split("_")[0]
        if prefix.isdigit() and int(prefix) >= start_id:
            pkgs_to_run.append(p)

    if limit is not None:
        pkgs_to_run = pkgs_to_run[:limit]

    total = len(pkgs_to_run)
    print(f"Starting 1-by-1 problem instruction audit across {total} packages (from ID {start_id})...", flush=True)

    results = []
    violations_summary = []
    warnings_summary = []
    passed_count = 0

    start_time = time.time()

    for idx, pkg in enumerate(pkgs_to_run, start=1):
        res = audit_single_package(pkg)
        results.append(res)

        if res.get("violations"):
            violations_summary.append(res)
            print(f"[{idx}/{total}] {pkg.name}: {len(res['violations'])} CONSTRAINT VIOLATIONS FOUND!", flush=True)
            for v in res["violations"]:
                print(f"    - Case {v['case_id']}: {v['type']} on '{v['param']}' ({v['rule']}, actual={v['actual']})", flush=True)
        elif res.get("coverage_warnings"):
            warnings_summary.append(res)
            passed_count += 1
            if idx % 100 == 0 or len(res["coverage_warnings"]) > 1:
                print(f"[{idx}/{total}] {pkg.name}: Passed with {len(res['coverage_warnings'])} coverage warnings", flush=True)
        else:
            passed_count += 1
            if idx % 200 == 0:
                print(f"[{idx}/{total}] {pkg.name}: Fully compliant ({res['total_cases']} cases, {res['constraints_count']} constraints)", flush=True)

    elapsed = time.time() - start_time
    print("\n" + "=" * 60, flush=True)
    print(f"AUDIT BATCH COMPLETE in {elapsed:.2f}s", flush=True)
    print(f"Total Packages Checked: {total}")
    print(f"Clean Pass (Zero Violations): {passed_count}")
    print(f"Packages with Constraint Violations: {len(violations_summary)}")
    print(f"Packages with Coverage Warnings: {len(warnings_summary)}")
    print("=" * 60, flush=True)

    # Load existing report or create new
    existing_report = {}
    if REPORT_FILE.is_file():
        try:
            existing_report = json.loads(REPORT_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass

    records = existing_report.get("packages", {})
    for r in results:
        records[r["pkg"]] = r

    final_payload = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_packages_audited": len(records),
        "violations_count": sum(len(r.get("violations", [])) for r in records.values()),
        "packages_with_violations": [r["pkg"] for r in records.values() if r.get("violations")],
        "packages": records,
    }

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(json.dumps(final_payload, indent=2), encoding="utf-8")
    print(f"Saved audit findings to {REPORT_FILE}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit test cases vs problem instructions")
    parser.add_argument("--start-id", type=int, default=1, help="Frontend ID to start from")
    parser.add_argument("--limit", type=int, default=None, help="Number of packages to audit in this run")
    args = parser.parse_args()

    run_sequential_audit(start_id=args.start_id, limit=args.limit)


if __name__ == "__main__":
    main()
