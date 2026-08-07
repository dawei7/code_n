import json
import re
import html
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

def convert_prose_to_refined_latex(text: str) -> str:
    if not text:
        return ""

    def dollar_replacer(match):
        content = match.group(1).strip()
        return f"${content}$"

    text = re.sub(r'\$\$\s*([^\$\n]+?)\s*\$\$', dollar_replacer, text)

    def big_o_replacer(match):
        inner = match.group(1).strip()
        inner_latex = re.sub(r'\blog\b', r'\\log', inner)
        inner_latex = re.sub(r'\b(\d+)\^(\d+)\b', r'\1^{\2}', inner_latex)
        inner_latex = inner_latex.replace(' * ', r' \cdot ')
        return f"$\\mathcal{{O}}({inner_latex})$"

    text = re.sub(r'(?<![\$\w`])O\(([^)\n]+)\)(?![\$\w`])', big_o_replacer, text)

    def backtick_math_replacer(match):
        raw = match.group(1).strip()

        if any(raw.startswith(prefix) for prefix in [
            "equations = [[", "nums = [", "root = [", "s = \"", "grid = [[", "arr = ["
        ]):
            return match.group(0)

        if raw in ["double", "int", "void", "true", "false", "null", "String", "boolean", "float", "char"]:
            return match.group(0)

        if raw.startswith("[") and raw.endswith("]") and not any(k in raw for k in ['<=', '>=', '!=', '^', '_i', '_j', '_k']):
            return match.group(0)

        has_subscript = bool(re.search(r'\b[a-zA-Z0-9]+_[a-zA-Z0-9]+\b', raw))
        has_indexing = bool(re.search(r'\b[a-zA-Z0-9_]+\s*\[[a-zA-Z0-9_]+\]', raw))
        has_math_op = any(op in raw for op in ['<=', '>=', '!=', '^', ' == ', ' + ', ' - ', ' * ', ' / ', ' = '])
        has_power = bool(re.search(r'\b(?:\d+|[a-zA-Z])\^\d+\b', raw))
        is_range_bounds = bool(re.search(r'\[-?\d+\^?\d*,\s*-?\d+\^?\d*', raw))

        if not (has_subscript or has_indexing or has_math_op or has_power or is_range_bounds):
            return match.group(0)

        latex = raw
        latex = latex.replace('<=', r'\le ').replace('>=', r'\ge ').replace('!=', r'\neq ')
        latex = re.sub(r'(\d+|\b[a-zA-Z])\^(-?\d+)\b', r'\1^{\2}', latex)

        def sub_var_replacer(s_match):
            base = s_match.group(1)
            sub = s_match.group(2)
            if len(base) > 1:
                return f"\\text{{{base}}}_{{{sub}}}"
            return f"{base}_{{{sub}}}"

        latex = re.sub(r'\b([a-zA-Z0-9]+)_([a-zA-Z0-9]+)\b', sub_var_replacer, latex)

        def arr_index_replacer(a_match):
            arr_name = a_match.group(1)
            idx = a_match.group(2)
            if len(arr_name) > 1:
                return f"\\text{{{arr_name}}}[{idx}]"
            return f"{arr_name}[{idx}]"

        latex = re.sub(r'\b([a-zA-Z0-9_]+)\[([a-zA-Z0-9_]+)\]', arr_index_replacer, latex)

        def var_dot_replacer(v_match):
            v_name = v_match.group(0)
            v_name_clean = v_name.replace('_', r'\_')
            return f"\\text{{{v_name_clean}}}"

        latex = re.sub(r'\b[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*\b', var_dot_replacer, latex)
        latex = re.sub(r'\s*==\s*', ' = ', latex)
        latex = re.sub(r'\s+', ' ', latex).strip()

        return f"${latex}$"

    text = re.sub(r'`([^`\n]+)`', backtick_math_replacer, text)

    def math_block_refiner(match):
        content = match.group(1)
        def text_replacer(t_match):
            inner = t_match.group(1)
            inner_clean = inner.replace('_', r'\_')
            return f"\\text{{{inner_clean}}}"

        content = re.sub(r'\\text\{([^}]+)\}', text_replacer, content)
        content = re.sub(r'\s*==\s*', ' = ', content)
        content = re.sub(r'(?<!\\)%', r'\%', content)
        content = re.sub(r'(?<!\\)&(?!amp;|lt;|gt;|quot;|apos;)', r'\&', content)

        def arr_index_in_math(a_match):
            arr_name = a_match.group(1)
            idx = a_match.group(2)
            if len(arr_name) > 1 and not arr_name.startswith("\\text"):
                return f"\\text{{{arr_name}}}[{idx}]"
            return a_match.group(0)

        content = re.sub(r'\b([a-zA-Z0-9_]+)\[([a-zA-Z0-9_]+)\]', arr_index_in_math, content)
        return f"${content.strip()}$"

    text = re.sub(r'\$([^\$\n]+?)\$', math_block_refiner, text)

    def plain_power_replacer(match):
        base = match.group(1)
        exp = match.group(2)
        return f"${base}^{{{exp}}}$"

    text = re.sub(r'(?<![\$\w`])(\d+)\^(-?\d+)(?![\$\w`])', plain_power_replacer, text)
    text = re.sub(r'\b([a-zA-Z])\^th\b', r'$\1^{\\text{th}}$', text)

    return text

