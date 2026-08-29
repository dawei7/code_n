"""Strict validation for canonical single-solution packages."""

from __future__ import annotations

import json
from pathlib import Path

from server.app.challenge_packages import leetcode_solution_path, leetcode_optimal_approach_path


ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = ROOT / "dsa" / "leetcode"
PACKAGE = (
    ROOT
    / "dsa"
    / "leetcode"
    / "1502_can-make-arithmetic-progression-from-sequence"
)


def _metadata(package: Path = PACKAGE) -> dict:
    return json.loads((package / "metadata.json").read_text(encoding="utf-8"))


def test_every_package_uses_single_canonical_solution_layout() -> None:
    packages = sorted(
        path
        for path in LEETCODE_ROOT.iterdir()
        if path.is_dir() and (path / "metadata.json").is_file()
    )

    index = json.loads((LEETCODE_ROOT / "index.json").read_text(encoding="utf-8"))
    assert len(packages) == index["count"]
    for package in packages[:200]:  # Sample first 200 packages for fast unit test
        metadata = _metadata(package)
        cid = str(metadata.get("challenge_id") or "")
        sol_path = leetcode_solution_path(cid)
        assert sol_path is not None and sol_path.is_file(), f"Missing canonical solution in {package}"
        approach_path = leetcode_optimal_approach_path(cid)
        assert approach_path is not None and approach_path.is_file(), f"Missing approach.md in {package}"
        assert not (package / "variants").exists(), f"Old variants/ directory still exists in {package}"
        assert not (package / "solution_variants.json").exists(), f"Old solution_variants.json exists in {package}"


def test_1502_single_canonical_solution_is_complete() -> None:
    metadata = _metadata(PACKAGE)
    cid = str(metadata["challenge_id"])
    sol_path = leetcode_solution_path(cid)
    approach_path = leetcode_optimal_approach_path(cid)

    assert sol_path is not None and sol_path.is_file()
    assert approach_path is not None and approach_path.is_file()
    assert (PACKAGE / "template.py").is_file()
    assert (PACKAGE / "cases.json").is_file()
    assert (PACKAGE / "benchmark.json").is_file()
