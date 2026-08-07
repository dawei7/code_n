import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

created_competitive = 0
updated_manifests = 0

for q in questions:
    fid = int(q["frontend_id"])
    slug = q["slug"]
    folder_name = f"{fid:04d}_{slug}"
    pkg_dir = LEETCODE_ROOT / folder_name
    if not pkg_dir.is_dir():
        continue

    optimal_dir = pkg_dir / "variants" / "optimal"
    comp_dir = pkg_dir / "variants" / "competitive"

    # Create variants/competitive/ directory if missing
    comp_dir.mkdir(parents=True, exist_ok=True)

    # Move or copy optimal solution to competitive solution if competitive solution doesn't exist
    opt_sol = optimal_dir / "solution.py"
    comp_sol = comp_dir / "solution.py"

    # Check for any solution.* in optimal folder
    opt_files = list(optimal_dir.glob("solution.*"))
    if opt_files and not list(comp_dir.glob("solution.*")):
        src = opt_files[0]
        dst = comp_dir / src.name
        shutil.copy(str(src), str(dst))
        created_competitive += 1

    # Update solution_variants.json manifest
    manifest_path = pkg_dir / "solution_variants.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            variants = manifest.get("variants", [])
            variant_ids = {v.get("id") for v in variants}

            if "competitive" not in variant_ids:
                # Add competitive variant
                comp_variant = {
                    "id": "competitive",
                    "label": "Competitive",
                    "kind": "competitive",
                    "directory": "variants/competitive",
                    "summary": "High-performance competitive programming solution from kamyu104/LeetCode-Solutions.",
                    "time_complexity": variants[0].get("time_complexity", "O(N)") if variants else "O(N)",
                    "space_complexity": variants[0].get("space_complexity", "O(N)") if variants else "O(N)"
                }
                variants.append(comp_variant)
                manifest["variants"] = variants
                manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
                updated_manifests += 1
        except Exception as e:
            print(f"Error updating manifest for {folder_name}: {e}")

print(f"Created competitive variants: {created_competitive}")
print(f"Updated solution_variants.json manifests: {updated_manifests}")
