"""Batch autocomplete LeetCode reference docs and generate optimal python solutions.

This script uses the Gemini API key from progress.json (or GEMINI_API_KEY environment variable)
to fill in the scaffolded docs and generate matching optimal Python solutions.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
import requests
import threading

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs" / "algorithms" / "leetcode"
OPTIMAL_ROOT = REPO_ROOT / "optimal_solutions" / "leetcode"
PROGRESS_PATH = REPO_ROOT / "progress.json"

MODELS_POOL = [
    "gemini-2.5-flash",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash-lite"
]
current_model_idx = 0


def get_api_key() -> str:
    """Retrieve Gemini API key from environment or progress.json."""
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"]

    if PROGRESS_PATH.exists():
        try:
            progress = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
            active_profile = progress.get("active_profile", "Default")
            profiles = progress.get("profiles", {})
            profile_data = profiles.get(active_profile, {})
            key = profile_data.get("gemini_api_key", "")
            if key:
                return key
        except Exception as e:
            print(f"Warning: Could not read progress.json: {e}")

    return ""


def call_gemini(prompt: str, api_key: str) -> str:
    """Send prompt to Gemini API with model rotation on 429 quota failure or safety block."""
    global current_model_idx
    headers = {"Content-Type": "application/json"}
    backoff = 5.0
    retries_for_current_model = 0

    while True:
        model = MODELS_POOL[current_model_idx]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.1
            }
        }

        try:
            result = [None]
            exception = [None]
            def do_post():
                try:
                    result[0] = requests.post(url, headers=headers, json=payload, timeout=(15, 30))
                except Exception as ex:
                    exception[0] = ex

            t = threading.Thread(target=do_post)
            t.daemon = True
            t.start()
            t.join(timeout=60)

            if t.is_alive():
                raise RuntimeError("Request timed out (hard 60s limit reached)")
            if exception[0] is not None:
                raise exception[0]

            response = result[0]
            if response.status_code == 200:
                data = response.json()
                try:
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                except (KeyError, IndexError) as e:
                    print(f"Format error in response for {model} (possibly safety blocked): {e}")
                    raise RuntimeError(f"Safety blocked or invalid response structure: {response.text}")
            elif response.status_code == 429:
                # Rotate model if daily limit hit
                resp_text = response.text
                if "RESOURCE_EXHAUSTED" in resp_text or "quota" in resp_text.lower():
                    if current_model_idx < len(MODELS_POOL) - 1:
                        old_model = MODELS_POOL[current_model_idx]
                        current_model_idx += 1
                        new_model = MODELS_POOL[current_model_idx]
                        print(f"Quota exhausted for {old_model}. Falling back to {new_model}...")
                        time.sleep(2)
                        retries_for_current_model = 0
                        continue
                print(f"Rate limited (429) on {model}. Retrying in {backoff:.1f}s...")
                time.sleep(backoff)
                backoff *= 2.0
                continue
            else:
                raise RuntimeError(f"HTTP {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Error during API call on {model}: {e}")
            retries_for_current_model += 1
            if retries_for_current_model >= 3:
                # Rotate model if we failed multiple times on this model
                if current_model_idx < len(MODELS_POOL) - 1:
                    old_model = MODELS_POOL[current_model_idx]
                    current_model_idx += 1
                    new_model = MODELS_POOL[current_model_idx]
                    print(f"Failed {retries_for_current_model} times on {old_model}. Falling back to {new_model}...")
                    retries_for_current_model = 0
                    time.sleep(2)
                    continue
                else:
                    print(f"Failed {retries_for_current_model} times on the last available model {model}. Skipping file.")
                    return ""
            time.sleep(5)


def generate_prompt(doc_content: str) -> str:
    return f"""You are an expert software engineer and computer science professor.
Your task is to take a scaffolded LeetCode problem documentation (which has placeholders like "TODO" and "Write an original local summary") and complete it, plus write the optimal Python 3 solution code.

Here is the scaffolded markdown:
{doc_content}

Generate your response using two XML-like tags:
1. <markdown>
The fully completed markdown content. Replace all "TODO" sections and "Write an original local summary" placeholders with clear, high-quality, professional original descriptions, function contract, examples, base algorithms, and complexity analysis.
Do not copy LeetCode's description word-for-word. Maintain the exact markdown format, table structure, and fields.
</markdown>

2. <python>
The clean, optimal, and correct Python 3 code for the solve function.
CRITICAL: The Python code MUST be a top-level standalone function named `solve`. Do NOT wrap it in a class (such as `class Solution` or any other class), and do NOT include `self` in the function parameters. All helper functions, classes (like TreeNodes, ListNodes), or imports must be defined at the top-level. The solve function signature must define the correct parameters matching the Function Contract inputs of your completed markdown.
Do not wrap this code inside markdown code blocks (like ```python). Just output the raw code lines inside the <python> tags.
</python>
"""


def extract_section(text: str, tag: str) -> str:
    start_tag = f"<{tag}>"
    end_tag = f"</{tag}>"
    start_idx = text.find(start_tag)
    if start_idx == -1:
        return ""
    end_idx = text.find(end_tag, start_idx)
    if end_idx == -1:
        return ""
    return text[start_idx + len(start_tag):end_idx].strip()


def process_file(doc_path: Path, api_key: str) -> bool:
    """Complete markdown file and create its optimal solution python file."""
    print(f"Processing: {doc_path.name}")
    try:
        content = doc_path.read_text(encoding="utf-8")
        prompt = generate_prompt(content)
        res_text = call_gemini(prompt, api_key)
        
        markdown_content = extract_section(res_text, "markdown")
        python_content = extract_section(res_text, "python")

        if not markdown_content or not python_content:
            print(f"Failed to extract sections for {doc_path.name}")
            return False

        # Clean python block from any accidental markdown wraps
        python_content = re.sub(r"^```python\s*", "", python_content)
        python_content = re.sub(r"\s*```$", "", python_content)

        # Write markdown back
        doc_path.write_text(markdown_content + "\n", encoding="utf-8")

        # Write Python solution
        relative_path = doc_path.relative_to(DOCS_ROOT)
        solution_path = (OPTIMAL_ROOT / relative_path).with_suffix(".py")
        solution_path.parent.mkdir(parents=True, exist_ok=True)
        solution_path.write_text(python_content + "\n", encoding="utf-8")

        print(f"Successfully completed {doc_path.name} and generated {solution_path.name}")
        return True
    except Exception as e:
        print(f"Failed to process {doc_path.name}: {e}")
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5, help="Limit number of completed files (0 for no limit)")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay between API requests in seconds")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key:
        print("ERROR: Gemini API Key not found. Please set GEMINI_API_KEY environment variable or configure it in the app profiles.")
        return 1

    # Find scaffolded docs needing completion
    to_process: list[Path] = []
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        if path.name.startswith("_") or path.name == "README.md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
            if "Write an original local summary" in text or "TODO" in text:
                to_process.append(path)
        except Exception:
            pass

    print(f"Found {len(to_process)} scaffolded documents needing completion.")
    if not to_process:
        print("All LeetCode documents are already completed!")
        return 0

    if args.limit > 0:
        to_process = to_process[:args.limit]
        print(f"Limiting execution to first {args.limit} files.")

    success_count = 0
    for i, path in enumerate(to_process):
        print(f"[{i+1}/{len(to_process)}] ", end="")
        if process_file(path, api_key):
            success_count += 1
        if i < len(to_process) - 1:
            time.sleep(args.delay)

    print(f"\nCompleted: {success_count} / {len(to_process)} successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
