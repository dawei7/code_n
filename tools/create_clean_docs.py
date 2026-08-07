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

def clean_description(raw_md: str) -> str:
    if not raw_md or "An official LeetCode description is not available for this problem" in raw_md:
        return "## Description\n\nAn official LeetCode description is not available for this problem.\n"

    text = raw_md

    # 1. Unescape HTML entities
    text = html.unescape(text)
    text = text.replace("\xa0", " ").replace("&nbsp;", " ")

    # 2. Fix tab-indented lists (remove leading tabs/spaces before bullet points to prevent code block rendering)
    lines = []
    for line in text.splitlines():
        cleaned_line = re.sub(r'^(?:\t|    )+(-\s*|\*\s*|\d+\.\s*)', r'\1', line)
        lines.append(cleaned_line)
    text = "\n".join(lines)

    # 3. Unwrap Example Input/Output blocks out of fenced code blocks ``` ... ```
    def unwrap_example_block(match):
        block_content = match.group(1).strip()
        # If it contains ASCII table borders like '+---+', leave code block intact
        if '+---' in block_content or '|' in block_content:
            return match.group(0)

        block_lines = block_content.splitlines()
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

    # Match ``` ... ``` blocks containing Input:
    text = re.sub(r'```[a-zA-Z]*\n(.*?Input:.*?)```', unwrap_example_block, text, flags=re.DOTALL | re.IGNORECASE)

    # 4. Remove redundant/broken HTML style tags like <font...>, <span>...</span>
    text = re.sub(r'<font\b[^>]*>(.*?)</font>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<span\b[^>]*>(.*?)</span>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</?(?:font|span)\b[^>]*>', '', text, flags=re.IGNORECASE)

    # 5. Clean up redundant backticks
    text = re.sub(r'`+([^`\n]+)`+', r'`\1`', text)

    # 6. Normalize headings
    text = re.sub(r'^\s*\*\*(Example\s*\d+):?\*\*', r'### \1', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^\s*\*\*Constraints:?\*\*', r'### Constraints', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^\s*\*\*Follow-up:?\*\*', r'### Follow-up', text, flags=re.MULTILINE | re.IGNORECASE)

    # Clean up excess whitespace
    lines = [line.rstrip() for line in text.splitlines()]
    result = "\n".join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result).strip()

    # Ensure ## Description header at top
    if not result.startswith("## Description"):
        result = re.sub(r'^#+\s*Description\s*', '', result).strip()
        result = f"## Description\n\n{result}"

    return result

def clean_editorial(raw_md: str) -> str:
    if not raw_md or "An official LeetCode editorial is not available for this problem" in raw_md:
        return "# Editorial\n\nAn official LeetCode editorial is not available for this problem.\n"

    text = raw_md

    # 1. Unescape HTML entities
    text = html.unescape(text)
    text = text.replace("\xa0", " ").replace("&nbsp;", " ")

    # 2. Remove leading tabs/spaces before bullet points
    lines = []
    for line in text.splitlines():
        cleaned_line = re.sub(r'^(?:\t|    )+(-\s*|\*\s*|\d+\.\s*)', r'\1', line)
        lines.append(cleaned_line)
    text = "\n".join(lines)

    # 3. Clean up HTML style tags
    text = re.sub(r'<font\b[^>]*>(.*?)</font>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<span\b[^>]*>(.*?)</span>', r'\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</?(?:font|span)\b[^>]*>', '', text, flags=re.IGNORECASE)

    # Clean up excess whitespace
    lines = [line.rstrip() for line in text.splitlines()]
    result = "\n".join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result).strip()

    return result

def process_package(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    
    if not ref_dir.is_dir():
        return fid, slug, False, False

    raw_desc_file = ref_dir / "raw_description.md"
    clean_desc_file = ref_dir / "description.md"
    desc_processed = False
    if raw_desc_file.is_file():
        raw_text = raw_desc_file.read_text(encoding="utf-8")
        clean_text = clean_description(raw_text)
        clean_desc_file.write_text(clean_text, encoding="utf-8")
        desc_processed = True

    raw_ed_file = ref_dir / "raw_editorial.md"
    clean_ed_file = ref_dir / "editorial.md"
    ed_processed = False
    if raw_ed_file.is_file():
        raw_text = raw_ed_file.read_text(encoding="utf-8")
        clean_text = clean_editorial(raw_text)
        clean_ed_file.write_text(clean_text, encoding="utf-8")
        ed_processed = True

    return fid, slug, desc_processed, ed_processed

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]
    
    total = len(questions)
    print(f"Creating clean description.md and editorial.md for {total} problems...")
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
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()
