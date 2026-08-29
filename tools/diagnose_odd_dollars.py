import json
import re
from pathlib import Path

data = json.load(open('guided_example_errors.json', encoding='utf-8'))
print(f"Total error packages: {len(data)}")

for item in data:
    pkg = item['dir']
    p = Path('dsa/leetcode') / pkg / 'guided_example.md'
    if not p.exists():
        continue
    text = p.read_text(encoding='utf-8')
    lines = text.split('\n')
    
    in_code = False
    in_display_math = False
    
    for i, line in enumerate(lines):
        line_num = i + 1
        trimmed = line.trim() if hasattr(line, 'trim') else line.strip()
        if trimmed.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
            
        if trimmed == '$$':
            in_display_math = not in_display_math
            continue
        if in_display_math:
            continue
            
        # Strip backticks
        clean = re.sub(r'`[^`\n]+?`', '', line)
        # Strip single line $$...$$
        clean = re.sub(r'\$\$[^\$\n]+?\$\$', '', clean)
        
        # Count dollars
        dollars = re.findall(r'(?<!\\)\$', clean)
        if len(dollars) % 2 != 0:
            print(f"{pkg}:{line_num} -> {line.strip()[:120]}")
