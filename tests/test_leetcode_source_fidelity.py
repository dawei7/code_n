from __future__ import annotations

import json
import shutil
from pathlib import Path

from tools.audit_leetcode_source_fidelity import audit
from tools.audit_leetcode_migration import _doc_status
from tools.check_leetcode_dataset import classify
from tools.leetcode_source_fidelity import _normalize_literal, validate_source_fidelity


ROOT = Path(__file__).resolve().parents[1]
TWO_SUM = ROOT / "dsa" / "leetcode" / "0001_two-sum"
COMBINE_TABLES = ROOT / "dsa" / "leetcode" / "0175_combine-two-tables"
PERSISTENT_BEHAVIOR = (
    ROOT
    / "dsa"
    / "leetcode"
    / "3832_find-users-with-persistent-behavior-patterns"
)


def test_two_sum_is_the_verified_source_fidelity_pilot() -> None:
    status = validate_source_fidelity(TWO_SUM)

    assert status.verified, status.errors


def test_first_problem_audit_separates_fidelity_from_completion() -> None:
    report = audit(1)

    assert report["scope"] == {"frontend_id_max": 1, "package_count": 1}
    assert report["counts"] == {"verified": 1, "unverified": 0, "invalid": 0}


def test_missing_manifest_is_explicitly_unverified(tmp_path: Path) -> None:
    package = tmp_path / "0001_two-sum"
    package.mkdir()

    status = validate_source_fidelity(package)

    assert status.status == "unverified"
    assert not status.verified
    assert not status.errors


def test_literal_normalization_preserves_whitespace_inside_strings() -> None:
    assert _normalize_literal('s = "   -042"') != _normalize_literal('s = " -042"')
    assert _normalize_literal("nums = [1, 2], target = 3") == _normalize_literal(
        "nums=[1,2],target=3"
    )


def test_claimed_fidelity_rejects_changed_example_facts(tmp_path: Path) -> None:
    package = tmp_path / TWO_SUM.name
    shutil.copytree(TWO_SUM, package)
    examples_path = package / "reference" / "examples.md"
    examples_path.write_text(
        examples_path.read_text(encoding="utf-8").replace(
            "target = 9", "target = 10", 1
        ),
        encoding="utf-8",
    )

    status = validate_source_fidelity(package)

    assert status.status == "invalid"
    assert any("example 1 input" in error for error in status.errors)


def test_claimed_fidelity_rejects_false_review_assertion(tmp_path: Path) -> None:
    package = tmp_path / TWO_SUM.name
    shutil.copytree(TWO_SUM, package)
    manifest_path = package / "source_fidelity.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["review"]["assertions"]["constraints"] = False
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    status = validate_source_fidelity(package)

    assert status.status == "invalid"
    assert any("assertions.constraints" in error for error in status.errors)


def test_verified_source_may_have_no_constraints_section(tmp_path: Path) -> None:
    package = tmp_path / TWO_SUM.name
    shutil.copytree(TWO_SUM, package)
    manifest_path = package / "source_fidelity.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["structure"]["sections"].remove("constraints")
    manifest["structure"]["constraint_count"] = 0
    del manifest["review"]["files"]["reference/constraints.md"]
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    (package / "reference" / "constraints.md").unlink()

    status = validate_source_fidelity(package)

    assert status.verified, status.errors


def test_completion_check_accepts_verified_source_without_constraints() -> None:
    result = classify(COMBINE_TABLES / "doc.md")

    assert result["has_required_sections"] is True
    assert result["status"] == "manual_complete"


def test_migration_audit_accepts_verified_source_without_constraints() -> None:
    result = _doc_status(PERSISTENT_BEHAVIOR / "doc.md")

    assert result["uses_reference_sections"] is True
    assert result["goal_narrative_complete"] is True
    assert result["complete"] is True


def test_claimed_fidelity_rejects_post_review_prose_changes(tmp_path: Path) -> None:
    package = tmp_path / TWO_SUM.name
    shutil.copytree(TWO_SUM, package)
    description_path = package / "reference" / "description.md"
    description_path.write_text(
        description_path.read_text(encoding="utf-8") + "\nChanged after review.\n",
        encoding="utf-8",
    )

    status = validate_source_fidelity(package)

    assert status.status == "invalid"
    assert any("changed after verification" in error for error in status.errors)
