"""Batch autocomplete LeetCode shared docs and Optimal branch artifacts.

This script uses the Gemini API key from progress.json (or GEMINI_API_KEY environment variable)
to fill in scaffolded docs, approaches, complexity bounds, and Python solutions.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
import requests
import threading

REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
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
                    else:
                        print(f"Quota exhausted for the last available model {model}. Skipping file.")
                        return ""
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


def generate_prompt(doc_content: str, approach_content: str) -> str:
    return f"""You are an expert software engineer and computer science professor.
Your task is to complete one scaffolded LeetCode package's shared documentation
and its Optimal branch.

Here is the scaffolded shared markdown:
{doc_content}

Here is the scaffolded Optimal approach:
{approach_content}

Generate your response using these XML-like tags:
1. <shared_markdown>
The completed shared markdown. It must contain Goal, Function Contract, and
Examples, but must not contain Required Complexity or Approach. Replace every
placeholder with clear original text. Do not copy LeetCode word-for-word.
</shared_markdown>

2. <approach_markdown>
The completed Optimal approach. It must contain exactly these level-two
headings in order: General, Complexity detail, Alternatives and edge cases.
The last section must be a scannable bullet list.
</approach_markdown>

3. <time_complexity>
Only the plain Optimal Big-O bound, such as O(n) or O(n \\log n). Do not add
words such as expected, amortized, average, or worst-case.
</time_complexity>

4. <space_complexity>
Only the plain Optimal Big-O bound.
</space_complexity>

5. <python>
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
    """Complete the shared doc and canonical Optimal branch artifacts."""
    print(f"Processing: {doc_path.name}")
    try:
        content = doc_path.read_text(encoding="utf-8")
        package = doc_path.parent
        manifest_path = package / "solution_variants.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        variants = manifest.get("variants")
        if not isinstance(variants, list):
            raise ValueError("solution_variants.json has no variants list")
        optimal = next(
            (
                row
                for row in variants
                if isinstance(row, dict) and row.get("id") == "optimal"
            ),
            None,
        )
        if optimal is None:
            raise ValueError("solution_variants.json has no Optimal branch")
        optimal_root = package / str(optimal["directory"])
        approach_path = optimal_root / "approach.md"
        approach_content = approach_path.read_text(encoding="utf-8")
        prompt = generate_prompt(content, approach_content)
        res_text = call_gemini(prompt, api_key)

        markdown_content = extract_section(res_text, "shared_markdown")
        approach_markdown = extract_section(res_text, "approach_markdown")
        time_complexity = extract_section(res_text, "time_complexity")
        space_complexity = extract_section(res_text, "space_complexity")
        python_content = extract_section(res_text, "python")

        if not all(
            (
                markdown_content,
                approach_markdown,
                time_complexity,
                space_complexity,
                python_content,
            )
        ):
            print(f"Failed to extract sections for {doc_path.name}")
            return False
        if "### Required Complexity" in markdown_content or "<summary>Approach</summary>" in markdown_content:
            raise ValueError("shared markdown contains branch-specific sections")
        headings = re.findall(r"^##\s+(.+?)\s*$", approach_markdown, flags=re.MULTILINE)
        if headings != ["General", "Complexity detail", "Alternatives and edge cases"]:
            raise ValueError("Optimal approach headings do not match the canonical format")
        for label, bound in (
            ("time", time_complexity),
            ("space", space_complexity),
        ):
            if not re.fullmatch(r"O(?:\(.+\)|\\left\(.+\\right\))", bound):
                raise ValueError(f"{label} complexity is not a plain Big-O bound")
            if "expected" in bound.lower():
                raise ValueError(f"{label} complexity must not include expected")

        # Clean python block from any accidental markdown wraps
        python_content = re.sub(r"^```python\s*", "", python_content)
        python_content = re.sub(r"\s*```$", "", python_content)

        # Write the shared document and Optimal branch artifacts.
        doc_path.write_text(markdown_content + "\n", encoding="utf-8")
        approach_path.write_text(approach_markdown + "\n", encoding="utf-8")
        solution_path = optimal_root / "solutions" / "python.py"
        solution_path.parent.mkdir(parents=True, exist_ok=True)
        solution_path.write_text(python_content + "\n", encoding="utf-8")
        optimal["time_complexity"] = time_complexity
        optimal["space_complexity"] = space_complexity
        manifest_path.write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
        )

        print(f"Successfully completed {doc_path.name} and its Optimal branch")
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

    # Find packages with a scaffolded shared doc or Optimal approach.
    to_process: list[Path] = []
    for path in sorted(LEETCODE_ROOT.glob("*/doc.md")):
        try:
            text = path.read_text(encoding="utf-8")
            approach_path = path.parent / "variants" / "optimal" / "approach.md"
            approach_text = (
                approach_path.read_text(encoding="utf-8")
                if approach_path.is_file()
                else "TODO"
            )
            if (
                "Write an original local summary" in text
                or "TODO" in text
                or "TODO" in approach_text
            ):
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
