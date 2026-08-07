import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin
import threading

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
COOKIE_PATH = LEETCODE_ROOT / "_local" / ".leetcode_cookie"

cookie_str = COOKIE_PATH.read_text().strip()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie': cookie_str,
    'Referer': 'https://leetcode.com/'
}

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

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
    # Clean filename of unsafe characters
    clean = re.sub(r'[^\w\.\-]', '_', name)
    return clean[:120]

def process_question_images(q):
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    ed_file = ref_dir / "editorial.md"
    
    if not ed_file.is_file():
        return fid, slug, 0, False

    content = ed_file.read_text(encoding="utf-8")
    if "An official LeetCode editorial is not available for this problem" in content:
        return fid, slug, 0, False

    # Check if there are any image or slideshow references
    has_slideshow = "!?!" in content
    has_md_img = "![" in content
    has_html_img = "<img" in content
    
    if not (has_slideshow or has_md_img or has_html_img):
        return fid, slug, 0, False

    images_dir = ref_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    base_editorial_url = f"https://leetcode.com/problems/{slug}/editorial/"

    images_downloaded = 0
    modified = False

    # 1. Slideshow JSONs: !\?!../Documents/...!\?!
    def replace_doc_json(match):
        nonlocal images_downloaded, modified
        raw_path = match.group(1).strip()
        json_rel_url = raw_path.split(":")[0]
        full_json_url = urljoin(base_editorial_url, json_rel_url)
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
                        images_downloaded += 1
                if local_file.is_file():
                    md_blocks.append(f"![Slide {idx+1}](images/{local_fname})")
            if md_blocks:
                modified = True
                return "\n\n" + "\n\n".join(md_blocks) + "\n\n"
        except Exception:
            pass
        return match.group(0)

    if has_slideshow:
        content = re.sub(r'!\?!([^!\?]+)!\?!', replace_doc_json, content)

    # 2. Markdown & HTML images
    def resolve_image_url(raw_url: str) -> str:
        clean_url = raw_url.split()[0].strip()
        if clean_url.startswith("http://") or clean_url.startswith("https://"):
            return clean_url
        if clean_url.startswith("/"):
            return urljoin("https://leetcode.com", clean_url)
        return urljoin(base_editorial_url, clean_url)

    def replace_md_img(match):
        nonlocal images_downloaded, modified
        alt = match.group(1)
        raw_url = match.group(2)
        if raw_url.startswith("images/"):
            return match.group(0)
        full_url = resolve_image_url(raw_url)
        fname_raw = Path(full_url.split("?")[0]).name
        if not fname_raw or len(fname_raw) > 100:
            fname_raw = f"img_{abs(hash(full_url))}.png"
        local_fname = sanitize_filename(fname_raw)
        local_file = images_dir / local_fname
        if not local_file.is_file():
            img_bytes = download_url(full_url)
            if img_bytes:
                local_file.write_bytes(img_bytes)
                images_downloaded += 1
        if local_file.is_file():
            modified = True
            return f"![{alt}](images/{local_fname})"
        return match.group(0)

    def replace_html_img(match):
        nonlocal images_downloaded, modified
        prefix = match.group(1)
        raw_url = match.group(2)
        suffix = match.group(3)
        if raw_url.startswith("images/"):
            return match.group(0)
        full_url = resolve_image_url(raw_url)
        fname_raw = Path(full_url.split("?")[0]).name
        if not fname_raw or len(fname_raw) > 100:
            fname_raw = f"img_{abs(hash(full_url))}.png"
        local_fname = sanitize_filename(fname_raw)
        local_file = images_dir / local_fname
        if not local_file.is_file():
            img_bytes = download_url(full_url)
            if img_bytes:
                local_file.write_bytes(img_bytes)
                images_downloaded += 1
        if local_file.is_file():
            modified = True
            return f'{prefix}src="images/{local_fname}"{suffix}'
        return match.group(0)

    if has_md_img:
        content = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_md_img, content)
    if has_html_img:
        content = re.sub(r'(<img\s+[^>]*?)src=["\']([^"\']+)["\']([^>]*?>)', replace_html_img, content)

    # Cleanup empty directory if no images were stored
    if images_dir.is_dir() and not any(images_dir.iterdir()):
        try:
            images_dir.rmdir()
        except Exception:
            pass
    elif modified:
        ed_file.write_text(content, encoding='utf-8')

    return fid, slug, images_downloaded, modified

def main():
    total = len(questions)
    print(f"Starting image download & linking for {total} problems...")
    start_time = time.time()
    
    total_images_saved = 0
    total_editorials_updated = 0
    completed = 0
    
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_q = {executor.submit(process_question_images, q): q for q in questions}
        for future in as_completed(future_to_q):
            fid, slug, count, modified = future.result()
            completed += 1
            total_images_saved += count
            if modified:
                total_editorials_updated += 1
                
            if completed % 250 == 0 or completed == total:
                elapsed = time.time() - start_time
                rate = completed / elapsed
                print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%) - Editorials Updated: {total_editorials_updated}, Images Saved: {total_images_saved} - {rate:.1f} q/s")
                
    elapsed = time.time() - start_time
    print(f"\nFINISHED! Processed {total} problems in {elapsed:.2f} seconds.")
    print(f"Total Editorials updated with local images: {total_editorials_updated}")
    print(f"Total Image files saved locally: {total_images_saved}")

if __name__ == "__main__":
    main()
