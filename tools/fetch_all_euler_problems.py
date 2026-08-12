"""Fetch all Project Euler problem statements and build challenge packages under dsa/euler/."""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

# Ensure project root in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


from tools.import_euler import create_euler_package


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s).strip("-")
    return s or "problem"


def fetch_url_text(url: str) -> str:
    import subprocess
    cmd = ["curl.exe", "-s", url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout
    except Exception:
        pass
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def fetch_problems_index() -> list[dict[str, str]]:
    url = "https://projecteuler.net/minimal=problems"
    text = fetch_url_text(url)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    problems: list[dict[str, str]] = []
    for line in lines:
        if line.startswith("ID##") or not ("##" in line):
            continue
        parts = line.split("##")
        if len(parts) >= 4:
            p_id = parts[0].strip()
            title = parts[1].strip()
            published = parts[2].strip()
            solved_by = parts[3].strip()
            problems.append({
                "id": p_id,
                "title": title,
                "slug": slugify(title),
                "published": published,
                "solved_by": solved_by,
            })
    return problems


def fetch_problem_statement(problem_id: str) -> str:
    url = f"https://projecteuler.net/minimal={problem_id}"
    try:
        raw_html = fetch_url_text(url)
        # Clean basic HTML tags to readable markdown/text
        text = re.sub(r"<p\b[^>]*>", "", raw_html)
        text = re.sub(r"</p>", "\n\n", text)
        text = re.sub(r"<br\s*/?>", "\n", text)
        text = re.sub(r"<[^>]+>", "", text)
        return text.strip()
    except Exception as err:
        print(f"Error fetching statement for problem {problem_id}: {err}")
        return f"Project Euler Problem {problem_id}"



def main():
    print("Fetching Project Euler problems index from minimal=problems...")
    problems = fetch_problems_index()
    print(f"Found {len(problems)} problems in minimal=problems index.")

    limit = 1007  # Fetch all available problems
    if len(sys.argv) > 1:
        try:
            limit = int(sys.argv[1])
        except ValueError:
            pass

    problems_to_import = problems[:limit]
    print(f"Importing {len(problems_to_import)} problem packages...")

    count = 0
    for item in problems_to_import:
        p_id = item["id"]
        title = item["title"]
        slug = item["slug"]
        
        # Check if already imported
        num_str = str(p_id).zfill(4)
        existing = list(Path(REPO_ROOT / "dsa" / "euler").glob(f"{num_str}_*"))
        if existing and (existing[0] / "metadata.json").is_file() and p_id != "1":
            print(f"Skipping existing problem {p_id}: {existing[0].name}")
            continue

        statement = fetch_problem_statement(p_id)
        description = f"### {title}\n\n{statement}"
        
        create_euler_package(
            frontend_id=p_id,
            title=title,
            slug=slug,
            description=description,
            difficulty="Level 0 (5%)",
            euler_level=0,
            category="math",
        )
        count += 1
        time.sleep(0.1) # Gentle rate limiting

    print(f"Successfully imported {count} Project Euler problem packages!")


if __name__ == "__main__":
    main()
