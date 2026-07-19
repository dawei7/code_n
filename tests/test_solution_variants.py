"""Strict validation for canonical solution branches."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from engine.solution_variants import validate_solution_variants


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


def test_every_package_uses_the_optimal_first_variant_topology() -> None:
    packages = sorted(
        path
        for path in LEETCODE_ROOT.iterdir()
        if path.is_dir() and (path / "metadata.json").is_file()
    )
    simplified_packages: list[str] = []

    index = json.loads((LEETCODE_ROOT / "index.json").read_text(encoding="utf-8"))
    assert len(packages) == index["count"]
    for package in packages:
        metadata = _metadata(package)
        assert metadata.get("solution_variants") == {
            "manifest": "solution_variants.json",
            "default": "optimal",
        }, package

        manifest = json.loads(
            (package / "solution_variants.json").read_text(encoding="utf-8")
        )
        assert manifest.get("default_variant") == "optimal", package
        variants = manifest.get("variants")
        assert isinstance(variants, list) and variants, package
        assert variants[0].get("id") == "optimal", package
        assert variants[0].get("directory") == "variants/optimal", package
        for variant in variants:
            for field in ("time_complexity", "space_complexity"):
                bound = str(variant.get(field) or "")
                assert re.match(r"^O(?:\(|\\left\()", bound), (package, field, bound)
                assert "expected" not in bound.lower(), (package, field, bound)
            if variant.get("kind") == "simplified":
                simplified_packages.append(package.name)

        shared_doc = (package / "doc.md").read_text(encoding="utf-8")
        assert "### Required Complexity" not in shared_doc, package
        assert "<summary>Approach</summary>" not in shared_doc, package
        assert not (package / "solutions").exists(), package
        assert not (package / "submission.json").exists(), package

    assert simplified_packages == [PACKAGE.name]


def test_1502_solution_variants_are_complete_and_elo_eligible() -> None:
    status = validate_solution_variants(
        PACKAGE / "solution_variants.json",
        metadata=_metadata(),
        expected_challenge_id="lc_1502",
    )

    assert status.complete, status.errors
    assert status.default_variant == "optimal"
    assert [variant.id for variant in status.variants] == ["optimal", "simplified"]
    assert [variant.kind for variant in status.variants] == ["optimal", "simplified"]
    assert status.effective_elo == 1154.828067979
    assert status.elo_source == "elo_rating"
    assert status.simplified_elo_ceiling == 1500
    assert all(variant.submission_status == "verified" for variant in status.variants)
    assert all(variant.verified_submission_id for variant in status.variants)


def test_simplified_branch_rejects_an_effective_elo_above_the_ceiling() -> None:
    metadata = _metadata()
    metadata["elo_rating"] = 1500.01

    status = validate_solution_variants(
        PACKAGE / "solution_variants.json",
        metadata=metadata,
        expected_challenge_id="lc_1502",
    )

    assert not status.complete
    assert any("exceeds 1500.00" in error for error in status.errors)


def test_candidate_branch_is_not_publishable(tmp_path: Path) -> None:
    package = tmp_path / PACKAGE.name
    shutil.copytree(PACKAGE, package)
    submission_path = package / "variants" / "simplified" / "submission.json"
    submission = json.loads(submission_path.read_text(encoding="utf-8"))
    submission.update(
        status="candidate",
        verified_submission_id="",
        verified_at="",
    )
    submission_path.write_text(json.dumps(submission, indent=2) + "\n", encoding="utf-8")

    status = validate_solution_variants(
        package / "solution_variants.json",
        metadata=_metadata(package),
        expected_challenge_id="lc_1502",
    )

    assert not status.complete
    assert any("must be remotely verified" in error for error in status.errors)
    assert status.variants[1].submission_status == "candidate"
