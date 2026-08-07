import json
import re
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

def convert_prose_to_latex(text: str) -> str:
    if not text:
        return ""

    # 1. Convert inline double dollar signs $$...$$ to single dollar sign $...$ if inline (no newlines)
    def dollar_replacer(match):
        content = match.group(1).strip()
        return f"${content}$"

    text = re.sub(r'\$\$\s*([^\$\n]+?)\s*\$\$', dollar_replacer, text)

    # 2. Convert Big-O notation into LaTeX \mathcal{O}(...) or O(...)
    def big_o_replacer(match):
        inner = match.group(1).strip()
        inner_latex = re.sub(r'\blog\b', r'\\log', inner)
        inner_latex = re.sub(r'\b(\d+)\^(\d+)\b', r'\1^{\2}', inner_latex)
        inner_latex = inner_latex.replace(' * ', r' \cdot ')
        return f"$\\mathcal{{O}}({inner_latex})$"

    text = re.sub(r'(?<![\$\w`])O\(([^)\n]+)\)(?![\$\w`])', big_o_replacer, text)

    # 3. Convert backticked constraints/math expressions into inline LaTeX $...$
    def backtick_math_replacer(match):
        raw = match.group(1).strip()

        # Do NOT convert code parameter assignments or array literals
        if any(raw.startswith(prefix) for prefix in ["nums =", "root =", "s =", "equations =", "arr =", "mat =", "grid =", "head ="]):
            return match.group(0)
        
        # Do NOT convert pure array literals like `[0,1]`, `[1,2]`, `[]`, `[1]`
        if raw.startswith("[") and raw.endswith("]") and not any(k in raw for k in ['<=', '>=', '!=', '^']):
            return match.group(0)

        has_math_op = any(op in raw for op in ['<=', '>=', '!=', '^', ' == ', ' + ', ' - ', ' * ', ' / '])
        has_power = bool(re.search(r'\b(?:\d+|[a-zA-Z])\^\d+\b', raw))
        is_range_bounds = bool(re.search(r'\[-?\d+\^?\d*,\s*-?\d+\^?\d*', raw))

        if not (has_math_op or has_power or is_range_bounds):
            return match.group(0)

        latex = raw
        latex = latex.replace('<=', r'\le ').replace('>=', r'\ge ').replace('!=', r'\neq ')
        latex = re.sub(r'(\d+|\b[a-zA-Z])\^(-?\d+)\b', r'\1^{\2}', latex)
        
        def var_dot_replacer(v_match):
            v_name = v_match.group(0)
            return f"\\text{{{v_name}}}"

        latex = re.sub(r'\b[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*\b', var_dot_replacer, latex)
        latex = re.sub(r'\s+', ' ', latex).strip()

        return f"${latex}$"

    text = re.sub(r'`([^`\n]+)`', backtick_math_replacer, text)

    # 4. Convert plain powers outside backticks/dollars: 10^5 -> $10^5$, 2^31 -> $2^{31}$
    def plain_power_replacer(match):
        base = match.group(1)
        exp = match.group(2)
        return f"${base}^{{{exp}}}$"

    text = re.sub(r'(?<![\$\w`])(\d+)\^(-?\d+)(?![\$\w`])', plain_power_replacer, text)

    # 5. Convert ordinal index expressions: i^th -> $i^{\text{th}}$
    text = re.sub(r'\b([a-zA-Z])\^th\b', r'$\1^{\\text{th}}$', text)

    return text

def convert_full_markdown(text: str) -> str:
    if not text:
        return ""
    # Protect fenced code blocks ``` ... ```
    parts = re.split(r'(```[a-zA-Z]*\n.*?```)', text, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith('```'):
            parts[i] = convert_prose_to_latex(parts[i])
    return "".join(parts)

def process_package_latex(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    
    if not ref_dir.is_dir():
        return fid, slug, False, False

    desc_file = ref_dir / "description.md"
    desc_processed = False
    if desc_file.is_file():
        old_desc = desc_file.read_text(encoding="utf-8")
        new_desc = convert_full_markdown(old_desc)
        if new_desc != old_desc:
            desc_file.write_text(new_desc, encoding="utf-8")
            desc_processed = True

    ed_file = ref_dir / "editorial.md"
    ed_processed = False
    if ed_file.is_file():
        old_ed = ed_file.read_text(encoding="utf-8")
        new_ed = convert_full_markdown(old_ed)
        if new_ed != old_ed:
            ed_file.write_text(new_ed, encoding="utf-8")
            ed_processed = True

    return fid, slug, desc_processed, ed_processed

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]
    
    total = len(questions)
    print(f"Applying LaTeX formatting to description.md and editorial.md for {total} problems...")
    start_time = time.time()
    
    desc_updated = 0
    ed_updated = 0
    completed = 0
    
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(process_package_latex, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, d_up, e_up = future.result()
            completed += 1
            if d_up:
                desc_updated += 1
            if e_up:
                ed_updated += 1
                
            if completed % 500 == 0 or completed == total:
                elapsed = time.time() - start_time
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Descriptions Updated: {desc_updated}, Editorials Updated: {ed_updated}")

    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total Descriptions formatted with LaTeX: {desc_updated}")
    print(f"Total Editorials formatted with LaTeX: {ed_updated}")

if __name__ == "__main__":
    main()