def build_clean_description(raw_md: str, contract_text: str = None) -> str:
    if not raw_md or "An official LeetCode description is not available for this problem" in raw_md:
        return "## Description\n\nAn official LeetCode description is not available for this problem.\n"

    text = raw_md
    text = html.unescape(text)
    text = text.replace("\xa0", " ").replace("&nbsp;", " ")

    lines = []
    for line in text.splitlines():
        cleaned_line = re.sub(r'^(?:\t|    )+(-\s*|\*\s*|\d+\.\s*)', r'\1', line)
        lines.append(cleaned_line)
    text = "\n".join(lines)

    def block_replacer(match):
        full_block = match.group(0)
        content = match.group(1).strip()

        if "Input:" in content or "Output:" in content:
            if '+---' in content or (content.count('|') > 2 and '\n|' in content):
                return full_block

            block_lines = content.splitlines()
            formatted_lines = []
            for bline in block_lines:
                bline = bline.strip()
                if not bline:
                    continue
                m_in = re.match(r'^(?:\*\*)?Input:\s*(?:\*\*)?\s*(.*)$', bline, re.IGNORECASE)
                m_out = re.match(r'^(?:\*\*)?Output:\s*(?:\*\*)?\s*(.*)$', bline, re.IGNORECASE)
                m_exp = re.match(r'^(?:\*\*)?Explanation:\s*(?:\*\*)?\s*(.*)$', bline, re.IGNORECASE)

                if m_in:
                    val = m_in.group(1).strip()
                    if not val.startswith('`') and not val.endswith('`'):
                        val = f"`{val}`"
                    formatted_lines.append(f"- **Input:** {val}")
                elif m_out:
                    val = m_out.group(1).strip()
                    if not val.startswith('`') and not val.endswith('`'):
                        val = f"`{val}`"
                    formatted_lines.append(f"- **Output:** {val}")
                elif m_exp:
                    val = m_exp.group(1).strip()
                    formatted_lines.append(f"- **Explanation:** {val}")
                else:
                    formatted_lines.append(bline)
            return "\n" + "\n".join(formatted_lines) + "\n"

        return full_block

    text = re.sub(r'```[a-zA-Z]*\n(.*?\n?)```', block_replacer, text, flags=re.DOTALL)

    text = re.sub(r'<font\b[^>]*>(.*?)</font>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<span\b[^>]*>(.*?)</span>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</?(?:font|span)\b[^>]*>', '', text, flags=re.IGNORECASE)

    text = re.sub(r'`+([^`\n]+)`+', r'`\1`', text)

    # Standardize section headings: Example 1, Constraints, Follow-up
    text = re.sub(r'^\s*(?:\*\*|#+)\s*Constraints:?\*\*', r'### Constraints', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^\s*(?:\*\*|#+)\s*Follow-up:?\*\*', r'### Follow-up', text, flags=re.MULTILINE | re.IGNORECASE)

    # Standardize individual sub-examples to #### Example N
    text = re.sub(r'^\s*(?:\*\*|#+)\s*Example\s*(\d+):?\*\*', r'#### Example \1', text, flags=re.MULTILINE | re.IGNORECASE)

    # Extract contract content if contract_text is available
    contract_snippet = ""
    if contract_text and contract_text.strip():
        c_body = contract_text.strip()
        c_body = re.sub(r'^#+\s*Function Contract\s*', '', c_body).strip()
        if c_body:
            contract_snippet = f"### Function Contract\n\n{c_body}\n\n"

    # Ensure ### Examples parent header exists before Example 1
    has_examples_parent = bool(re.search(r'^\s*#+\s*Examples\s*$', text, flags=re.MULTILINE | re.IGNORECASE))
    if not has_examples_parent and re.search(r'^\s*####\s*Example\s*1\b', text, flags=re.MULTILINE | re.IGNORECASE):
        text = re.sub(r'^(\s*####\s*Example\s*1\b)', r'### Examples\n\n\1', text, count=1, flags=re.MULTILINE | re.IGNORECASE)

    # Position contract_snippet in front of ### Examples (or #### Example 1 or ### Constraints)
    if contract_snippet:
        text = re.sub(r'### Function Contract\n.*?(?=### |#### |\Z)', '', text, flags=re.DOTALL)
        if re.search(r'^\s*### Examples\b', text, flags=re.MULTILINE):
            text = re.sub(r'^(\s*### Examples\b)', lambda m: f"{contract_snippet}{m.group(1)}", text, count=1, flags=re.MULTILINE)
        elif re.search(r'^\s*#### Example\s*1\b', text, flags=re.MULTILINE):
            text = re.sub(r'^(\s*#### Example\s*1\b)', lambda m: f"{contract_snippet}### Examples\n\n{m.group(1)}", text, count=1, flags=re.MULTILINE)
        elif re.search(r'^\s*### Constraints\b', text, flags=re.MULTILINE):
            text = re.sub(r'^(\s*### Constraints\b)', lambda m: f"{contract_snippet}{m.group(1)}", text, count=1, flags=re.MULTILINE)
        else:
            text = f"{text}\n\n{contract_snippet}"

    parts = re.split(r'(```[a-zA-Z]*\n.*?```)', text, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith('```'):
            parts[i] = convert_prose_to_refined_latex(parts[i])
    text = "".join(parts)

    lines = [line.rstrip() for line in text.splitlines()]
    result = "\n".join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result).strip()

    if not result.startswith("## Description"):
        result = re.sub(r'^#+\s*Description\s*', '', result).strip()
        result = f"## Description\n\n{result}"

    return result

def build_clean_editorial(raw_md: str) -> str:
    if not raw_md or "An official LeetCode editorial is not available for this problem" in raw_md:
        return "# Editorial\n\nAn official LeetCode editorial is not available for this problem.\n"

    text = raw_md
    text = html.unescape(text)
    text = text.replace("\xa0", " ").replace("&nbsp;", " ")

    lines = []
    for line in text.splitlines():
        cleaned_line = re.sub(r'^(?:\t|    )+(-\s*|\*\s*|\d+\.\s*)', r'\1', line)
        lines.append(cleaned_line)
    text = "\n".join(lines)

    text = re.sub(r'<font\b[^>]*>(.*?)</font>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<span\b[^>]*>(.*?)</span>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</?(?:font|span)\b[^>]*>', '', text, flags=re.IGNORECASE)

    parts = re.split(r'(```[a-zA-Z]*\n.*?```)', text, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith('```'):
            parts[i] = convert_prose_to_refined_latex(parts[i])
    text = "".join(parts)

    lines = [line.rstrip() for line in text.splitlines()]
    result = "\n".join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result).strip()

    if text.count('```') % 2 != 0:
        result += "\n```"

    return result

def process_package(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    raw_dir = ref_dir / "raw"

    if not raw_dir.is_dir():
        return fid, slug, False, False

    raw_desc_file = raw_dir / "raw_description.md"
    raw_contract_file = raw_dir / "raw_contract.md"
    clean_desc_file = ref_dir / "description.md"

    desc_processed = False
    if raw_desc_file.is_file():
        raw_text = raw_desc_file.read_text(encoding="utf-8")
        contract_text = raw_contract_file.read_text(encoding="utf-8") if raw_contract_file.is_file() else None
        clean_text = build_clean_description(raw_text, contract_text)
        clean_desc_file.write_text(clean_text, encoding="utf-8")
        desc_processed = True

    raw_ed_file = raw_dir / "raw_editorial.md"
    clean_ed_file = ref_dir / "editorial.md"
    ed_processed = False
    if raw_ed_file.is_file():
        raw_text = raw_ed_file.read_text(encoding="utf-8")
        clean_text = build_clean_editorial(raw_text)
        clean_ed_file.write_text(clean_text, encoding="utf-8")
        ed_processed = True

    return fid, slug, desc_processed, ed_processed

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]

    total = len(questions)
    print(f"Rebuilding robust clean description.md and editorial.md for {total} problems...")
    start_time = time.time()

    desc_count = 0
    ed_count = 0
    completed = 0

    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(process_package, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, d_proc, e_proc = future.result()
            completed += 1
            if d_proc:
                desc_count += 1
            if e_proc:
                ed_count += 1

            if completed % 500 == 0 or completed == total:
                elapsed = time.time() - start_time
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Clean Descriptions: {desc_count}, Clean Editorials: {ed_count}")

    elapsed = time.time() - start_time
    print(f"\nFINISHED! Rebuilt {total} problems in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()
