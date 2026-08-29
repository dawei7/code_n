import os
import re
import glob
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")

def clean_bullets(content: str) -> str:
    lines = content.split("\n")
    fixed_lines = []
    
    for line in lines:
        if line.strip().startswith("- **- **") or line.strip().startswith("- ** - **"):
            last_bullet_idx = line.rfind("- **")
            if last_bullet_idx > 0:
                line = line[last_bullet_idx:]
        
        m = re.match(r"^(\s*-\s*\*\*)(.*?)\:\s*(.*?)\:\*\*\s*\2\:\s*(.*)$", line)
        if m:
            line = f"{m.group(1)}{m.group(2)}:** {m.group(4)}"
            
        fixed_lines.append(line)
        
    return "\n".join(fixed_lines)


def clean_broken_tables(content: str) -> str:
    step2_table_pattern = re.compile(
        r"(\|\s*Parameter\s*\|\s*Current Observed Sub-state\s*\|\s*Transition Decision\s*\|\s*Updated State\s*\|\s*\n"
        r"\|\s*---\s*\|\s*---\s*\|\s*---\s*\|\s*---\s*\|\s*\n)"
        r"\|\s*Intermediate State\s*\|\s*Subproblem evaluation\s*\|[\s\S]*?\|\s*Invariant satisfied\s*\|\s*\n"
        r"(\|\s*Candidate Set\s*\|\s*Active candidates\s*\|\s*Prune non-optimal paths\s*\|\s*Monotone progress\s*\|)",
        re.MULTILINE
    )
    
    replacement = (
        r"\1"
        r"| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |\n"
        r"\2"
    )
    
    content = step2_table_pattern.sub(replacement, content)
    
    lines = content.split("\n")
    cleaned_lines = []
    
    for line in lines:
        if line.strip().startswith("|") and line.strip().endswith("|"):
            line = re.sub(r"\$\$(.*?)\$\$", r"$\1$", line)
        cleaned_lines.append(line)
            
    return "\n".join(cleaned_lines)


def clean_latex_glitches(content: str) -> str:
    # 1. Strip zero-width spaces \u200B and \uFEFF
    content = content.replace("\u200b", "").replace("\u200B", "").replace("\ufeff", "")
    
    # 2. Fix asymmetric dollars
    content = re.sub(r"\$\$([a-zA-Z0-9_\{\}\^\\]+?)\$", r"$\1$", content)
    content = re.sub(r"(?<!\$)\$([a-zA-Z0-9_\{\}\^\\]+?)\$\$(?!\$)", r"$\1$", content)
    
    # 3. Fix unescaped underscores in \texttt{foo_bar} in math
    def fix_texttt(m):
        inner = m.group(1).replace("_", r"\_")
        return r"\texttt{" + inner + "}"
    content = re.sub(r"\\texttt\{([a-zA-Z0-9_]+)\}", fix_texttt, content)
    
    # 4. Fix specific known KaTeX syntax errors
    content = content.replace(r"\@cdots", r"\cdots")
    content = content.replace(r"\maxFrequency", r"\text{maxFrequency}")
    content = content.replace(r"\qu...", r"\quad\dots")
    
    return content


def process_all_markdown_files():
    all_files = sorted(list(LEETCODE_ROOT.glob("*/guided_example.md")) +
                       list(LEETCODE_ROOT.glob("*/approach.md")) +
                       list(LEETCODE_ROOT.glob("*/reference/*.md")) +
                       list(LEETCODE_ROOT.glob("*/doc.md")))
    
    print(f"Processing {len(all_files)} markdown documentation files...")
    
    modified_count = 0
    for file_path in all_files:
        original = file_path.read_text(encoding="utf-8")
        updated = original
        
        if file_path.name == "guided_example.md":
            updated = clean_broken_tables(updated)
            updated = clean_bullets(updated)
            
        updated = clean_latex_glitches(updated)
        
        if updated != original:
            file_path.write_text(updated, encoding="utf-8")
            modified_count += 1
            
    print(f"Completed cleanup: Modified {modified_count} files.")


if __name__ == "__main__":
    process_all_markdown_files()
