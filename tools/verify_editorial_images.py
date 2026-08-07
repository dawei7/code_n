import json
import re
from pathlib import Path

LEETCODE_ROOT = Path("dsa/leetcode")
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

total_questions = len(questions)
editorials_with_local_images = 0
total_local_images = 0
unresolved_external_urls = []
missing_local_file_references = []

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    ref_dir = LEETCODE_ROOT / folder_name / "reference"
    ed_file = ref_dir / "editorial.md"
    images_dir = ref_dir / "images"
    
    if not ed_file.is_file():
        continue
        
    content = ed_file.read_text(encoding="utf-8")
    if "An official LeetCode editorial is not available for this problem" in content:
        continue
        
    # Find all image links in editorial.md
    md_imgs = re.findall(r'!\[.*?\]\((.*?)\)', content)
    html_imgs = re.findall(r'<img\s+[^>]*?src=["\']([^"\']+)["\']', content)
    all_imgs = md_imgs + html_imgs
    
    has_local = False
    for img_ref in all_imgs:
        clean_ref = img_ref.split()[0].strip()
        if clean_ref.startswith("images/"):
            has_local = True
            fname = clean_ref[len("images/"):]
            target_file = images_dir / fname
            if not target_file.is_file():
                missing_local_file_references.append((folder_name, clean_ref))
        elif clean_ref.startswith("http://") or clean_ref.startswith("https://") or "leetcode.com" in clean_ref:
            unresolved_external_urls.append((folder_name, clean_ref))
            
    if has_local:
        editorials_with_local_images += 1
        
    if images_dir.is_dir():
        total_local_images += len(list(images_dir.iterdir()))

print("=== EDITORIAL IMAGES AUDIT REPORT ===")
print(f"Total problems audited: {total_questions}")
print(f"Editorials with local image galleries: {editorials_with_local_images}")
print(f"Total local image files saved across corpus: {total_local_images}")
print(f"Broken / missing local image references: {len(missing_local_file_references)}")
print(f"Unresolved external image URLs remaining: {len(unresolved_external_urls)}")

if missing_local_file_references:
    print("\nSample broken references:", missing_local_file_references[:10])
if unresolved_external_urls:
    print("\nSample unresolved URLs:", unresolved_external_urls[:10])
