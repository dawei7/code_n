import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

euler_dir = Path("dsa/euler")
fixed_count = 0

for pkg in sorted(euler_dir.glob("*_*")):
    if not pkg.is_dir():
        continue
    app_file = pkg / "approach.md"
    if not app_file.exists():
        continue
    text = app_file.read_text(encoding="utf-8")
    
    # 1. Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        # Single line $$ ... $$
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4:
            inner = stripped[2:-2].strip()
            if ("&" in inner or "\\\\" in inner) and "\\begin{" not in inner:
                if "\\text{if}" in inner or "\\text{for}" in inner or "\\text{when}" in inner:
                    inner = f"\\begin{{cases}}\n{inner}\n\\end{{cases}}"
                elif inner.startswith("&") or inner.count("&") > 2:
                    inner = f"\\begin{{matrix}}\n{inner}\n\\end{{matrix}}"
                else:
                    inner = f"\\begin{{aligned}}\n{inner}\n\\end{{aligned}}"
            new_lines.append("")
            new_lines.append("$$")
            new_lines.append(inner)
            new_lines.append("$$")
            new_lines.append("")
        elif stripped.startswith("$$") and len(stripped) > 2:
            inner = stripped[2:].strip()
            new_lines.append("")
            new_lines.append("$$")
            new_lines.append(inner)
        elif stripped.endswith("$$") and len(stripped) > 2 and not stripped.startswith("$$"):
            inner = stripped[:-2].strip()
            new_lines.append(inner)
            new_lines.append("$$")
            new_lines.append("")
        else:
            new_lines.append(line)
            
    formatted = "\n".join(new_lines)
    
    # 2. Check all $$ ... $$ blocks for missing environments
    def fix_block(match):
        content = match.group(1).strip()
        if ("&" in content or "\\\\" in content) and "\\begin{" not in content:
            if "\\text{if}" in content or "\\text{for}" in content or "\\text{when}" in content:
                return f"$$\n\\begin{{cases}}\n{content}\n\\end{{cases}}\n$$"
            elif content.strip().startswith("&") or content.count("&") >= content.count("\\\\") * 2:
                return f"$$\n\\begin{{matrix}}\n{content}\n\\end{{matrix}}\n$$"
            else:
                return f"$$\n\\begin{{aligned}}\n{content}\n\\end{{aligned}}\n$$"
        return f"$$\n{content}\n$$"

    fixed_text = re.sub(r"\$\$\s*(.*?)\s*\$\$", fix_block, formatted, flags=re.DOTALL)
    
    # Clean up excess blank lines around $$
    fixed_text = re.sub(r"\n{3,}\$\$", "\n\n$$", fixed_text)
    fixed_text = re.sub(r"\$\$\n{3,}", "$$\n\n", fixed_text)
    
    if fixed_text != text:
        app_file.write_text(fixed_text, encoding="utf-8")
        fixed_count += 1

print(f"Fixed {fixed_count} approach files.")
