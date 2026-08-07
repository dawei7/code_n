import json
import re
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

def convert_python2_to_python3(code: str) -> str:
    if not code:
        return ""

    # Replace xrange -> range
    code = re.sub(r'\bxrange\b', 'range', code)
    # Replace sys.maxint -> sys.maxsize
    code = re.sub(r'\bsys\.maxint\b', 'sys.maxsize', code)
    # Replace basestring -> str
    code = re.sub(r'\bbasestring\b', 'str', code)
    # Replace unicode -> str
    code = re.sub(r'\bunicode\b', 'str', code)
    # Replace .iteritems() -> .items()
    code = re.sub(r'\.iteritems\(\)', '.items()', code)
    # Replace .itervalues() -> .values()
    code = re.sub(r'\.itervalues\(\)', '.values()', code)
    # Replace .iterkeys() -> .keys()
    code = re.sub(r'\.iterkeys\(\)', '.keys()', code)

    # Convert print statements without parentheses: print "hello" -> print("hello")
    def print_replacer(match):
        arg = match.group(1).strip()
        if arg.startswith('(') and arg.endswith(')'):
            return f"print{arg}"
        return f"print({arg})"

    code = re.sub(r'^\s*print\s+([^\n;]+)', print_replacer, code, flags=re.MULTILINE)

    return code

def process_package(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    pkg_dir = LEETCODE_ROOT / folder_name

    if not pkg_dir.is_dir():
        return fid, slug, 0, 0

    renamed_count = 0
    py3_converted_count = 0

    variants_dir = pkg_dir / "variants"
    if variants_dir.is_dir():
        for variant_folder in variants_dir.iterdir():
            if not variant_folder.is_dir():
                continue
            solutions_dir = variant_folder / "solutions"
            if not solutions_dir.is_dir():
                continue

            # Look for existing solution files
            files = list(solutions_dir.iterdir())
            for f in files:
                if f.is_dir() or f.name.startswith("candidate"):
                    continue

                stem = f.stem.lower()
                ext = f.suffix.lower()

                # Determine standard solution target name
                target_name = None
                if ext == ".py":
                    target_name = "solution.py"
                elif ext == ".js":
                    target_name = "solution.js"
                elif ext == ".sql":
                    target_name = "solution.sql"
                elif ext == ".sh":
                    target_name = "solution.sh"

                if target_name:
                    target_file = solutions_dir / target_name
                    if f.name != target_name:
                        content = f.read_text(encoding="utf-8")
                        if ext == ".py":
                            new_content = convert_python2_to_python3(content)
                            if new_content != content:
                                py3_converted_count += 1
                            target_file.write_text(new_content, encoding="utf-8")
                        else:
                            target_file.write_text(content, encoding="utf-8")
                        
                        f.unlink()  # Remove legacy file (leetcode.py, leetcode_sqlite.sql, etc.)
                        renamed_count += 1
                    else:
                        # Existing solution.<ext> - ensure Python 3 compatibility
                        if ext == ".py":
                            content = f.read_text(encoding="utf-8")
                            new_content = convert_python2_to_python3(content)
                            if new_content != content:
                                py3_converted_count += 1
                                f.write_text(new_content, encoding="utf-8")

    return fid, slug, renamed_count, py3_converted_count

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]

    total = len(questions)
    print(f"Migrating solutions to solution.* and converting Python 2 to Python 3 for {total} problems...")
    start_time = time.time()

    total_renamed = 0
    total_py3 = 0
    completed = 0

    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(process_package, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, r_cnt, p_cnt = future.result()
            completed += 1
            total_renamed += r_cnt
            total_py3 += p_cnt

            if completed % 500 == 0 or completed == total:
                elapsed = time.time() - start_time
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Renamed: {total_renamed}, Python 3 Fixes: {total_py3}")

    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total solution files renamed to solution.*: {total_renamed}")
    print(f"Total Python 2 to Python 3 syntax conversions: {total_py3}")

if __name__ == "__main__":
    main()
