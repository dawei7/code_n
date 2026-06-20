import os
import glob
import re
import time
import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY = os.environ.get("DEEPL_API_KEY", "")
API_URL = "https://api-free.deepl.com/v2/translate"

replacements = {
    # General terms from fix_german.py
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

    # Additional standard CS terms (as per user's best practice, "keep better more than less")
    r'\bPrioritätswarteschlange\b': r'Priority Queue',
    r'\bPrioritätswarteschlangen\b': r'Priority Queues',
    r'\bAdjazenzliste\b': r'Adjacency List',
    r'\bAdjazenzlisten\b': r'Adjacency Lists',
    r'\bAdjazenzmatrix\b': r'Adjacency Matrix',
    r'\bAdjazenzmatrizen\b': r'Adjacency Matrices',
    r'\bKantenliste\b': r'Edge List',
    r'\bKantenlisten\b': r'Edge Lists',
    r'\bVerkettete Liste\b': r'Linked List',
    r'\bVerketteten Liste\b': r'Linked List',
    r'\bVerkettete Listen\b': r'Linked Lists',
    r'\bVerketteten Listen\b': r'Linked Lists',
    r'\bdoppelt verkettete Liste\b': r'doubly linked List',
    r'\bDoppelt verkettete Liste\b': r'Doubly Linked List',
    r'\bdoppelt verketteten Liste\b': r'doubly linked List',
    r'\bDoppelt verketteten Liste\b': r'Doubly Linked List',
    r'\beinfach verkettete Liste\b': r'singly linked List',
    r'\bEinfach verkettete Liste\b': r'Singly Linked List',
    r'\beinfach verketteten Liste\b': r'singly linked List',
    r'\bEinfach verketteten Liste\b': r'Singly Linked List',
    r'\bHashtabelle\b': r'Hash Table',
    r'\bHashtabellen\b': r'Hash Tables',
    r'\bHash-Tabelle\b': r'Hash Table',
    r'\bHash-Tabellen\b': r'Hash Tables',
    r'\bBinärbaum\b': r'Binary Tree',
    r'\bBinärbäume\b': r'Binary Trees',
    r'\bbinäre Suchbaum\b': r'Binary Search Tree',
    r'\bbinären Suchbaum\b': r'Binary Search Tree',
    r'\bbinärer Suchbaum\b': r'Binary Search Tree',
    r'\bBinäre Suchbäume\b': r'Binary Search Trees',
    r'\bbinären Suchbäumen\b': r'Binary Search Trees',
    r'\bSegmentbaum\b': r'Segment Tree',
    r'\bSegmentbäume\b': r'Segment Trees',
    r'\bFenwick-Baum\b': r'Fenwick Tree',
    r'\bFenwick-Bäume\b': r'Fenwick Trees',
    r'\bSpannbaum\b': r'Spanning Tree',
    r'\bSpannbäume\b': r'Spanning Trees',
    r'\bminimaler Spannbaum\b': r'Minimum Spanning Tree (MST)',
    r'\bMinimale Spannbäume\b': r'Minimum Spanning Trees (MSTs)',
    r'\bminimalen Spannbaum\b': r'Minimum Spanning Tree (MST)',
    r'\bminimalen Spannbäume\b': r'Minimum Spanning Trees (MSTs)',
    r'\bFlussnetzwerk\b': r'Flow Network',
    r'\bFlussnetzwerke\b': r'Flow Networks',
    r'\bmaximaler Fluss\b': r'maximum flow',
    r'\bMaximaler Fluss\b': r'Maximum Flow',
    r'\bmaximalen Fluss\b': r'maximum flow',
    r'\bMaximalen Fluss\b': r'Maximum Flow',
    r'\bminimaler Schnitt\b': r'minimum cut',
    r'\bMinimaler Schnitt\b': r'Minimum Cut',
    r'\bminimalen Schnitt\b': r'minimum cut',
    r'\bMinimalen Schnitt\b': r'Minimum Cut',
    r'\bbipartites Matching\b': r'bipartite Matching',
    r'\bBipartites Matching\b': r'Bipartite Matching',
    r'\bbipartiten Matching\b': r'bipartite Matching',
    r'\bBipartiten Matching\b': r'Bipartite Matching',
    r'\bTopologische Sortierung\b': r'Topological Sort',
    r'\btopologische Sortierung\b': r'topological sort',
    r'\bTopologische Sortierungen\b': r'Topological Sorts',
    r'\btopologische Sortierungen\b': r'topological sorts',
    r'\bKürzester Pfad\b': r'Shortest Path',
    r'\bkürzester Pfad\b': r'shortest path',
    r'\bKürzeste Pfade\b': r'Shortest Paths',
    r'\bkürzeste Pfade\b': r'shortest paths',
    r'\bkürzesten Pfad\b': r'shortest path',
    r'\bkürzesten Pfaden\b': r'shortest paths',
}

def extract_placeholders(text):
    placeholders = []
    
    # 1. Code blocks: ```...```
    def replacer_code(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'```.*?```', replacer_code, text, flags=re.DOTALL)
    
    # 2. Inline code: `...`
    def replacer_inline_code(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'`[^`]+`', replacer_inline_code, text)
    
    # 3. Math blocks: $$...$$
    def replacer_math_block(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'\$\$[^\$]+\$\$', replacer_math_block, text, flags=re.DOTALL)
    
    # 4. Math inline: $...$
    def replacer_math_inline(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'\$[^\$]+\$', replacer_math_inline, text)
    
    # 5. HTML tags: <...> (Fix: avoid matching inequalities like <= by requiring a word character after <)
    def replacer_html(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'</?[a-zA-Z][^>]*>', replacer_html, text)
    
    # 6. Markdown link/image URLs: ](...)
    def replacer_url(match):
        placeholders.append(match.group(1))
        return f']([[[PH_{len(placeholders)-1}]]])'
    text = re.sub(r'\]\(([^)]+)\)', replacer_url, text)
    
    return text, placeholders

