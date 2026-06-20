import os
import glob
import re
import time
import requests
import sys

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = "gemini-3.1-flash-lite"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

def is_boilerplate(content):
    if "Let $\\mathcal{S}$ define the state space of the algorithm" in content:
        return True
    if "Let \\mathcal{S} define the state space of the algorithm" in content:
        return True
    if "Bellman formulation yields an optimal substructure" in content:
        return True
    return False

def call_gemini(prompt):
    headers = {
        "Content-Type": "application/json"
    }
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
            "temperature": 0.2
        }
    }
    
    retries = 5
    backoff = 5.0
    for attempt in range(retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                data = response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            elif response.status_code == 429:
                print(f"Rate limited (429). Retrying in {backoff:.1f}s...")
                time.sleep(backoff)
                backoff *= 2.0
                continue
            else:
                raise Exception(f"HTTP Error {response.status_code}: {response.text}")
        except Exception as e:
            if "Quota Exceeded" in str(e):
                raise e
            if attempt == retries - 1:
                raise e
            time.sleep(2 + attempt * 2)

def generate_math_spec(algo_name, category, algo_content):
    prompt = f"""You are a university-level computer science and mathematics professor. 
Your task is to write a mathematically rigorous, technically accurate, and pedagogical "Formal Mathematical Specification" for the following algorithm:

Algorithm Name: {algo_name}
Category: {category}

Here is the English description and implementation of the algorithm for context:
{algo_content}

Write a formal mathematical specification that strictly follows this structure:

# Formal Mathematical Specification: {algo_name}

## 1. Definitions and Notation
Provide a rigorous definition of the inputs, outputs, state space, and any mathematical domains or sets used in the algorithm using LaTeX (e.g., $V$ for vertices, $E$ for edges, state spaces $\\mathcal{{S}}$, etc.).

## 2. Algebraic Characterization [or Loop Invariants / Recurrence Relations / Graph Formulations]
Provide the formal mathematical equations, recurrence relations, invariants, or algebraic transitions that govern the algorithm's correctness. Be mathematically precise and use LaTeX for all formulas.

## 3. Complexity Analysis
- **Time Complexity:** Provide a formal mathematical proof or derivation of the time complexity using asymptotic notation ($O$, $\\Omega$, $\\Theta$). Explain the recurrence or summation representing the work done.
- **Space Complexity:** Provide a formal derivation of the space complexity (auxiliary and total space).

Write in a professional, scientific style suitable for math and computer science students at the university level. Use LaTeX for all mathematical terms, variables, and formulas. Do not include markdown code block syntax wrapping the entire document—just return the raw markdown content.
"""
    return call_gemini(prompt)

def main():
    if not API_KEY:
        print("ERROR: GEMINI_API_KEY environment variable is not set. Please set it before running this script.")
        sys.exit(1)
        
    start_time = time.time()
    
    # 1. Find all algorithm files
    algo_files = glob.glob('docs/algorithms/**/*.md', recursive=True)
    algo_files = [f for f in algo_files if 'README' not in f and '_template' not in f and not f.endswith('_de.md')]
    
    print(f"Found {len(algo_files)} algorithms in the workspace.")
    
    to_generate = []
    for file in algo_files:
        parts = os.path.normpath(file).split(os.sep)
        category = parts[2]
        filename = parts[3]
        math_file = os.path.join('docs', 'mathematical', category, filename)
        
        needs_gen = True
        if os.path.exists(math_file):
            with open(math_file, 'r', encoding='utf-8') as f:
                content = f.read()
            if not is_boilerplate(content):
                needs_gen = False
                
        if needs_gen:
            to_generate.append((file, math_file, category))
            
    total_to_gen = len(to_generate)
    print(f"Identified {total_to_gen} files that need mathematical specifications.")
    
    if total_to_gen == 0:
        print("All mathematical specification files are already customized! Nothing to do.")
        return
        
    success = 0
    failure = 0
    
    # Sequential generation to strictly respect Gemini free tier rate limits (15 RPM)
    # 4.5 seconds sleep between requests ensures we stay safely under 15 RPM
    delay = 4.5
    
    for i, (algo_file, math_file, category) in enumerate(to_generate):
        print(f"[{i+1}/{total_to_gen}] Processing: {algo_file}")
        try:
            with open(algo_file, 'r', encoding='utf-8') as f:
                algo_content = f.read()
                
            name_match = re.match(r'^#\s*(.+)$', algo_content.splitlines()[0])
            algo_name = name_match.group(1) if name_match else os.path.basename(algo_file)
            
            # Generate the specification
            spec_content = generate_math_spec(algo_name, category, algo_content)
            
            # Ensure target directory exists
            os.makedirs(os.path.dirname(math_file), exist_ok=True)
            
            # Write specification
            with open(math_file, 'w', encoding='utf-8') as f:
                f.write(spec_content)
                
            success += 1
            print(f"[{i+1}/{total_to_gen}] Success -> {math_file}")
            
            # Rate limit sleep
            time.sleep(delay)
            
        except Exception as e:
            print(f"[{i+1}/{total_to_gen}] Failed: {algo_file} - Error: {e}")
            failure += 1
            time.sleep(10)
            
    print("\n--- Summary ---")
    print(f"Total processed: {success + failure}")
    print(f"Successful: {success}")
    print(f"Failed: {failure}")
    print(f"Total time elapsed: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
