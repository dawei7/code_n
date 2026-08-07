import json
import re
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

def merge_contract_and_add_examples_header(desc_text: str, contract_text: str = None) -> str:
    if not desc_text or "An official LeetCode description is not available for this problem" in desc_text:
        return desc_text

    text = desc_text

    # Extract contract content if contract_text is available
    contract_snippet = ""
    if contract_text and contract_text.strip():
        c_body = contract_text.strip()
        c_body = re.sub(r'^#+\s*Function Contract\s*', '', c_body).strip()
        if c_body:
            contract_snippet = f"### Function Contract\n\n{c_body}\n\n"

    # Ensure ### Examples parent header exists before Example 1
    has_examples_parent = bool(re.search(r'^\s*#+\s*Examples\s*$', text, flags=re.MULTILINE | re.IGNORECASE))

    if not has_examples_parent and re.search(r'^\s*#+\s*Example\s*1\b', text, flags=re.MULTILINE | re.IGNORECASE):
        text = re.sub(r'^(\s*#+\s*Example\s*1\b)', r'### Examples\n\n\1', text, count=1, flags=re.MULTILINE | re.IGNORECASE)

    # Standardize individual examples to #### Example N under ### Examples
    def example_subheading_replacer(match):
        ex_num = match.group(1)
        return f"#### Example {ex_num}"

    text = re.sub(r'^\s*#+\s*Example\s*(\d+):?', example_subheading_replacer, text, flags=re.MULTILINE | re.IGNORECASE)

    # Position contract_snippet in front of ### Examples (or #### Example 1 or ### Constraints)
    if contract_snippet:
        # Remove any pre-existing Function Contract block in text to avoid duplication
        text = re.sub(r'### Function Contract\n.*?(?=### |\Z)', '', text, flags=re.DOTALL)

        if re.search(r'^\s*### Examples\b', text, flags=re.MULTILINE):
            text = re.sub(r'^(\s*### Examples\b)', lambda m: f"{contract_snippet}{m.group(1)}", text, count=1, flags=re.MULTILINE)
        elif re.search(r'^\s*#### Example\s*1\b', text, flags=re.MULTILINE):
            text = re.sub(r'^(\s*#### Example\s*1\b)', lambda m: f"{contract_snippet}### Examples\n\n{m.group(1)}", text, count=1, flags=re.MULTILINE)
        elif re.search(r'^\s*### Constraints\b', text, flags=re.MULTILINE):
            text = re.sub(r'^(\s*### Constraints\b)', lambda m: f"{contract_snippet}{m.group(1)}", text, count=1, flags=re.MULTILINE)
        else:
            text = f"{text}\n\n{contract_snippet}"

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

    desc_file = ref_dir / "description.md"
    contract_file = ref_dir / "contract.md"

    if not desc_file.is_file():
        return fid, slug, False, False

    desc_text = desc_file.read_text(encoding="utf-8")
    contract_text = contract_file.read_text(encoding="utf-8") if contract_file.is_file() else None

    new_desc = merge_contract_and_add_examples_header(desc_text, contract_text)

    contract_merged = bool(contract_text and "### Function Contract" in new_desc)
    
    if new_desc != desc_text:
        desc_file.write_text(new_desc, encoding="utf-8")
        return fid, slug, True, contract_merged

    return fid, slug, False, contract_merged

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]

    total = len(questions)
    print(f"Merging contract.md and adding Examples header across {total} problems...")
    start_time = time.time()

    desc_updated = 0
    contracts_merged = 0
    completed = 0

    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(process_package, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, d_up, c_merged = future.result()
            completed += 1
            if d_up:
                desc_updated += 1
            if c_merged:
                contracts_merged += 1

            if completed % 500 == 0 or completed == total:
                elapsed = time.time() - start_time
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Descriptions Updated: {desc_updated}, Contracts Merged: {contracts_merged}")

    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total Descriptions updated with Examples header & merged Contract: {desc_updated}")
    print(f"Total Contracts merged into description.md: {contracts_merged}")

if __name__ == "__main__":
    main()