def restore_placeholders(text, placeholders):
    # 1. Fix spacing in markdown link placeholder brackets: ] ( [ [ [ PH_x ] ] ] ) -> ]([[[PH_x]]])
    text = re.sub(r'\]\s*\(\s*\[\s*\[\s*\[\s*(?:PH|ph)_(\d+)\s*\]\s*\]\s*\]\s*\)', r']([[[PH_\1]]])', text)
    
    # 2. General fix for spacing in placeholder brackets: [ [ [ PH_x ] ] ] -> [[[PH_x]]]
    text = re.sub(r'\[\s*\[\s*\[\s*(?:PH|ph)_(\d+)\s*\]\s*\]\s*\]', r'[[[PH_\1]]]', text)
    
    # 3. Restore all placeholders in order (checking both casing of 'ph'/'PH')
    for i, ph in enumerate(placeholders):
        text = text.replace(f'[[[PH_{i}]]]', ph)
        text = text.replace(f'[[[ph_{i}]]]', ph)
        
    return text

def translate_text(text, api_key=API_KEY):
    headers = {
        "Authorization": f"DeepL-Auth-Key {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": [text],
        "target_lang": "DE",
        "source_lang": "EN"
    }
    
    retries = 6
    backoff_time = 2.0
    for attempt in range(retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                data = response.json()
                return data["translations"][0]["text"]
            elif response.status_code == 456:
                raise Exception("DeepL API Quota Exceeded (HTTP 456).")
            elif response.status_code == 429:
                print(f"Rate limited (429). Retrying in {backoff_time:.1f}s...")
                time.sleep(backoff_time)
                backoff_time *= 2.5
                continue
            else:
                raise Exception(f"HTTP Error {response.status_code}: {response.text}")
        except Exception as e:
            if "Quota Exceeded" in str(e):
                raise e
            if attempt == retries - 1:
                raise e
            time.sleep(2 + attempt * 2)

def process_file(filepath):
    try:
        time.sleep(0.1)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # 1. Extract placeholders
        protected_text, placeholders = extract_placeholders(text)
        
        # 2. Translate via DeepL
        translated_text = translate_text(protected_text)
        
        # 3. Restore placeholders
        final_text = restore_placeholders(translated_text, placeholders)
        
        # 4. Post-processing replacements
        for pattern, replacement in replacements.items():
            final_text = re.sub(pattern, replacement, final_text)
            
        final_text = final_text.replace("| Zeit | Raum |", "| Zeit | Platz |")
        final_text = final_text.replace("| Zeit | Speicherplatz |", "| Zeit | Platz |")
        
        return final_text, None
    except Exception as e:
        return None, str(e)

def main():
    if not API_KEY:
        print("ERROR: DEEPL_API_KEY environment variable is not set. Please set it before running this script.")
        sys.exit(1)
        
    start_time = time.time()
    
    eng_files = [f for f in glob.glob('docs/algorithms/**/*.md', recursive=True) 
                 if not f.endswith('_de.md') and 'README' not in f and '_template' not in f]
    
    # Standard DeepL mode: skip existing files (allows resuming when key has quota again)
    files_to_process = []
    for file in eng_files:
        target_file = file[:-3] + '_de.md'
        if not os.path.exists(target_file):
            files_to_process.append(file)
                
    total_to_translate = len(files_to_process)
    if total_to_translate == 0:
        print("All files already translated!")
        return
        
    print(f"Translating {total_to_translate} remaining files in parallel (2 workers)...")
    
    success_count = 0
    failure_count = 0
    quota_exceeded = False
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_to_file = {}
        for file in files_to_process:
            future = executor.submit(process_file, file)
            future_to_file[future] = (file, file[:-3] + '_de.md')
            
        processed = 0
        for future in as_completed(future_to_file):
            file, target_file = future_to_file[future]
            processed += 1
            try:
                translated_content, err = future.result()
                if err:
                    print(f"[{processed}/{total_to_translate}] Failed: {file} - Error: {err}")
                    failure_count += 1
                    if "Quota Exceeded" in err:
                        quota_exceeded = True
                        print("Stopping translation due to Quota Exceeded error.")
                        executor.shutdown(wait=False, cancel_futures=True)
                        break
                else:
                    with open(target_file, 'w', encoding='utf-8') as f:
                        f.write(translated_content)
                    success_count += 1
                    print(f"[{processed}/{total_to_translate}] Success: {file}")
            except Exception as exc:
                print(f"[{processed}/{total_to_translate}] Generated an exception: {file} - {exc}")
                failure_count += 1
                if "Quota Exceeded" in str(exc):
                    quota_exceeded = True
                    print("Stopping translation due to Quota Exceeded error.")
                    executor.shutdown(wait=False, cancel_futures=True)
                    break
                    
    print("\n--- Summary ---")
    print(f"Total processed files: {success_count + failure_count}")
    print(f"Successful translations: {success_count}")
    print(f"Failed translations: {failure_count}")
    print(f"Total time elapsed: {time.time() - start_time:.2f} seconds")
    
    if quota_exceeded:
        print("\n[WARNING] Translation did not complete because the DeepL Free API limit (500k characters) was reached.")

if __name__ == "__main__":
    main()
