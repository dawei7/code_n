import json
import re
from pathlib import Path

repo_root = Path('.')
leetcode_dir = repo_root / 'dsa' / 'leetcode'

packages = sorted([
    p for p in leetcode_dir.iterdir()
    if p.is_dir() and not p.name.startswith(('_', '.'))
])

print(f"Auditing all {len(packages)} canonical problem packages...")

violations = {
    "example_block_html": [],
    "unspaced_headings": [],
    "generic_n_contracts": [],
    "disallowed_html_tags": [],
}

allowed_tags = {
    'img', 'br', 'sub', 'sup', 'table', 'thead', 'tbody', 'tr', 'td', 'th',
    'a', 'details', 'summary', 'span', 'b', 'i', 'strong', 'em', 'code', 'kbd',
    'svg', 'path', 'circle', 'rect', 'line', 'polygon', 'polyline', 'text', 'g'
}

for pkg in packages:
    doc_files = []
    if (pkg / 'doc.md').exists():
        doc_files.append(pkg / 'doc.md')
    if (pkg / 'reference').exists():
        doc_files.extend(list((pkg / 'reference').glob('*.md')))
        
    for df in doc_files:
        try:
            text = df.read_text(encoding='utf-8')
        except Exception as e:
            violations["disallowed_html_tags"].append((str(df), [f"Read error: {e}"]))
            continue
            
        rel_path = str(df.relative_to(repo_root))
        
        # 1. Check for example-block html
        if 'example-block' in text:
            violations["example_block_html"].append(rel_path)
            
        # 2. Check for unspaced headings (heading attached to previous line without blank line)
        if re.search(r'[^\n]\n#{1,6}\s+[^\n]+', text):
            violations["unspaced_headings"].append(rel_path)
            
        # 3. Check for generic '- `n`: Input parameter.'
        if "- `n`: Input parameter." in text:
            violations["generic_n_contracts"].append(rel_path)
            
        # Strip code blocks and LaTeX math before searching for raw HTML tags
        clean_for_tags = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        clean_for_tags = re.sub(r'`[^`]*`', '', clean_for_tags)
        clean_for_tags = re.sub(r'\$\$.*?\$\$', '', clean_for_tags, flags=re.DOTALL)
        clean_for_tags = re.sub(r'\$[^\$]*\$', '', clean_for_tags)
        
        # Find HTML tags
        found_tags = re.findall(r'<([a-zA-Z][a-zA-Z0-9]*)[^>]*>', clean_for_tags)
        bad_tags = [t.lower() for t in found_tags if t.lower() not in allowed_tags]
        if bad_tags:
            violations["disallowed_html_tags"].append((rel_path, bad_tags[:3]))

print("\n" + "="*50)
print("REFERENCE DOCUMENTATION AUDIT RESULTS")
print("="*50)
print(f"1. example-block div tags:     {len(violations['example_block_html'])}")
print(f"2. Unspaced headings:          {len(violations['unspaced_headings'])}")
print(f"3. Generic '- n: Input' stubs: {len(violations['generic_n_contracts'])}")
print(f"4. Disallowed HTML tags:       {len(violations['disallowed_html_tags'])}")
print("="*50)

if violations['example_block_html']:
    print("\nSamples with example-block:", violations['example_block_html'][:5])
if violations['unspaced_headings']:
    print("\nSamples with unspaced headings:", violations['unspaced_headings'][:5])
if violations['generic_n_contracts']:
    print("\nSamples with generic contract:", violations['generic_n_contracts'][:5])
if violations['disallowed_html_tags']:
    print("\nSamples with disallowed HTML:", violations['disallowed_html_tags'][:5])
    
total_violations = sum(len(v) for v in violations.values())
if total_violations == 0:
    print("\nSUCCESS: All 4,005 reference documents passed audit with 0 violations!")
else:
    print(f"\nAUDIT INCOMPLETE: {total_violations} issues remaining.")
