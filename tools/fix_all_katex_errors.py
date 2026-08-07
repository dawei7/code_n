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

def fix_katex_in_prose(text: str) -> str:
    if not text:
        return ""

    # Helper to clean individual $...$ or $$...$$ math content
    def clean_math_content(math_str: str) -> str:
        # 1. Escape underscores inside \text{...}
        def text_replacer(match):
            inner = match.group(1)
            inner_escaped = inner.replace('_', r'\_')
            return f"\\text{{{inner_escaped}}}"

        res = re.sub(r'\\text\{([^}]+)\}', text_replacer, math_str)

        # 2. Replace == with = in math mode
        res = re.sub(r'\s*==\s*', ' = ', res)

        # 3. Escape reserved characters % and & in math mode (when not part of HTML entity like &lt;)
        res = re.sub(r'(?<!\\)%', r'\%', res)
        res = re.sub(r'(?<!\\)&(?!amp;|lt;|gt;|quot;|apos;)', r'\&', res)

        # 4. Fix multi-character subscript identifiers without braces (e.g. $A_i_j$ -> $A_{i\_j}$)
        def multi_subscript_replacer(match):
            base = match.group(1)
            sub = match.group(2)
            sub_clean = sub.replace('_', r'\_')
            return f"{base}_{{{sub_clean}}}"
            
        res = re.sub(r'([a-zA-Z0-9]+)_([a-zA-Z0-9_]{2,})', multi_subscript_replacer, res)

        # 5. Clean extra inner whitespace
        res = res.strip()
        return res

    # Replace inline math $...$
    def inline_math_replacer(match):
        inner = match.group(1)
        cleaned = clean_math_content(inner)
        return f"${cleaned}$"

    # Replace block math $$...$$
    def block_math_replacer(match):
        inner = match.group(1)
        cleaned = clean_math_content(inner)
        return f"$${cleaned}$$"

    # Process block math first, then inline math
    text = re.sub(r'\$\$\s*([^\$]+?)\s*\$\$', block_math_replacer, text)
    text = re.sub(r'\$([^\$\n]+?)\$', inline_math_replacer, text)

    return text

def fix_file_katex(file_path: Path) -> bool:
    if not file_path.is_file():
        return False

    old_content = file_path.read_text(encoding="utf-8")
    if not old_content or "An official LeetCode description is not available for this problem" in old_content:
        return False

    # Protect fenced code blocks ``` ... ```
    parts = re.split(r'(```[a-zA-Z]*\n.*?```)', old_content, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith('```'):
            parts[i] = fix_katex_in_prose(parts[i])

    new_content = "".join(parts)
    if new_content != old_content:
        file_path.write_text(new_content, encoding="utf-8")
        return True
    return False

def process_package(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"

    d_updated = fix_file_katex(ref_dir / "description.md")
    e_updated = fix_file_katex(ref_dir / "editorial.md")

    return fid, slug, d_updated, e_updated

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]

    total = len(questions)
    print(f"Auditing and fixing KaTeX math errors across {total} problems...")
    start_time = time.time()

    desc_fixed = 0
    ed_fixed = 0
    completed = 0

    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(process_question_katex, q) if 'process_question_katex' in globals() else executor.submit(process_package, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, d_up, e_up = future.result()
            completed += 1
            if d_up:
                desc_fixed += 1
            if e_up:
                ed_fixed += 1

            if completed % 500 == 0 or completed == total:
                elapsed = time.time() - start_time
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Descriptions Fixed: {desc_fixed}, Editorials Fixed: {ed_fixed}")

    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total Descriptions fixed for KaTeX: {desc_fixed}")
    print(f"Total Editorials fixed for KaTeX: {ed_fixed}")

if __name__ == "__main__":
    main()
