import os
import re
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")

def fix_file_content(content: str, file_path: Path) -> str:
    # 1. Clean zero-width spaces
    content = content.replace("\u200b", "").replace("\u200B", "").replace("\ufeff", "")
    
    # 2. Fix x^\* -> x^*, a^\* -> a^*, b^\* -> b^*
    content = content.replace(r"^\*", r"^*")
    content = content.replace(r"\Theta(x^\*)", r"\Theta(x^*)")
    
    # 3. Fix \centernot -> \not, \@cdots -> \cdots
    content = content.replace(r"\centernot\implies", r"\not\implies")
    content = content.replace(r"\@cdots", r"\cdots")
    
    # 4. Fix unescaped underscores in \texttt{...}
    def fix_texttt(m):
        inner = m.group(1).replace("_", r"\_")
        return r"\texttt{" + inner + "}"
    content = re.sub(r"\\texttt\{([a-zA-Z0-9_]+)\}", fix_texttt, content)
    
    # 5. Fix code expressions inappropriately wrapped in $...$
    content = re.sub(r"\$(boxGrid\s*=\s*\[\[[\s\S]*?\]\])\$", r"`\1`", content)
    content = re.sub(r"\$(board\s*=\s*\[\[[\s\S]*?\]\])\$", r"`\1`", content)
    content = re.sub(r"\$(seats\s*=\s*\[\[[\s\S]*?\]\])\$", r"`\1`", content)
    content = re.sub(r"\$(grid\s*=\s*\[[\s\S]*?\])\$", r"`\1`", content)
    content = re.sub(r"\$(moves\s*=\s*\"[^\"]+?\")\$", r"`\1`", content)
    content = re.sub(r"\$(preorder\s*=\s*\"[^\"]+?\")\$", r"`\1`", content)
    content = re.sub(r"\$(input\s*=\s*\"[^\"]+?\")\$", r"`\1`", content)
    content = re.sub(r"\$(color\s*=\s*\"[^\"]+?\")\$", r"`\1`", content)
    content = re.sub(r"\$(start\s*=\s*\"[^\"]+?\",\s*target\s*=\s*\"[^\"]+?\")\$", r"`\1`", content)
    content = re.sub(r"\$(?:nums\s*=\s*)?(\[[0-9,\s_]+?\])\$", r"`nums = \1`", content)
    content = re.sub(r"\$\"(!?@#[\s\S]*?)\"\$(?:\$)?", r'`"\1"`', content)
    content = re.sub(r"\$(\['\\'[^\$]+?\])\$", r"`\1`", content)
    content = re.sub(r"\$\(?special offer #(\d+)\)?(.*?)\$", r"(special offer #\1)\2", content)
    content = re.sub(r"\$(c\s*=\s*'#')\$", r"`\1`", content)
    content = re.sub(r"\$\\text\{color\}\[0\]\s*=\s*'#'\$", r"`color[0] = '#'`", content)
    content = re.sub(r"\$\\text\{moves\}\[i\]\s*=\s*'\_'\$", r"`moves[i] = '_'`", content)
    content = re.sub(r"\$(\d+\s*\^\s*\d+\s*\^\s*[\d\s\^\=]+?)\$", r"`\1`", content)
    content = re.sub(r"\$([0-9\s\^\=]+?<u>\*\*[\d]+\*\*</u>[0-9\s\^\=]*?)\$", r"`\1`", content)
    content = re.sub(r"\$__init__\([\s\S]*?\)\$", r"`__init__(...)`", content)
    content = re.sub(r"\$!@#[\s\S]*?\$", r'`"!@#$%^&*()-+"`', content)
    
    # 6. Fix nested subscripts and stray underscores
    content = content.replace(r"a_{i}^b_{i}", r"a_{i}^{b_{i}}")
    content = content.replace(r"u^_i", r"u_i")
    content = content.replace(r"z_{1},_ z_{2}", r"z_{1}, z_{2}")
    content = content.replace(r"b_{1} <_ b_{2}", r"b_{1} < b_{2}")
    content = content.replace(r"(x_{i},_ y_{i})", r"(x_{i}, y_{i})")
    content = content.replace(r"s_{i}.length,_ t_{i}.length", r"s_{i}.\text{length}, t_{i}.\text{length}")
    content = content.replace(r"nums1_i_", r"nums1_i")
    content = content.replace(r"\text{customer\_id}", r"\text{customer\_id}")
    content = content.replace(r"\text{customer\\_id}", r"\text{customer\_id}")
    content = content.replace(r"exit_time[node]", r"exit\_time[node]")
    
    # 7. Asymmetric dollars
    content = re.sub(r"\$\$([a-zA-Z0-9_\{\}\^\\]+?)\$", r"$\1$", content)
    content = re.sub(r"(?<!\$)\$([a-zA-Z0-9_\{\}\^\\]+?)\$\$(?!\$)", r"$\1$", content)
    
    return content


def run():
    all_files = sorted(list(LEETCODE_ROOT.glob("*/guided_example.md")) +
                       list(LEETCODE_ROOT.glob("*/approach.md")) +
                       list(LEETCODE_ROOT.glob("*/reference/*.md")) +
                       list(LEETCODE_ROOT.glob("*/doc.md")))
    
    modified = 0
    for f in all_files:
        orig = f.read_text(encoding="utf-8")
        fixed = fix_file_content(orig, f)
        if fixed != orig:
            f.write_text(fixed, encoding="utf-8")
            modified += 1
            
    print(f"Fixed {modified} files.")

if __name__ == "__main__":
    run()
