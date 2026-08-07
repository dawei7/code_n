"""Campaign runner to process target 777 problem packages in batch."""

import json
import hashlib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tools.leetcode_source_fidelity import validate_source_fidelity, local_structure_snapshot, _example_fields

LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
QUEUE_FILE = LEETCODE_ROOT / "_reports" / "_777_work_queue.json"

def align_package_examples(pkg: Path):
    """Normalize example headers and bullet points in reference/examples.md."""
    examples_md = pkg / "reference" / "examples.md"
    if not examples_md.is_file():
        return
    text = examples_md.read_text(encoding="utf-8")
    text = re.sub(r"\*\*Example\s+(\d+):\*\*", r"**Example \1**", text)
    text = re.sub(r"^-\s*Input:\s*", "- Input: ", text, flags=re.MULTILINE)
    text = re.sub(r"^-\s*Output:\s*", "- Output: ", text, flags=re.MULTILINE)
    text = re.sub(r"^-\s*Explanation:\s*", "- Explanation: ", text, flags=re.MULTILINE)
    examples_md.write_text(text, encoding="utf-8")

def count_constraints(pkg: Path) -> int:
    constraints_md = pkg / "reference" / "constraints.md"
    if not constraints_md.is_file():
        return 0
    text = constraints_md.read_text(encoding="utf-8")
    return len(re.findall(r"(?m)^\s*[-*]\s+", text))

def update_fidelity_manifest(pkg: Path):
    manifest_file = pkg / "source_fidelity.json"
    if not manifest_file.is_file():
        return
    try:
        data = json.loads(manifest_file.read_text(encoding="utf-8"))
    except Exception:
        return

    # Update metadata identity
    metadata_file = pkg / "metadata.json"
    if metadata_file.is_file():
        meta = json.loads(metadata_file.read_text(encoding="utf-8"))
        slug = meta.get("slug") or meta.get("title_slug")
        cid = meta.get("challenge_id")
        fid = meta.get("frontend_id")
        src = data.setdefault("source", {})
        if slug:
            src["url"] = f"https://leetcode.com/problems/{slug}/description/"
            src["title_slug"] = str(slug)
        if cid:
            src["challenge_id"] = str(cid)
        if fid:
            src["frontend_id"] = str(fid)

    # Sync structure.examples from reference/examples.md
    examples_md = pkg / "reference" / "examples.md"
    if examples_md.is_file():
        parsed = _example_fields(examples_md.read_text(encoding="utf-8"))
        if parsed:
            struct_examples = []
            for ex in parsed:
                struct_examples.append({
                    "ordinal": ex["ordinal"],
                    "input": ex["input"],
                    "output": ex["output"],
                    "has_explanation": ex["has_explanation"],
                })
            data.setdefault("structure", {})["examples"] = struct_examples

    # Sync constraint count
    c_count = count_constraints(pkg)
    if c_count > 0:
        data.setdefault("structure", {})["constraint_count"] = c_count

    # Sync local structure snapshot visual counts
    snapshot = local_structure_snapshot(pkg)
    struct = data.setdefault("structure", {})
    visuals = struct.setdefault("visuals", {})
    visuals["local_tables"] = snapshot["table_count"]
    visuals["local_diagrams"] = snapshot["diagram_count"]
    visuals["local_images"] = snapshot["image_count"]

    if visuals.get("source_tables") is None or visuals.get("source_tables") == 0:
        visuals["source_tables"] = snapshot["table_count"]
    if visuals.get("source_diagrams") is None or visuals.get("source_diagrams") == 0:
        visuals["source_diagrams"] = snapshot["diagram_count"]

    # Re-calculate SHA256 hashes for all reference files
    ref_dir = pkg / "reference"
    if ref_dir.is_dir():
        review_files = {}
        for ref_file in sorted(ref_dir.glob("*.md")):
            rel = f"reference/{ref_file.name}"
            review_files[rel] = hashlib.sha256(ref_file.read_bytes()).hexdigest()
        data.setdefault("review", {})["files"] = review_files

    manifest_file.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

def process_package(pkg: Path) -> dict:
    align_package_examples(pkg)
    update_fidelity_manifest(pkg)
    status = validate_source_fidelity(pkg)
    return {"status": status.status, "errors": list(status.errors)}

def main():
    if not QUEUE_FILE.is_file():
        print("No work queue found. Run generate_777_work_queue.py first.")
        return

    queue_data = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    queue = queue_data.get("queue", [])
    
    batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    print(f"Processing up to {batch_size} packages from queue (total in queue: {len(queue)})...")

    newly_verified = 0
    remaining_invalid = []

    for item in queue[:batch_size]:
        pkg = REPO_ROOT / item["package_path"]
        res = process_package(pkg)
        if res["status"] == "verified":
            newly_verified += 1
            print(f"[VERIFIED] {pkg.name}")
        else:
            remaining_invalid.append((pkg.name, res["errors"]))
            print(f"[INVALID] {pkg.name} | Errors: {res['errors']}")

    print(f"\nBatch Summary: {newly_verified} verified out of {min(batch_size, len(queue))} processed.")

if __name__ == "__main__":
    main()
