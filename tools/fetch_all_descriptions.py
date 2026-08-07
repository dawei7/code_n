import json
import re
import sys
import time
import html
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin
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

query = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    titleSlug
    isPaidOnly
    content
  }
}
"""

def download_url(url: str) -> bytes | None:
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.read()
        except Exception:
            if attempt == 2:
                return None
            time.sleep(0.3 * (attempt + 1))
    return None

def sanitize_filename(name: str) -> str:
    clean = re.sub(r'[^\w\.\-]', '_', name)
    return clean[:120]

def html_to_markdown_description(html_content: str, ref_dir: Path, slug: str) -> str:
    if not html_content:
        return ""

    images_dir = ref_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    base_url = f"https://leetcode.com/problems/{slug}/"

    text = html_content
    text = text.replace("&nbsp;", " ").replace("\xa0", " ")

    # 1. Slideshow JSONs: !\?!../Documents/...!\?!
    def replace_doc_json(match):
        raw_path = match.group(1).strip()
        json_rel_url = raw_path.split(":")[0]
        full_json_url = urljoin(base_url, json_rel_url)
        json_data_raw = download_url(full_json_url)
        if not json_data_raw:
            return match.group(0)
        try:
            doc_data = json.loads(json_data_raw.decode('utf-8'))
            timeline = doc_data.get("timeline", [])
            md_blocks = []
            doc_stem = sanitize_filename(Path(json_rel_url).stem)
            for idx, frame in enumerate(timeline):
                img_rel = frame.get("image", "")
                if not img_rel:
                    continue
                frame_full_url = urljoin(full_json_url, img_rel)
                fname_raw = Path(frame_full_url.split("?")[0]).name
                if not fname_raw:
                    fname_raw = f"frame_{idx}.png"
                local_fname = sanitize_filename(f"slideshow_{doc_stem}_{fname_raw}")
                local_file = images_dir / local_fname
                if not local_file.is_file():
                    img_bytes = download_url(frame_full_url)
                    if img_bytes:
                        local_file.write_bytes(img_bytes)
                if local_file.is_file():
                    md_blocks.append(f"![Slide {idx+1}](images/{local_fname})")
            if md_blocks:
                return "\n\n" + "\n\n".join(md_blocks) + "\n\n"
        except Exception:
            pass
        return match.group(0)

    text = re.sub(r'!\?!([^!\?]+)!\?!', replace_doc_json, text)

    # 2. Download and convert all <img> tags
    def img_replacer(match):
        attrs = match.group(1)
        src_match = re.search(r'src=["\']([^"\']+)["\']', attrs, re.IGNORECASE)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', attrs, re.IGNORECASE)
        if not src_match:
            return ""
        raw_src = src_match.group(1).strip()
        alt_text = alt_match.group(1).strip() if alt_match else ""
        
        full_url = raw_src if raw_src.startswith("http") else urljoin(base_url, raw_src)
        fname_raw = Path(full_url.split("?")[0]).name
        if not fname_raw or len(fname_raw) > 100:
            fname_raw = f"img_{abs(hash(full_url))}.png"
        local_fname = sanitize_filename(fname_raw)
        local_file = images_dir / local_fname
        
        if not local_file.is_file():
            img_bytes = download_url(full_url)
            if img_bytes:
                local_file.write_bytes(img_bytes)
        
        if local_file.is_file():
            return f"\n\n![{alt_text}](images/{local_fname})\n\n"
        return f"\n\n![{alt_text}]({full_url})\n\n"

    text = re.sub(r'<img\s+([^>]*?)>', img_replacer, text, flags=re.DOTALL | re.IGNORECASE)

    # Convert headings
    text = re.sub(r'<h1\b[^>]*>(.*?)</h1>', r'# \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h2\b[^>]*>(.*?)</h2>', r'## \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h3\b[^>]*>(.*?)</h3>', r'### \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h4\b[^>]*>(.*?)</h4>', r'#### \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert code blocks: <pre><code>...</code></pre> or <pre>...</pre>
    def pre_replacer(match):
        inner = match.group(1)
        inner = re.sub(r'</?code\b[^>]*>', '', inner, flags=re.IGNORECASE)
        cleaned = html.unescape(inner).strip()
        return f"\n\n```\n{cleaned}\n```\n\n"

    text = re.sub(r'<pre\b[^>]*>(.*?)</pre>', pre_replacer, text, flags=re.DOTALL | re.IGNORECASE)

    # Inline code <code>...</code>
    text = re.sub(r'<code\b[^>]*>(.*?)</code>', r'`\1`', text, flags=re.DOTALL | re.IGNORECASE)

    # Bold and strong
    text = re.sub(r'<(?:strong|b)\b[^>]*>(.*?)</(?:strong|b)>', r'**\1**', text, flags=re.DOTALL | re.IGNORECASE)

    # Emphasis and italic
    text = re.sub(r'<(?:em|i)\b[^>]*>(.*?)</(?:em|i)>', r'*\1*', text, flags=re.DOTALL | re.IGNORECASE)

    # Subscript and superscript
    text = re.sub(r'<sub\b[^>]*>(.*?)</sub>', r'_\1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<sup\b[^>]*>(.*?)</sup>', r'^\1', text, flags=re.DOTALL | re.IGNORECASE)

    # Paragraphs and line breaks
    text = re.sub(r'<p\b[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<br\s*/?>', r'\n', text, flags=re.IGNORECASE)

    # Lists
    def li_replacer(match):
        return f"- {match.group(1).strip()}\n"
    text = re.sub(r'<li\b[^>]*>(.*?)</li>', li_replacer, text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</?(?:ul|ol)\b[^>]*>', r'\n', text, flags=re.IGNORECASE)

    # Clean up empty images dir if no images were stored
    if images_dir.is_dir() and not any(images_dir.iterdir()):
        try:
            images_dir.rmdir()
        except Exception:
            pass

    # Clean formatting, unescape HTML entities, and add ## Description header
    lines = [line.rstrip() for line in text.splitlines()]
    result = "\n".join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result).strip()
    result = html.unescape(result)
    
    return f"## Description\n\n{result}\n"

def process_question_description(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    ref_dir.mkdir(parents=True, exist_ok=True)
    out_file = ref_dir / "description.md"
    
    data = json.dumps({'query': query, 'variables': {'titleSlug': slug}}).encode('utf-8')
    req = urllib.request.Request("https://leetcode.com/graphql", data=data, headers=headers)
    
    content_html = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                qdata = res.get('data', {}).get('question', {})
                content_html = qdata.get('content')
                break
        except Exception:
            time.sleep(0.5 * (attempt + 1))
            
    if content_html:
        md = html_to_markdown_description(content_html, ref_dir, slug)
        out_file.write_text(md, encoding='utf-8')
        return fid, slug, "description", len(md)
    else:
        placeholder = "## Description\n\nAn official LeetCode description is not available for this problem.\n"
        out_file.write_text(placeholder, encoding='utf-8')
        return fid, slug, "placeholder", len(placeholder)

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]
    
    total = len(questions)
    print(f"Starting description fetch and image download for {total} problems...")
    start_time = time.time()
    
    desc_count = 0
    placeholder_count = 0
    completed = 0
    
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(process_question_description, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, status, size = future.result()
            completed += 1
            if status == "description":
                desc_count += 1
            else:
                placeholder_count += 1
                
            if completed % 250 == 0 or completed == total:
                elapsed = time.time() - start_time
                rate = completed / elapsed
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Descriptions: {desc_count}, Placeholders: {placeholder_count} - {rate:.1f} q/s")
                
    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total Descriptions fetched & converted: {desc_count}")
    print(f"Total Placeholders written: {placeholder_count}")

if __name__ == "__main__":
    main()
