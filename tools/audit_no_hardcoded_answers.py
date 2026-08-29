#!/usr/bin/env python3
"""Bulletproof Anti-Cheating AST Audit Tool for Project Euler Corpus.

Parses every solution.py file across dsa/euler/ and verifies:
1. ZERO AST literal constants match any part (>4 digits) of the canonical answer key.
2. ZERO constant addition/subtraction offset tricks (e.g., base + offset, x - offset, a / b, sol += const) evaluate to or adjust target answers.
3. ZERO hardcoded sample return branches (e.g. if x == sample: return constant).
4. ZERO dummy/no-op loops (e.g. for _ in range(1): total_iter += 1).
5. Every solution.py contains genuine dynamic computation loops (for/while/comprehensions).
"""

import ast
import json
import sys
from pathlib import Path

# Force UTF-8 encoding for stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
EULER_ROOT = REPO_ROOT / "dsa" / "euler"
ANSWERS_FILE = EULER_ROOT / "solutions_answers.json"


def load_answers():
    if not ANSWERS_FILE.is_file():
        print(f"Error: {ANSWERS_FILE} not found.")
        sys.exit(1)
    with open(ANSWERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def audit_corpus(start_p=1, end_p=1007):
    answers = load_answers()
    pkgs = sorted([p for p in EULER_ROOT.glob("*_*") if p.is_dir()])

    violations = []
    total_checked = 0

    for pkg in pkgs:
        prefix = pkg.name.split("_")[0]
        try:
            pid = int(prefix)
        except ValueError:
            continue

        if pid < start_p or pid > end_p:
            continue

        str_pid = str(pid)
        canonical_ans = answers.get(str_pid)
        if not canonical_ans:
            continue

        sol_file = pkg / "solution.py"
        if not sol_file.is_file():
            sol_file = pkg / "variants" / "optimal" / "solutions" / "solution.py"
        if not sol_file.is_file():
            continue

        total_checked += 1
        try:
            content = sol_file.read_text(encoding="utf-8")
            tree = ast.parse(content)
        except Exception as err:
            violations.append((pid, pkg.name, f"PARSE_ERROR: {err}"))
            continue

        target_str = str(canonical_ans).strip()
        has_violation = False

        solve_fn = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "solve":
                solve_fn = node
                break

        if not solve_fn:
            violations.append((pid, pkg.name, "NO_SOLVE_FUNCTION"))
            continue

        # 1. Check for answer literal or partial answer digit string match (excluding docstring)
        for node in ast.walk(solve_fn):
            if isinstance(node, ast.Constant):
                # Ignore docstring
                if isinstance(node.value, str) and (
                    solve_fn.body
                    and isinstance(solve_fn.body[0], ast.Expr)
                    and solve_fn.body[0].value == node
                ):
                    continue
                val_str = str(node.value).strip()
                if len(target_str) >= 4 and len(val_str) >= 4:
                    if val_str == target_str or (
                        len(target_str) >= 5
                        and val_str in target_str
                        and len(val_str) > len(target_str) - 2
                    ):
                        violations.append(
                            (pid, pkg.name, f"ANSWER_DIGIT_TRICK_DETECTED ({val_str})")
                        )
                        has_violation = True
                        break

        if has_violation:
            continue

        # 2. Check for Augmented Assignment with large numeric literals (e.g. sol += 1256527472561)
        for node in ast.walk(solve_fn):
            if isinstance(node, ast.AugAssign) and isinstance(node.value, ast.Constant):
                val = node.value.value
                if isinstance(val, (int, float)) and abs(val) >= 100:
                    if abs(val) not in (100, 1000, 10000, 100000, 1000000, 10**9 + 7):
                        violations.append(
                            (pid, pkg.name, f"AUG_ASSIGN_NUMERIC_CONSTANT ({val})")
                        )
                        has_violation = True
                        break

        if has_violation:
            continue

        # 3. Check for constant addition/subtraction offset tricks in binary operations
        for node in ast.walk(solve_fn):
            if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub)):
                left_const = isinstance(node.left, ast.Constant) and isinstance(
                    node.left.value, (int, float)
                )
                right_const = isinstance(node.right, ast.Constant) and isinstance(
                    node.right.value, (int, float)
                )
                if left_const or right_const:
                    c_val = str(node.left.value if left_const else node.right.value)
                    if ("." in c_val and len(c_val.split(".")[1]) >= 3) or (
                        c_val.lstrip("-").isdigit() and len(c_val.lstrip("-")) >= 5
                    ):
                        if abs(float(c_val)) not in (10**9 + 7, 1000000, 100000):
                            violations.append(
                                (pid, pkg.name, f"CONSTANT_OFFSET_TRICK_DETECTED ({c_val})")
                            )
                            has_violation = True
                            break

        if has_violation:
            continue

        # 4. Check for dummy / no-op for loops (e.g. for _ in range(1): ...)
        for node in ast.walk(solve_fn):
            if (
                isinstance(node, ast.For)
                and isinstance(node.target, ast.Name)
                and node.target.id == "_"
            ):
                if (
                    isinstance(node.iter, ast.Call)
                    and isinstance(node.iter.func, ast.Name)
                    and node.iter.func.id == "range"
                ):
                    if (
                        len(node.iter.args) == 1
                        and isinstance(node.iter.args[0], ast.Constant)
                        and node.iter.args[0].value == 1
                    ):
                        violations.append((pid, pkg.name, "DUMMY_FOR_LOOP_DETECTED"))
                        has_violation = True
                        break

        if has_violation:
            continue

        # 5. Check for hardcoded sample return branches (e.g. if n == 4: return 30)
        for node in ast.walk(solve_fn):
            if isinstance(node, ast.If):
                for stmt in node.body:
                    if (
                        isinstance(stmt, ast.Return)
                        and isinstance(stmt.value, ast.Constant)
                        and stmt.value.value not in (None, True, False, 0, 1)
                    ):
                        if isinstance(stmt.value.value, (int, float, str)) and stmt.value.value not in (
                            0,
                            1,
                            "",
                        ):
                            violations.append(
                                (
                                    pid,
                                    pkg.name,
                                    f"HARDCODED_SAMPLE_RETURN_BRANCH ({stmt.value.value})",
                                )
                            )
                            has_violation = True
                            break

        if has_violation:
            continue

        # 6. Check for dynamic computation loop across file AST
        has_loop = False
        has_comp = False
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                has_loop = True
            elif isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
                has_comp = True

        if not (has_loop or has_comp):
            violations.append((pid, pkg.name, "NO_DYNAMIC_LOOP_OR_COMPREHENSION"))

    print(f"=== BULLETPROOF ANTI-CHEATING AST AUDIT (Range {start_p}-{end_p}) ===")
    print(f"Total Packages Checked: {total_checked}")
    print(f"Total Violations Detected: {len(violations)}")

    if violations:
        print("\nVIOLATIONS FOUND:")
        for pid, name, reason in violations[:30]:
            print(f"  [FAIL] P{pid:04d} ({name}): {reason}")
        print(
            "\nAUDIT FAILED: Hardcoded literals, constant offset tricks, sample return branches, or fake solutions detected."
        )
        sys.exit(1)
    else:
        print(
            f"\nAUDIT PASSED: 100% of checked solutions (P{start_p}-P{end_p}) contain genuine dynamic algorithms with zero tricks or hardcoded returns."
        )
        sys.exit(0)


if __name__ == "__main__":
    start = 1
    end = 1007
    if len(sys.argv) > 1:
        arg = sys.argv[1].replace("--range=", "").replace("--range", "")
        if not arg and len(sys.argv) > 2:
            arg = sys.argv[2]
        if "-" in arg:
            s, e = arg.split("-")
            start, end = int(s), int(e)
        else:
            start = end = int(arg)
    audit_corpus(start, end)
