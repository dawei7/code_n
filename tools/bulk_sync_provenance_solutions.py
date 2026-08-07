import json
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

DOOCS_ROOT = REPO_ROOT / "temp_doocs" / "solution"
KAMYU_ROOT = REPO_ROOT / "temp_kamyu104"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

# Build map of doocs folders by frontend_id
doocs_map = {}
if DOOCS_ROOT.is_dir():
    for range_dir in DOOCS_ROOT.iterdir():
        if range_dir.is_dir():
            for q_dir in range_dir.iterdir():
                if q_dir.is_dir():
                    # Name format is e.g. "0001.Two Sum" or "0001.Two%20Sum" or "0001.two-sum"
                    prefix = q_dir.name.split(".")[0]
                    if prefix.isdigit():
                        fid = int(prefix)
                        doocs_map[fid] = q_dir

# Build map of kamyu104 files by slug and language
kamyu_python_map = {}
kamyu_sql_map = {}
kamyu_sh_map = {}
kamyu_js_map = {}

if (KAMYU_ROOT / "Python").is_dir():
    for f in (KAMYU_ROOT / "Python").glob("*.py"):
        kamyu_python_map[f.stem] = f

if (KAMYU_ROOT / "MySQL").is_dir():
    for f in (KAMYU_ROOT / "MySQL").glob("*.sql"):
        kamyu_sql_map[f.stem] = f

if (KAMYU_ROOT / "Shell").is_dir():
    for f in (KAMYU_ROOT / "Shell").glob("*.sh"):
        kamyu_sh_map[f.stem] = f

if (KAMYU_ROOT / "JavaScript").is_dir():
    for f in (KAMYU_ROOT / "JavaScript").glob("*.js"):
        kamyu_js_map[f.stem] = f


def py2_to_py3(code: str) -> str:
    # Convert Python 2 syntax to Python 3
    code = re.sub(r"\bclass\s+Solution\(object\):", "class Solution:", code)
    code = re.sub(r"\bxrange\b", "range", code)
    code = re.sub(r"\b(\w+)\.iteritems\(\)", r"\1.items()", code)
    code = re.sub(r"\b(\w+)\.itervalues\(\)", r"\1.values()", code)
    code = re.sub(r"\b(\w+)\.iterkeys\(\)", r"\1.keys()", code)
    code = re.sub(r"\bsys\.maxint\b", "sys.maxsize", code)
    # Print statement to function if needed
    code = re.sub(r"^(\s*)print\s+([^(#\n].*)$", r"\1print(\2)", code, flags=re.MULTILINE)
    return code


optimal_synced = 0
competitive_synced = 0

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    pkg_dir = LEETCODE_ROOT / folder_name
    if not pkg_dir.is_dir():
        continue

    meta_path = pkg_dir / "metadata.json"
    primary_lang = "python"
    if meta_path.is_file():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            primary_lang = meta.get("primary_language", "python")
        except Exception:
            pass

    optimal_dir = pkg_dir / "variants" / "optimal"
    competitive_dir = pkg_dir / "variants" / "competitive"

    optimal_dir.mkdir(parents=True, exist_ok=True)
    competitive_dir.mkdir(parents=True, exist_ok=True)

    # 1. Sync Optimal Solution from doocs/leetcode
    if fid in doocs_map:
        doocs_q_dir = doocs_map[fid]
        # Look for Solution.py, Solution.sql, Solution.sh, Solution.ts/js
        target_file = None
        if primary_lang == "python" and (doocs_q_dir / "Solution.py").is_file():
            target_file = doocs_q_dir / "Solution.py"
            dst = optimal_dir / "solution.py"
        elif primary_lang == "sql" and (doocs_q_dir / "Solution.sql").is_file():
            target_file = doocs_q_dir / "Solution.sql"
            dst = optimal_dir / "solution.sql"
        elif primary_lang == "bash" and (doocs_q_dir / "Solution.sh").is_file():
            target_file = doocs_q_dir / "Solution.sh"
            dst = optimal_dir / "solution.sh"
        elif primary_lang in {"javascript", "typescript"} and (doocs_q_dir / "Solution.js").is_file():
            target_file = doocs_q_dir / "Solution.js"
            dst = optimal_dir / "solution.js"
        elif (doocs_q_dir / "Solution.py").is_file():
            target_file = doocs_q_dir / "Solution.py"
            dst = optimal_dir / "solution.py"

        if target_file:
            content = target_file.read_text(encoding="utf-8", errors="ignore")
            if dst.suffix == ".py":
                content = py2_to_py3(content)
            dst.write_text(content, encoding="utf-8")
            optimal_synced += 1

    # 2. Sync Competitive Solution from kamyu104/LeetCode-Solutions
    kamyu_file = None
    dst_comp = None
    if primary_lang == "python" and slug in kamyu_python_map:
        kamyu_file = kamyu_python_map[slug]
        dst_comp = competitive_dir / "solution.py"
    elif primary_lang == "sql" and slug in kamyu_sql_map:
        kamyu_file = kamyu_sql_map[slug]
        dst_comp = competitive_dir / "solution.sql"
    elif primary_lang == "bash" and slug in kamyu_sh_map:
        kamyu_file = kamyu_sh_map[slug]
        dst_comp = competitive_dir / "solution.sh"
    elif primary_lang == "javascript" and slug in kamyu_js_map:
        kamyu_file = kamyu_js_map[slug]
        dst_comp = competitive_dir / "solution.js"
    elif slug in kamyu_python_map:
        kamyu_file = kamyu_python_map[slug]
        dst_comp = competitive_dir / "solution.py"

    if kamyu_file and dst_comp:
        content = kamyu_file.read_text(encoding="utf-8", errors="ignore")
        if dst_comp.suffix == ".py":
            content = py2_to_py3(content)
        dst_comp.write_text(content, encoding="utf-8")
        competitive_synced += 1

print(f"Optimal solutions synced from doocs/leetcode: {optimal_synced}")
print(f"Competitive solutions synced from kamyu104/LeetCode-Solutions: {competitive_synced}")
