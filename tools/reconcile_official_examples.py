import json, re, ast, sys
from pathlib import Path

REPO_ROOT = Path("c:/dawei7/code_n")
sys.path.insert(0, str(REPO_ROOT))

from server.app.engine_runner import run_player_code
from server.app.challenge_packages import leetcode_variant_solution_path
from server.app.validated_cases import ValidatedCase

LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"


def parse_markdown_examples(desc_text: str):
    examples = []
    ex_pattern = re.compile(
        r"####\s+Example\s+(\d+)\s*\n+(.*?)(?=\n+####|\n+###|\Z)",
        re.DOTALL
    )
    for m in ex_pattern.finditer(desc_text):
        ex_num = int(m.group(1))
        content = m.group(2)
        
        inp_m = re.search(r"-\s+\*\*Input:\*\*\s*(.+?)(?=\n\s*-\s+\*\*Output:|\Z)", content, re.DOTALL)
        out_m = re.search(r"-\s+\*\*Output:\*\*\s*(.+?)(?=\n\s*-\s+\*\*Explanation:|\n\s*-\s+\*\*Note:|\n\s*-\s+\*\*Constraints:|\n\s*###|\Z)", content, re.DOTALL)
        
        if inp_m and out_m:
            raw_inp = inp_m.group(1).strip()
            raw_out = out_m.group(1).strip()
            examples.append({
                "num": ex_num,
                "raw_inp": raw_inp,
                "raw_out": raw_out
            })
    return examples


def parse_assignment_input(raw_inp: str):
    s = raw_inp.strip().strip("$`")
    parts = []
    current = []
    in_quote = False
    quote_char = ''
    bracket_depth = 0
    
    for ch in s:
        if ch in ('"', "'") and not in_quote:
            in_quote = True
            quote_char = ch
            current.append(ch)
        elif in_quote and ch == quote_char:
            in_quote = False
            current.append(ch)
        elif not in_quote and ch in ('[', '{', '('):
            bracket_depth += 1
            current.append(ch)
        elif not in_quote and ch in (']', '}', ')'):
            bracket_depth -= 1
            current.append(ch)
        elif not in_quote and bracket_depth == 0 and ch == ',':
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current).strip())
        
    inp_dict = {}
    for part in parts:
        if '=' in part:
            k, v = part.split('=', 1)
            k = k.strip().strip("$`")
            v = v.strip().strip("$`")
            try:
                v_clean = v.replace("true", "True").replace("false", "False").replace("null", "None")
                val = ast.literal_eval(v_clean)
                inp_dict[k] = val
            except Exception:
                inp_dict[k] = v
        else:
            return None
    return inp_dict


def eval_solution_for_case(cid: str, pkg_dir: Path, inp: dict):
    meta = json.loads((pkg_dir / "metadata.json").read_text(encoding="utf-8"))
    lang = meta.get("primary_language", "python")
    sol_file = leetcode_variant_solution_path(cid, "optimal", lang) or (pkg_dir / "solution.py")
    source = sol_file.read_text(encoding="utf-8")
    
    test_case = ValidatedCase(
        id="test-dyn-eval",
        name="test",
        kind="trial",
        visible=True,
        input=inp,
        expected=None
    )
    res = run_player_code(
        challenge_id=cid,
        source=source,
        language=lang,
        mode="audit",
        run_cases=[test_case],
        benchmark_cases=[]
    )
    if res.case_results:
        cr = res.case_results[0]
        if cr.passed or cr.return_value_repr is not None:
            try:
                return json.loads(cr.return_value_repr)
            except Exception:
                return ast.literal_eval(cr.return_value_repr)
    raise RuntimeError(f"Dynamic evaluation failed for {cid} on input {inp}: {res.message}")


def reconcile_package(pkg_name: str):
    pkg_dir = LEETCODE_ROOT / pkg_name
    desc_p = pkg_dir / "reference" / "description.md"
    if not desc_p.exists():
        desc_p = pkg_dir / "doc.md"
    if not desc_p.exists():
        return
        
    cases_p = pkg_dir / "cases.json"
    if not cases_p.exists():
        return
        
    cases_data = json.loads(cases_p.read_text(encoding="utf-8"))
    cases_list = cases_data.get("cases", [])
    meta = json.loads((pkg_dir / "metadata.json").read_text(encoding="utf-8"))
    cid = f"lc_{meta['frontend_id']}"
    
    exs = parse_markdown_examples(desc_p.read_text(encoding="utf-8"))
    if not exs:
        return
        
    modified = False
    
    for ex in exs:
        parsed_inp = parse_assignment_input(ex["raw_inp"])
        if parsed_inp is None:
            continue
            
        # Check if already present
        matched = None
        for c in cases_list:
            if c["input"] == parsed_inp:
                matched = c
                break
                
        if matched:
            # Promote trial to sample if needed
            if matched.get("kind") != "sample":
                matched["kind"] = "sample"
                if "tags" not in matched:
                    matched["tags"] = []
                if "sample" not in matched["tags"]:
                    matched["tags"].insert(0, "sample")
                modified = True
        else:
            # Missing case: dynamically compute expected value using canonical solution
            try:
                expected_val = eval_solution_for_case(cid, pkg_dir, parsed_inp)
                new_case = {
                    "id": f"sample-{ex['num']}",
                    "name": f"sample: example {ex['num']}",
                    "kind": "sample",
                    "visible": True,
                    "input": parsed_inp,
                    "expected": expected_val,
                    "tags": ["sample"]
                }
                # Find position to insert (after existing samples)
                sample_idx = 0
                for i, c in enumerate(cases_list):
                    if c.get("kind") == "sample" or "sample" in c.get("tags", []):
                        sample_idx = i + 1
                cases_list.insert(sample_idx, new_case)
                modified = True
                print(f"  [{pkg_name}] Added missing Example {ex['num']}: {parsed_inp} => {expected_val}")
            except Exception as e:
                print(f"  [WARN] Failed to dynamically eval Example {ex['num']} for {pkg_name}: {e}")
                
    if modified:
        cases_data["cases"] = cases_list
        cases_p.write_text(json.dumps(cases_data, indent=2), encoding="utf-8")
        print(f"Updated {pkg_name}/cases.json")


def main():
    report_path = LEETCODE_ROOT / "_reports" / "instruction_case_violations.json"
    report_data = json.loads(report_path.read_text(encoding="utf-8"))
    missing_ex_pkgs = [k for k, v in report_data['packages'].items() if any(w['type'] == 'missing_official_example' for w in v.get('coverage_warnings', []))]
    
    print(f"Starting reconciliation across {len(missing_ex_pkgs)} packages with missing official examples...")
    for pkg in missing_ex_pkgs:
        reconcile_package(pkg)
    print("Reconciliation complete!")


if __name__ == "__main__":
    main()
