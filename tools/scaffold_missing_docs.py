import sys, os, glob, re
sys.path.insert(0, 'c:/dawei7/code_n')
from challenges.registry import CHALLENGE_REGISTRY

def doc_family(category):
    return 'neetcode' if category.startswith('neetcode_') else 'geeksforgeeks'

TEMPLATE_PATH = 'c:/dawei7/code_n/docs/_template.md'
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

# Get existing docs
docs = glob.glob('c:/dawei7/code_n/docs/algorithms/**/*.md', recursive=True)
doc_ids = set()
for d in docs:
    basename = os.path.basename(d)
    if basename.startswith('_'): continue
    parts = basename.split('_')
    if len(parts) >= 2:
        doc_ids.add(f'{parts[0]}_{parts[1]}')

# Iterate over registry
created = 0
for ch_id, cls in CHALLENGE_REGISTRY.items():
    if ch_id in doc_ids:
        continue

    # Instantiate to get info
    c = cls()
    info = c.info
    
    # Format complexity
    complexity = info.required_complexity.value if hasattr(info.required_complexity, 'value') else str(info.required_complexity)
    
    # Create slug
    slug = re.sub(r'[^a-z0-9]+', '-', info.name.lower()).strip('-')
    filename = f"{ch_id}_{slug}.md"
    
    # Create source-family/category directory
    cat_dir = f"c:/dawei7/code_n/docs/algorithms/{doc_family(info.category)}/{info.category}"
    os.makedirs(cat_dir, exist_ok=True)
    
    # Inject data into template
    content = template.replace('{Algorithm Name}', info.name)
    content = content.replace('{challenge_id}', info.id)
    content = content.replace('{category}', info.category)
    content = content.replace('{complexity}', complexity)
    content = content.replace('{d}', str(info.difficulty))
    content = content.replace('{r}', str(max(1, info.difficulty))) # default relevance
    
    # Simple placeholder for problem statement
    desc = info.description.replace('\n', ' ').strip()
    problem_statement = f"{desc}\n\n**Input:** `n` (size of input)\n**Output:** The solution to the problem."
    content = content.replace('{1-2 paragraphs: state the problem the algorithm solves, the input and\noutput, and a concrete example with sample input and output.}', problem_statement)
    
    # Write file
    file_path = os.path.join(cat_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    created += 1
    
print(f"Scaffolded {created} missing reference documents!")
