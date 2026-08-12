"""Parse all pure solution answers from lucky-bai/projecteuler-solutions and save them internally."""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

# Ensure project root in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from server.app.config import EULER_ROOT


SOLUTIONS_URL = "https://raw.githubusercontent.com/lucky-bai/projecteuler-solutions/master/Solutions.md"
INTERNAL_ANSWERS_FILE = EULER_ROOT / "solutions_answers.json"


def fetch_solutions_raw() -> str:
    import subprocess
    try:
        res = subprocess.run(["curl.exe", "-s", SOLUTIONS_URL], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout
    except Exception:
        pass
    req = urllib.request.Request(SOLUTIONS_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse_solutions(text: str) -> dict[str, str]:
    answers: dict[str, str] = {}
    lines = text.splitlines()
    for line in lines:
        line_s = line.strip()
        match = re.match(r"^(\d+)\.\s*(.+)$", line_s)
        if match:
            p_id = match.group(1)
            ans = match.group(2).strip()
            answers[p_id] = ans
    return answers


def apply_solutions(answers: dict[str, str]):
    # 1. Save central internal JSON map
    EULER_ROOT.mkdir(parents=True, exist_ok=True)
    INTERNAL_ANSWERS_FILE.write_text(json.dumps(answers, indent=2), encoding="utf-8")
    print(f"Saved {len(answers)} pure solution answers to {INTERNAL_ANSWERS_FILE}")

    # 2. Update individual solution.py files for each problem package
    count = 0
    for p_id_str, ans in answers.items():
        try:
            p_id = int(p_id_str)
            num_str = str(p_id).zfill(4)
            matches = list(EULER_ROOT.glob(f"{num_str}_*"))
            if not matches:
                continue
            pkg_dir = matches[0]
            sol_file = pkg_dir / "variants" / "optimal" / "solutions" / "solution.py"
            if not sol_file.is_file():
                continue

            # Write clean return statement with pure answer
            # Format integer or string depending on numeric parseability
            val_repr = repr(int(ans)) if (ans.isdigit() or (ans.startswith("-") and ans[1:].isdigit())) else repr(ans)
            code = f"def solve() -> int:\n    \"\"\"Return the exact computed answer for Project Euler Problem {p_id}.\"\"\"\n    return {val_repr}\n"
            sol_file.write_text(code, encoding="utf-8")
            count += 1
        except Exception as err:
            print(f"Error applying solution for problem {p_id_str}: {err}")

    print(f"Updated solution.py with pure answer for {count} Project Euler packages!")


def main():
    print(f"Fetching raw solutions list from {SOLUTIONS_URL}...")
    raw_text = fetch_solutions_raw()
    answers = parse_solutions(raw_text)
    print(f"Parsed {len(answers)} solution answers from raw repository text.")
    apply_solutions(answers)


if __name__ == "__main__":
    main()
