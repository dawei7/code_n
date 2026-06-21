import os
import glob
import re
import time
import requests
import sys
import argparse

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODELS_POOL = ["gemini-3.5-flash", "gemini-3.1-flash-lite", "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3-flash-preview"]
current_model_idx = 0

def call_gemini(prompt):
    global current_model_idx
    headers = {
        "Content-Type": "application/json"
    }
    
    retries = 5
    backoff = 5.0
    
    while True:
        model = MODELS_POOL[current_model_idx]
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.1
            }
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                data = response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            elif response.status_code == 429:
                resp_text = response.text
                is_daily_limit = True
                try:
                    data = response.json()
                    violations = data.get("error", {}).get("details", [])
                    quota_violations = []
                    for detail in violations:
                        if detail.get("@type") == "type.googleapis.com/google.rpc.QuotaFailure":
                            quota_violations.extend(detail.get("violations", []))
                    
                    if quota_violations:
                        is_daily = False
                        is_minute = False
                        for v in quota_violations:
                            quota_id = v.get("quotaId", "").lower()
                            if "day" in quota_id or "daily" in quota_id:
                                is_daily = True
                            if "minute" in quota_id:
                                is_minute = True
                        if is_minute and not is_daily:
                            is_daily_limit = False
                        else:
                            is_daily_limit = is_daily
                except Exception:
                    pass

                if is_daily_limit and ("RESOURCE_EXHAUSTED" in resp_text or "quota" in resp_text.lower()):
                    if current_model_idx < len(MODELS_POOL) - 1:
                        old_model = MODELS_POOL[current_model_idx]
                        current_model_idx += 1
                        new_model = MODELS_POOL[current_model_idx]
                        print(f"Quota exhausted for {old_model}. Automatically falling back to {new_model}...")
                        time.sleep(2)
                        continue
                
                print(f"Rate limited (429) on {model}. Retrying in {backoff:.1f}s...")
                time.sleep(backoff)
                backoff *= 2.0
                continue
            else:
                raise Exception(f"HTTP Error {response.status_code}: {response.text}")
        except Exception as e:
            if "Quota Exceeded" in str(e):
                raise e
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(2)

def generate_translation_prompt(content):
    prompt = f"""You are a university-level computer science and mathematics professor who is a native speaker of both English and German.
Your task is to translate the following computer science and mathematics documentation from English to German.

Strict translation rules:
1. Maintain all markdown formatting, tables, headers, list structures, and HTML tags (e.g. details/summary tags) exactly.
2. Do NOT translate or modify any code blocks (e.g., ```python ... ```). Leave them completely identical and unchanged, including comments in them.
3. Do NOT translate inline code or variable names (e.g., `solve()`, `edges`, `cover`, `u`, `v`, `hi`, `lo`, `degrees`).
4. Do NOT translate LaTeX mathematical formulas (e.g., $O(V + E)$, $V$, $E$, $\\mathcal{{S}}$, etc.). Keep them exactly as they are.
5. Keep standard computer science nouns and terms in English (but apply German capitalization rules where appropriate):
   - Queue, Stack, Priority Queue, Deque, Linked List, Doubly Linked List
   - Hash Table, Hash Map, Binary Tree, Binary Search Tree, Segment Tree, Fenwick Tree
   - Adjacency List, Adjacency Matrix, Edge List, Flow Network
   - String, Pointer, Array
   - peek, push, pop
   (For example: "Wir fügen ein Element zur Queue hinzu" or "Der Stack ist leer.")
6. Use correct and precise German academic/scientific terminology for mathematical, logical, and graph theoretical concepts:
   - Vertex Cover -> Knotenbedeckung (Note: keep Vertex-Cover in headers or challenge titles for searchability/consistency, e.g. "# Vertex-Cover (2-Approximation)", but use "Knotenbedeckung" in descriptions)
   - Cycle / Cycles (in a graph) -> Zyklus / Zyklen
   - Connected component -> Zusammenhangskomponente
   - Loop invariant -> Schleifeninvariante
   - Recurrence relation -> Rekursionsgleichung / Rekurrenz
   - Proof by contradiction -> Beweis durch Widerspruch
   - Proof by induction -> Beweis durch vollständige Induktion (or Induktionsbeweis)
   - Base case (in induction) -> Induktionsanfang (or Basis)
   - Inductive step -> Induktionsschritt
   - Space complexity -> Platzkomplexität (never "Raumkomplexität")
   - Time complexity -> Zeitkomplexität
7. In complexity tables (e.g., Best/Average/Worst cases), translate:
   - "Best" -> "Bestfall" (or "Bester Fall")
   - "Average" -> "Durchschnittlicher Fall"
   - "Worst" -> "Schlechtester Fall"
8. Translate all other general descriptions, explanations, problem statements, real-world applications, and text outside of code/math elements into clear, professional, and natural scientific German.
9. Do not wrap the output in markdown code blocks (like ```markdown ... ```). Just output the raw translated markdown content.

Here is the English content to translate:
{content}
"""
    return prompt

