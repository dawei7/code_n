import os
import glob
import re

replacements = {
    r'\b(h|H)allo\b': r'\1i', # hi pointer
    r'\b(d|D)rücken\b': r'\1ush', # push
    r'\b(d|D)rückt\b': r'\1usht', # pushes
    r'\b(g|G)edrückt\b': r'\1epusht', # pushed
    r'\bRundgang\b': r'Schritt-für-Schritt-Durchlauf', # Walk-through
    r'\bWarteschlange\b': r'Queue',
    r'\bWarteschlangen\b': r'Queues',
    r'\bStapel\b': r'Stack',
    r'\bStapeln\b': r'Stacks',
    r'\| Raum \|': r'| Platz |', # Space in tables
    r'\bRaumkomplexität\b': r'Platzkomplexität',
    r'\bAm besten\b': r'Bester Fall',
    r'\bAm schlimmsten\b': r'Schlechtester Fall',
    r'\bDurchschnitt\b': r'Durchschnittlicher Fall', # in complexity table
    r'\bBinärdatei\b': r'Binär',
    r'\bZeichenfolge\b': r'String',
    r'\bZeichenfolgen\b': r'Strings',
    r'\bgucken\b': r'peek',
    r'\bSpähen\b': r'peek',
    r'\bÜberweisen\b': r'Umschichten', # transferring elements
    r'\büberweisen\b': r'umschichten',
    r'\bübertragen\b': r'umschichten',
    r'\bÜbertragen\b': r'Umschichten',
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for pattern, replacement in replacements.items():
        # Only replace outside of code blocks to be safe?
        # Actually our translated markdown has no translated code blocks since we protected them.
        # But we can just run regex on the whole text.
        content = re.sub(pattern, replacement, content)

    # special fix for the complexity table headers which might be messed up
    content = content.replace("| Zeit | Raum |", "| Zeit | Platz |")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

md_files = glob.glob('docs/**/*_de.md', recursive=True)
count = 0
for file in md_files:
    if process_file(file):
        count += 1

print(f"Fixed {count} files.")
