"""Migrate every canonical LeetCode package to solution-variant topology.

The migration is intentionally mechanical:

- shared ``doc.md`` keeps the problem statement, contract, and examples;
- Required Complexity moves into the default Optimal manifest row;
- the authored Approach moves to ``variants/optimal/approach.md``;
- root solutions and submission evidence move into ``variants/optimal/``;
- every package receives the same manifest pointer and Optimal branch.

No Simplified branch is inferred or created. Existing additional branches, such
as the reviewed LeetCode 1502 pilot, are preserved verbatim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = ROOT / "dsa" / "leetcode"
APPROACH_HEADINGS = ("General", "Complexity detail", "Alternatives and edge cases")
MANIFEST_NAME = "solution_variants.json"
VARIANT_POINTER = {"manifest": MANIFEST_NAME, "default": "optimal"}
COMPLEXITY_BOUND_RE = re.compile(r"^O(?:\(|\\left\()")

COMPLEXITY_RE = re.compile(
    r"^### Required Complexity\s*$"
    r"\s*^- \*\*Time:\*\* \$([^$]+)\$\s*$"
    r"\s*^- \*\*Space:\*\* \$([^$]+)\$\s*",
    flags=re.MULTILINE,
)
APPROACH_RE = re.compile(
    r"<details>\s*<summary>Approach</summary>\s*(.*?)\s*</details>\s*",
    flags=re.DOTALL,
)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Invalid JSON: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected a JSON object: {path}")
    return payload


def _atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.solution-variant-migration.tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def _atomic_json(path: Path, payload: dict[str, Any]) -> None:
    _atomic_text(path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _copy_verified_then_remove(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    source_hash = _sha256(source)
    if destination.exists():
        if not destination.is_file() or _sha256(destination) != source_hash:
            raise RuntimeError(f"Destination conflict: {destination}")
    else:
        shutil.copy2(source, destination)
        if _sha256(destination) != source_hash:
            raise RuntimeError(f"Hash verification failed: {source} -> {destination}")
    source.unlink()


def _ordered_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    inserted = False
    for key, value in metadata.items():
        if key == "solution_variants":
            continue
        result[key] = value
        if key == "runnable_in_coden":
            result["solution_variants"] = dict(VARIANT_POINTER)
            inserted = True
    if not inserted:
        result["solution_variants"] = dict(VARIANT_POINTER)
    return result


def _extract_doc_artifacts(text: str) -> tuple[str, str, str, str]:
    complexity_match = COMPLEXITY_RE.search(text)
    time_complexity = complexity_match.group(1).strip() if complexity_match else "O(...)"
    space_complexity = complexity_match.group(2).strip() if complexity_match else "O(...)"

    approach_match = APPROACH_RE.search(text)
    approach = ""
    if approach_match:
        approach = approach_match.group(1).strip()
        headings = tuple(
            re.findall(r"^####\s+(.+?)\s*$", approach, flags=re.MULTILINE)
        )
        if headings != APPROACH_HEADINGS:
            raise RuntimeError(f"Unexpected Approach headings: {headings}")
        approach = re.sub(
            r"^####\s+(General|Complexity detail|Alternatives and edge cases)\s*$",
            r"## \1",
            approach,
            flags=re.MULTILINE,
        ).strip() + "\n"

    shared = APPROACH_RE.sub("", text)
    shared = COMPLEXITY_RE.sub("", shared)
    return shared.rstrip() + "\n", time_complexity, space_complexity, approach


def _new_manifest(
    metadata: dict[str, Any],
    *,
    time_complexity: str,
    space_complexity: str,
) -> dict[str, Any]:
    title = str(metadata.get("title") or "this problem")
    return {
        "schema_version": 1,
        "challenge_id": str(metadata.get("challenge_id") or ""),
        "default_variant": "optimal",
        "variants": [
            {
                "id": "optimal",
                "label": "Optimal",
                "kind": "optimal",
                "directory": "variants/optimal",
                "summary": (
                    f"Uses the canonical optimal approach for {title} and meets "
                    "the required complexity bound."
                ),
                "time_complexity": time_complexity,
                "space_complexity": space_complexity,
            }
        ],
    }


def _update_existing_manifest(
    manifest: dict[str, Any],
    *,
    time_complexity: str,
    space_complexity: str,
) -> dict[str, Any]:
    rows = manifest.get("variants")
    if not isinstance(rows, list):
        raise RuntimeError("Existing solution-variant manifest has no variants list")
    optimal = next(
        (
            row
            for row in rows
            if isinstance(row, dict) and str(row.get("id") or "") == "optimal"
        ),
        None,
    )
    if optimal is None:
        raise RuntimeError("Existing solution-variant manifest has no optimal row")
    if time_complexity != "O(...)":
        optimal["time_complexity"] = time_complexity
    if space_complexity != "O(...)":
        optimal["space_complexity"] = space_complexity
    for row in rows:
        if not isinstance(row, dict):
            continue
        for field in ("time_complexity", "space_complexity"):
            value = str(row.get(field) or "")
            row[field] = re.sub(r"\s+expected\s*$", "", value).strip()
    return manifest


def _package_dirs() -> list[Path]:
    return sorted(
        path
        for path in LEETCODE_ROOT.iterdir()
        if path.is_dir() and (path / "metadata.json").is_file()
    )


def plan() -> Counter[str]:
    counts: Counter[str] = Counter()
    for package in _package_dirs():
        counts["packages"] += 1
        doc_path = package / "doc.md"
        text = doc_path.read_text(encoding="utf-8") if doc_path.is_file() else ""
        _shared, _time, _space, approach = _extract_doc_artifacts(text)
        counts["docs_with_required_complexity"] += "### Required Complexity" in text
        counts["docs_with_approach"] += bool(approach)
        counts["root_solution_files"] += sum(
            1
            for path in (package / "solutions").glob("*")
            if path.is_file()
        )
        counts["root_submissions"] += (package / "submission.json").is_file()
        counts["new_manifests"] += not (package / MANIFEST_NAME).is_file()
    return counts


def migrate_package(package: Path) -> None:
    metadata_path = package / "metadata.json"
    metadata = _load_json(metadata_path)
    doc_path = package / "doc.md"
    text = doc_path.read_text(encoding="utf-8") if doc_path.is_file() else ""
    shared, time_complexity, space_complexity, approach = _extract_doc_artifacts(text)

    manifest_path = package / MANIFEST_NAME
    if manifest_path.is_file():
        manifest = _update_existing_manifest(
            _load_json(manifest_path),
            time_complexity=time_complexity,
            space_complexity=space_complexity,
        )
    else:
        manifest = _new_manifest(
            metadata,
            time_complexity=time_complexity,
            space_complexity=space_complexity,
        )

    if approach:
        approach_path = package / "variants" / "optimal" / "approach.md"
        if approach_path.is_file():
            if approach_path.read_text(encoding="utf-8") != approach:
                raise RuntimeError(f"Approach destination conflict: {approach_path}")
        else:
            _atomic_text(approach_path, approach)

    root_solutions = package / "solutions"
    if root_solutions.is_dir():
        unexpected_directories = [
            path
            for path in root_solutions.iterdir()
            if path.is_dir() and path.name != "__pycache__"
        ]
        if unexpected_directories:
            raise RuntimeError(
                f"Unexpected solution subdirectories in {package}: {unexpected_directories}"
            )
        for source in sorted(path for path in root_solutions.iterdir() if path.is_file()):
            _copy_verified_then_remove(
                source,
                package / "variants" / "optimal" / "solutions" / source.name,
            )
        cache = root_solutions / "__pycache__"
        if cache.is_dir():
            shutil.rmtree(cache)
        if any(root_solutions.iterdir()):
            raise RuntimeError(f"Legacy solutions directory is not empty: {root_solutions}")
        root_solutions.rmdir()

    root_submission = package / "submission.json"
    if root_submission.is_file():
        _copy_verified_then_remove(
            root_submission,
            package / "variants" / "optimal" / "submission.json",
        )

    if doc_path.is_file() and shared != text:
        _atomic_text(doc_path, shared)
    _atomic_json(manifest_path, manifest)
    _atomic_json(metadata_path, _ordered_metadata(metadata))


def check() -> Counter[str]:
    failures: list[str] = []
    counts: Counter[str] = Counter()
    for package in _package_dirs():
        counts["packages"] += 1
        metadata = _load_json(package / "metadata.json")
        if metadata.get("solution_variants") != VARIANT_POINTER:
            failures.append(f"{package.name}: invalid metadata pointer")
        manifest_path = package / MANIFEST_NAME
        if not manifest_path.is_file():
            failures.append(f"{package.name}: manifest missing")
            continue
        manifest = _load_json(manifest_path)
        rows = manifest.get("variants")
        valid_rows = rows if isinstance(rows, list) else []
        optimal = next(
            (
                row
                for row in valid_rows
                if isinstance(row, dict) and row.get("id") == "optimal"
            ),
            None,
        )
        if optimal is None:
            failures.append(f"{package.name}: optimal row missing")
        else:
            for field in ("time_complexity", "space_complexity"):
                value = str(optimal.get(field) or "")
                if not COMPLEXITY_BOUND_RE.match(value) or "expected" in value.lower():
                    failures.append(f"{package.name}: invalid {field}: {value}")
        if (package / "solutions").exists():
            failures.append(f"{package.name}: legacy solutions directory remains")
        if (package / "submission.json").exists():
            failures.append(f"{package.name}: legacy submission remains")
        doc_path = package / "doc.md"
        text = doc_path.read_text(encoding="utf-8") if doc_path.is_file() else ""
        if "### Required Complexity" in text:
            failures.append(f"{package.name}: shared Required Complexity remains")
        if "<summary>Approach</summary>" in text:
            failures.append(f"{package.name}: shared Approach remains")
        approach_path = package / "variants" / "optimal" / "approach.md"
        if approach_path.is_file():
            headings = tuple(
                re.findall(
                    r"^##\s+(.+?)\s*$",
                    approach_path.read_text(encoding="utf-8"),
                    flags=re.MULTILINE,
                )
            )
            if headings != APPROACH_HEADINGS:
                failures.append(f"{package.name}: invalid optimal Approach headings")
            counts["optimal_approaches"] += 1
        if (package / "variants" / "optimal" / "solutions").is_dir():
            counts["optimal_solution_directories"] += 1
        if (package / "variants" / "optimal" / "submission.json").is_file():
            counts["optimal_submissions"] += 1
    if failures:
        preview = "\n".join(failures[:50])
        raise RuntimeError(f"{len(failures)} migration check failures:\n{preview}")
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="Apply the migration.")
    mode.add_argument("--check", action="store_true", help="Validate the migrated corpus.")
    args = parser.parse_args()

    if args.check:
        print(json.dumps(check(), indent=2, sort_keys=True))
        return 0

    migration_plan = plan()
    print(json.dumps(migration_plan, indent=2, sort_keys=True))
    if not args.apply:
        print("Dry run only. Re-run with --apply to migrate the corpus.")
        return 0

    for package in _package_dirs():
        migrate_package(package)
    print("Migration applied.")
    print(json.dumps(check(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
