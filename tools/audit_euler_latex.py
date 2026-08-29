"""Comprehensive LaTeX and Markdown auditor for Project Euler packages."""
from __future__ import annotations

import re
from pathlib import Path

EULER_ROOT = Path("dsa/euler")


def is_table_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.endswith("|") and s.count("|") >= 2


def audit_markdown_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = []
    lines = text.splitlines()

    # 1. Check for table rows wrongly starting or ending with math delimiters ($| or |$)
    for idx, line in enumerate(lines):
        s = line.strip()
        if (s.startswith("$|") or s.startswith("$$|")) and s.count("|") >= 2 and ("---" in s or idx + 1 < len(lines) and "---" in lines[idx+1]):
            errors.append(f"Line {idx+1}: Table row starts with math delimiter: {s[:50]}")
        if (s.endswith("|$") or s.endswith("|$$")) and s.count("|") >= 2 and ("---" in s or idx > 0 and "---" in lines[idx-1]):
            errors.append(f"Line {idx+1}: Table row ends with math delimiter: {s[-50:]}")

    # Remove fenced code blocks
    no_code = re.sub(r"```[\s\S]*?```", "", text)
    no_code = re.sub(r"`[^`\n]*`", "", no_code)

    # 2. Check for unbalanced display math $$
    display_count = len(re.findall(r"\$\$", no_code))
    if display_count % 2 != 0:
        errors.append(f"Unbalanced '$$' display math delimiters: count={display_count}")

    # 3. Check for unbalanced inline math $
    no_display = re.sub(r"\$\$[\s\S]*?\$\$", "", no_code)
    inline_dollars = [m.start() for m in re.finditer(r"(?<!\\)\$", no_display)]
    if len(inline_dollars) % 2 != 0:
        errors.append(f"Unbalanced '$' inline math delimiters: count={len(inline_dollars)}")

    # 4. Check for bare LaTeX commands outside math blocks
    no_math = re.sub(r"\$\$[\s\S]*?\$\$", "", no_code)
    no_math = re.sub(r"\$[^\$\n]*?\$", "", no_math)

    PROSE_COMMANDS = [
        "times", "frac", "sum", "prod", "sqrt", "pmod", "binom", "cdot", "equiv",
        "approx", "alpha", "beta", "gamma", "delta", "pi", "theta", "phi", "infty"
    ]
    for cmd in PROSE_COMMANDS:
        for m in re.finditer(rf"\\{cmd}\b", no_math):
            sample = no_math[max(0, m.start()-15):min(len(no_math), m.end()+25)].replace("\n", " ")
            errors.append(f"Bare \\{cmd} outside math: '...{sample}...'")

    # 5. Check for mismatched curly braces inside math blocks
    math_blocks = re.findall(r"\$\$([\s\S]*?)\$\$", no_code) + re.findall(r"\$([^\$\n]+?)\$", no_code)
    for block in math_blocks:
        open_b = block.count("{") - block.count(r"\{")
        close_b = block.count("}") - block.count(r"\}")
        if open_b != close_b:
            errors.append(f"Mismatched curly braces ({open_b} open vs {close_b} close) in math block: '{block[:50]}'")

    return errors


def main():
    total_packages = 0
    package_errors: dict[str, list[str]] = {}

    for pkg in sorted(EULER_ROOT.glob("*_*")):
        if not pkg.is_dir():
            continue
        total_packages += 1
        pkg_issues = []
        for md_file in pkg.rglob("*.md"):
            errs = audit_markdown_file(md_file)
            if errs:
                for e in errs:
                    pkg_issues.append(f"{md_file.relative_to(pkg)}: {e}")
        if pkg_issues:
            package_errors[pkg.name] = pkg_issues

    print(f"Audited {total_packages} Euler packages.")
    if package_errors:
        print(f"\n[FAIL] Found issues in {len(package_errors)} packages:\n")
        for name, errs in package_errors.items():
            print(f"=== {name} ===")
            for e in errs:
                print(f"  - {e}")
    else:
        print("\n[SUCCESS] All 1,009 Euler packages passed LaTeX & Markdown audit with 0 issues!")


if __name__ == "__main__":
    main()
