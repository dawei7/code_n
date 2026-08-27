"""Clean and normalize all Euler Markdown and LaTeX documentation.

1. Unescapes HTML entities (&amp;, &lt;, &gt;, &quot;, &#39;, etc.)
2. Normalizes align -> aligned in math blocks for KaTeX compatibility
3. Ensures reference/description.md starts with '## Description'
"""
from __future__ import annotations

import html
import re
from pathlib import Path

EULER_ROOT = Path("dsa/euler")


def clean_markdown_text(text: str) -> str:
    # 1. Unescape HTML entities
    cleaned = html.unescape(text)

    # 2. Fix KaTeX align environment within $$ ... $$ -> aligned
    # Replace \begin{align} with \begin{aligned} and \end{align} with \end{aligned}
    cleaned = re.sub(r'\\begin\{align\*?\}', r'\\begin{aligned}', cleaned)
    cleaned = re.sub(r'\\end\{align\*?\}', r'\\end{aligned}', cleaned)

    return cleaned


def normalize_description_heading(text: str) -> str:
    # If the file starts with '# ...' or '### ...' replace with '## Description'
    lines = text.splitlines()
    if not lines:
        return "## Description\n"
    
    first_non_empty = 0
    while first_non_empty < len(lines) and not lines[first_non_empty].strip():
        first_non_empty += 1

    if first_non_empty < len(lines):
        line = lines[first_non_empty].strip()
        if line.startswith("#"):
            lines[first_non_empty] = "## Description"
        else:
            lines.insert(first_non_empty, "## Description\n")
    else:
        lines = ["## Description", ""]

    return "\n".join(lines) + "\n"


def process_package(pkg_dir: Path) -> int:
    modified = 0

    # 1. reference/description.md
    desc_file = pkg_dir / "reference" / "description.md"
    if desc_file.is_file():
        raw = desc_file.read_text(encoding="utf-8")
        cleaned = clean_markdown_text(raw)
        cleaned = normalize_description_heading(cleaned)
        if cleaned != raw:
            desc_file.write_text(cleaned, encoding="utf-8")
            modified += 1

    # 2. other reference files
    ref_dir = pkg_dir / "reference"
    if ref_dir.is_dir():
        for rf in ref_dir.glob("*.md"):
            if rf.name == "description.md":
                continue
            raw = rf.read_text(encoding="utf-8")
            cleaned = clean_markdown_text(raw)
            if cleaned != raw:
                rf.write_text(cleaned, encoding="utf-8")
                modified += 1

    # 3. doc.md
    doc_file = pkg_dir / "doc.md"
    if doc_file.is_file():
        raw = doc_file.read_text(encoding="utf-8")
        cleaned = clean_markdown_text(raw)
        if cleaned != raw:
            doc_file.write_text(cleaned, encoding="utf-8")
            modified += 1

    # 4. variants/optimal/approach.md
    app_file = pkg_dir / "variants" / "optimal" / "approach.md"
    if app_file.is_file():
        raw = app_file.read_text(encoding="utf-8")
        cleaned = clean_markdown_text(raw)
        if cleaned != raw:
            app_file.write_text(cleaned, encoding="utf-8")
            modified += 1

    return modified


def main() -> None:
    total_packages = 0
    total_modified_files = 0
    packages_changed = 0

    for pkg_dir in sorted(EULER_ROOT.iterdir()):
        if not pkg_dir.is_dir() or not pkg_dir.name[:4].isdigit():
            continue
        total_packages += 1
        count = process_package(pkg_dir)
        if count > 0:
            packages_changed += 1
            total_modified_files += count

    print(f"Scanned {total_packages} Euler packages.")
    print(f"Normalized {total_modified_files} files across {packages_changed} packages.")


if __name__ == "__main__":
    main()
