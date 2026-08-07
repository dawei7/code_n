import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import threading

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
COOKIE_PATH = LEETCODE_ROOT / "_local" / ".leetcode_cookie"

if not COOKIE_PATH.is_file():
    raise RuntimeError(f"Cookie file not found at {COOKIE_PATH}")

cookie_str = COOKIE_PATH.read_text().strip()
csrf_token = ""
for part in cookie_str.split(";"):
    if "csrftoken=" in part:
        csrf_token = part.split("=")[1].strip()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie': cookie_str,
    'x-csrftoken': csrf_token,
    'Content-Type': 'application/json',
    'Referer': 'https://leetcode.com/'
}

solution_query = """
query questionSolutionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    titleSlug
    solution {
      id
      title
      content
    }
  }
}
"""

playground_cache = {}
cache_lock = threading.Lock()

def get_playground_code(playground_id: str) -> str:
    with cache_lock:
        if playground_id in playground_cache:
            return playground_cache[playground_id]

    gql_query = f"""
    query fetchPlayground {{
      allPlaygroundCodes(uuid: "{playground_id}") {{
        code
        langSlug
      }}
    }}
    """
    data = json.dumps({'query': gql_query}).encode('utf-8')
    req = urllib.request.Request("https://leetcode.com/graphql", data=data, headers=headers)
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                codes = res.get('data', {}).get('allPlaygroundCodes', [])
                if not codes:
                    with cache_lock:
                        playground_cache[playground_id] = ""
                    return ""
                
                # Select language according to user rule:
                # Priority: Python3 > Javascript > Bash > Postgres > first language
                selected = None
                for target_langs in [
                    ['python3', 'python'],
                    ['javascript', 'typescript', 'js', 'ts'],
                    ['bash', 'shell', 'sh'],
                    ['postgres', 'postgresql', 'mysql', 'sql']
                ]:
                    for item in codes:
                        if item.get('langSlug', '').lower() in target_langs:
                            selected = item
                            break
                    if selected:
                        break
                
                if not selected:
                    selected = codes[0]
                
                lang_slug = selected.get('langSlug', '').lower()
                code_text = selected.get('code', '')
                
                lang_map = {
                    'python3': 'python',
                    'python': 'python',
                    'javascript': 'javascript',
                    'typescript': 'javascript',
                    'js': 'javascript',
                    'ts': 'javascript',
                    'bash': 'bash',
                    'shell': 'bash',
                    'sh': 'bash',
                    'postgres': 'sql',
                    'postgresql': 'sql',
                    'mysql': 'sql',
                    'sql': 'sql',
                    'cpp': 'cpp',
                    'java': 'java',
                    'c': 'c',
                    'csharp': 'csharp',
                    'cs': 'csharp',
                    'golang': 'go',
                    'go': 'go',
                    'ruby': 'ruby',
                    'swift': 'swift',
                    'kotlin': 'kotlin',
                    'scala': 'scala',
                    'rust': 'rust',
                }
                md_lang = lang_map.get(lang_slug, lang_slug)
                formatted = f"\n```{md_lang}\n{code_text}\n```\n"
                with cache_lock:
                    playground_cache[playground_id] = formatted
                return formatted
        except Exception as e:
            time.sleep(0.5 * (attempt + 1))

    with cache_lock:
        playground_cache[playground_id] = ""
    return ""

def process_editorial_content(content: str) -> str:
    pattern = r'<iframe\b[^>]*?(?:src=["\']https?://leetcode\.com/playground/([a-zA-Z0-9]+)|name=["\']([a-zA-Z0-9]+)["\'])[^>]*?>\s*(?:</iframe>)?'
    
    def replacer(match):
        pid = match.group(1) or match.group(2)
        if pid:
            code_block = get_playground_code(pid)
            if code_block:
                return code_block
        return match.group(0)

    processed = re.sub(pattern, replacer, content)
    return processed

def process_question(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    ref_dir.mkdir(parents=True, exist_ok=True)
    out_file = ref_dir / "editorial.md"
    
    data = json.dumps({'query': solution_query, 'variables': {'titleSlug': slug}}).encode('utf-8')
    req = urllib.request.Request("https://leetcode.com/graphql", data=data, headers=headers)
    
    sol = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                sol = res.get('data', {}).get('question', {}).get('solution')
                break
        except Exception as e:
            time.sleep(0.5 * (attempt + 1))
            
    if sol and sol.get('content'):
        raw_content = sol['content']
        processed_content = process_editorial_content(raw_content)
        out_file.write_text(processed_content, encoding='utf-8')
        return fid, slug, "editorial", len(processed_content)
    else:
        placeholder = "# Editorial\n\nAn official LeetCode editorial is not available for this problem.\n"
        out_file.write_text(placeholder, encoding='utf-8')
        return fid, slug, "placeholder", len(placeholder)

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]
    
    total = len(questions)
    print(f"Starting editorial fetch for {total} problems...")
    start_time = time.time()
    
    editorial_count = 0
    placeholder_count = 0
    completed = 0
    
    with ThreadPoolExecutor(max_workers=12) as executor:
        future_to_q = {executor.submit(process_question, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, status, size = future.result()
            completed += 1
            if status == "editorial":
                editorial_count += 1
            else:
                placeholder_count += 1
                
            if completed % 250 == 0 or completed == total:
                elapsed = time.time() - start_time
                rate = completed / elapsed
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Editorials: {editorial_count}, Placeholders: {placeholder_count} - {rate:.1f} q/s")
                
    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total Editorials fetched: {editorial_count}")
    print(f"Total Placeholders written: {placeholder_count}")

if __name__ == "__main__":
    main()