def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prompt = generate_translation_prompt(content)
    translated_content = call_gemini(prompt)
    
    # Strip leading/trailing code fence wrapper if Gemini accidentally returns it
    if translated_content.startswith("```markdown"):
        translated_content = translated_content[11:]
        if translated_content.endswith("```"):
            translated_content = translated_content[:-3]
    elif translated_content.startswith("```"):
        translated_content = translated_content[3:]
        if translated_content.endswith("```"):
            translated_content = translated_content[:-3]
            
    return translated_content.strip()

def main():
    parser = argparse.ArgumentParser(description="Translate documentation from English to German using Gemini 3.1 Flash Lite API.")
    parser.add_argument("--target", choices=["algorithms", "mathematical", "all"], default="all",
                        help="Target directories to translate. Priority: algorithms, then mathematical.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing _de.md files.")
    parser.add_argument("--limit", type=int, default=0, help="Limit the number of files to translate (0 for no limit).")
    parser.add_argument("--model", default="gemini-3.1-flash-lite", help="Initial model to use for translation.")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: GEMINI_API_KEY environment variable is not set. Please set it before running this script.")
        sys.exit(1)

    # Reorder MODELS_POOL based on CLI input
    global MODELS_POOL, current_model_idx
    if args.model in MODELS_POOL:
        MODELS_POOL.remove(args.model)
    MODELS_POOL.insert(0, args.model)
    current_model_idx = 0

    start_time = time.time()

    # 1. Gather English source files based on target
    target_dirs = []
    if args.target == "algorithms":
        target_dirs = ["docs/algorithms"]
    elif args.target == "mathematical":
        target_dirs = ["docs/mathematical"]
    else:
        target_dirs = ["docs/algorithms", "docs/mathematical"]

    eng_files = []
    for d in target_dirs:
        files = glob.glob(f"{d}/**/*.md", recursive=True)
        # Filter out _de.md, README, and _template
        files = [f for f in files if not f.endswith("_de.md") and "README" not in f and "_template" not in f]
        eng_files.extend(files)

    print(f"Found {len(eng_files)} English files in targeted directories: {', '.join(target_dirs)}")

    # 2. Filter files that already have translated versions (unless overwrite is active)
    to_translate = []
    for file in eng_files:
        target_file = file[:-3] + '_de.md'
        if args.overwrite or not os.path.exists(target_file):
            to_translate.append((file, target_file))

    if args.limit > 0:
        to_translate = to_translate[:args.limit]

    total_to_translate = len(to_translate)
    print(f"Identified {total_to_translate} files that need translation.")

    if total_to_translate == 0:
        print("All target files are already translated! Nothing to do.")
        return

    success_count = 0
    failure_count = 0

    # Sequential translation with rate limit sleep (15 RPM -> 4.5 seconds delay)
    delay = 4.5

    for i, (source_file, target_file) in enumerate(to_translate):
        print(f"[{i+1}/{total_to_translate}] Translating: {source_file} -> {target_file}")
        try:
            translated_text = translate_file(source_file)
            
            # Ensure parent directory exists
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated_text)
                
            success_count += 1
            print(f"[{i+1}/{total_to_translate}] Success!")
            time.sleep(delay)
        except Exception as e:
            print(f"[{i+1}/{total_to_translate}] Failed: {e}")
            failure_count += 1
            # Back off slightly on failure
            time.sleep(10)

    print("\n--- Translation Summary ---")
    print(f"Total processed files: {success_count + failure_count}")
    print(f"Successful translations: {success_count}")
    print(f"Failed translations: {failure_count}")
    print(f"Total time elapsed: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
