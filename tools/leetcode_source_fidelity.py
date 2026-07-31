"""Validate reviewed LeetCode statement-fidelity manifests.

The manifest records facts and review evidence, not LeetCode's prose or HTML.
Missing manifests mean "unverified"; they do not make an otherwise complete
challenge package incomplete.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MANIFEST_NAME = "source_fidelity.json"
SOURCE_SECTION_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
SOURCE_SECTION_HEADINGS = {
    "description": "Description",
    "examples": "Examples",
    "constraints": "Constraints",
    "follow_up": "Follow-up",
    "clarification_for_follow_up": "Clarification for the follow-up question",
    "follow_up_example": "Follow-up Example",
    "method_read4": "Method read4",
    "definition_of_read4": "Definition of read4",
    "read4_example": "How read4 works",
    "method_read": "Method read",
    "definition_of_read": "Definition of read",
    "note": "Note",
}
REQUIRED_ASSERTIONS = (
    "semantic_coverage",
    "section_order",
    "examples",
    "example_explanations",
    "constraints",
    "visuals_and_tables",
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
EXAMPLE_HEADING_PATTERN = re.compile(
    r"(?m)^\*\*Example\s+(\d+)\*\*\s*$"
)


@dataclass(frozen=True)
class SourceFidelityStatus:
    status: str
    errors: tuple[str, ...] = ()

    @property
    def verified(self) -> bool:
        return self.status == "verified" and not self.errors


def _load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid {MANIFEST_NAME}: {exc}")
        return {}
    if not isinstance(payload, dict):
        errors.append(f"{MANIFEST_NAME} must contain a JSON object")
        return {}
    return payload


def _metadata(package: Path, errors: list[str]) -> dict[str, Any]:
    path = package / "metadata.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid metadata.json: {exc}")
        return {}
    if not isinstance(payload, dict):
        errors.append("metadata.json must contain a JSON object")
        return {}
    return payload


def _string(value: object) -> str:
    return str(value or "").strip()


def _normalize_literal(value: object) -> str:
    text = html.unescape(_string(value)).strip("`")
    normalized: list[str] = []
    quote = ""
    escaped = False
    for character in text:
        if escaped:
            normalized.append(character)
            escaped = False
            continue
        if character == "\\" and quote:
            normalized.append(character)
            escaped = True
            continue
        if character in ('"', "'"):
            if not quote:
                quote = character
            elif quote == character:
                quote = ""
            normalized.append(character)
            continue
        if character.isspace() and not quote:
            continue
        normalized.append(character)
    return "".join(normalized)


def _example_fields(markdown: str) -> list[dict[str, object]]:
    matches = list(EXAMPLE_HEADING_PATTERN.finditer(markdown))
    examples: list[dict[str, object]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        body = markdown[match.end() : end]
        fields: dict[str, object] = {"ordinal": int(match.group(1))}
        for label in ("Input", "Output"):
            value_match = re.search(
                rf"(?mi)^-\s+(?:\*\*)?{label}:(?:\*\*)?\s*(.+?)\s*$",
                body,
            )
            fields[label.lower()] = value_match.group(1) if value_match else ""
        fields["has_explanation"] = bool(
            re.search(
                r"(?mi)^-\s+(?:\*\*)?Explanation:(?:\*\*)?\s*\S",
                body,
            )
        )
        examples.append(fields)
    return examples


def _markdown_table_count(markdown: str) -> int:
    return len(
        re.findall(
            r"(?m)^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$",
            markdown,
        )
    )


def _markdown_image_count(markdown: str) -> int:
    return len(re.findall(r"!\[[^\]]*\]\([^\)]+\)|<img\b", markdown, re.IGNORECASE))


def _markdown_diagram_count(markdown: str) -> int:
    return len(re.findall(r"(?m)^```(?:text|mermaid)\s*$", markdown))


def _validate_identity(
    manifest: dict[str, Any], metadata: dict[str, Any], errors: list[str]
) -> None:
    source = manifest.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
        return
    expected = (
        ("provider", "leetcode"),
        ("challenge_id", _string(metadata.get("challenge_id"))),
        ("frontend_id", _string(metadata.get("frontend_id"))),
        ("title_slug", _string(metadata.get("slug"))),
    )
    for field, expected_value in expected:
        if _string(source.get(field)) != expected_value:
            errors.append(f"source.{field} does not match metadata.json")
    source_url = _string(source.get("url"))
    expected_slug = _string(metadata.get("slug"))
    if source_url != f"https://leetcode.com/problems/{expected_slug}/description/":
        errors.append("source.url must be the canonical LeetCode description URL")
    if not SHA256_PATTERN.fullmatch(_string(source.get("content_sha256"))):
        errors.append("source.content_sha256 must be a lowercase SHA-256 digest")
    if not DATE_PATTERN.fullmatch(_string(source.get("checked_at"))):
        errors.append("source.checked_at must use YYYY-MM-DD")
    if not isinstance(source.get("paid_only"), bool):
        errors.append("source.paid_only must be boolean")


def _validate_examples(
    package: Path, structure: dict[str, Any], errors: list[str]
) -> None:
    expected_examples = structure.get("examples")
    if not isinstance(expected_examples, list) or not expected_examples:
        errors.append("structure.examples must be a non-empty list")
        return
    examples_path = package / "reference" / "examples.md"
    if not examples_path.is_file():
        errors.append("reference/examples.md is missing")
        return
    actual_examples = _example_fields(examples_path.read_text(encoding="utf-8"))
    if len(actual_examples) != len(expected_examples):
        errors.append(
            "reference/examples.md example count does not match structure.examples"
        )
        return
    for index, (expected, actual) in enumerate(
        zip(expected_examples, actual_examples, strict=True), start=1
    ):
        if not isinstance(expected, dict):
            errors.append(f"structure.examples[{index - 1}] must be an object")
            continue
        expected_ordinal = expected.get("ordinal")
        if expected_ordinal != index or actual["ordinal"] != index:
            errors.append(f"example {index} is out of order")
        for field in ("input", "output"):
            if _normalize_literal(actual[field]) != _normalize_literal(expected.get(field)):
                errors.append(f"example {index} {field} does not match reviewed source facts")
        expected_explanation = expected.get("has_explanation")
        if not isinstance(expected_explanation, bool):
            errors.append(f"example {index} has_explanation must be boolean")
        elif actual["has_explanation"] is not expected_explanation:
            errors.append(
                f"example {index} explanation presence does not match the source"
            )


def _validate_structure(
    package: Path, manifest: dict[str, Any], errors: list[str]
) -> None:
    structure = manifest.get("structure")
    if not isinstance(structure, dict):
        errors.append("structure must be an object")
        return
    sections = structure.get("sections")
    if not isinstance(sections, list) or not sections:
        errors.append("structure.sections must be a non-empty list")
        sections = []
    if len(sections) != len(set(_string(section) for section in sections)):
        errors.append("structure.sections must not contain duplicates")
    for section in sections:
        section_id = _string(section)
        if not SOURCE_SECTION_ID_PATTERN.fullmatch(section_id):
            errors.append(f"unsupported source section: {section_id or '<empty>'}")
            continue
        filename = f"{section_id}.md"
        section_path = package / "reference" / filename
        if not section_path.is_file():
            errors.append(f"reference/{filename} is missing")
            continue
        heading = SOURCE_SECTION_HEADINGS.get(
            section_id, section_id.replace("_", " ").title()
        )
        if not section_path.read_text(encoding="utf-8").lstrip().startswith(
            f"## {heading}"
        ):
            errors.append(f"reference/{filename} must start with ## {heading}")
    for required in ("description", "examples"):
        if required not in sections:
            errors.append(f"structure.sections is missing {required}")

    constraint_count = structure.get("constraint_count")
    constraints_path = package / "reference" / "constraints.md"
    if not isinstance(constraint_count, int) or constraint_count < 0:
        errors.append("structure.constraint_count must be a non-negative integer")
    elif constraint_count > 0 and "constraints" not in sections:
        errors.append("structure.sections is missing constraints")
    elif "constraints" in sections and constraints_path.is_file():
        constraint_text = constraints_path.read_text(encoding="utf-8")
        actual_count = len(re.findall(r"(?m)^-\s+\S", constraint_text))
        if actual_count != constraint_count:
            errors.append(
                "reference/constraints.md bullet count does not match the source"
            )

    _validate_examples(package, structure, errors)

    visuals = structure.get("visuals")
    if not isinstance(visuals, dict):
        errors.append("structure.visuals must be an object")
        return
    for field in (
        "source_images",
        "source_tables",
        "source_diagrams",
        "local_images",
        "local_tables",
        "local_diagrams",
    ):
        if not isinstance(visuals.get(field), int) or visuals[field] < 0:
            errors.append(f"structure.visuals.{field} must be a non-negative integer")
    reference_dir = package / "reference"
    local_markdown = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(reference_dir.glob("*.md"))
        if path.is_file()
    )
    if isinstance(visuals.get("local_images"), int):
        if _markdown_image_count(local_markdown) != visuals["local_images"]:
            errors.append("local image count does not match structure.visuals")
    if isinstance(visuals.get("local_tables"), int):
        if _markdown_table_count(local_markdown) != visuals["local_tables"]:
            errors.append("local table count does not match structure.visuals")
    if isinstance(visuals.get("local_diagrams"), int):
        if _markdown_diagram_count(local_markdown) != visuals["local_diagrams"]:
            errors.append("local diagram count does not match structure.visuals")


def _validate_review(
    package: Path, manifest: dict[str, Any], errors: list[str]
) -> None:
    review = manifest.get("review")
    if not isinstance(review, dict):
        errors.append("review must be an object")
        return
    if review.get("status") != "verified":
        errors.append("review.status must be verified")
    assertions = review.get("assertions")
    if not isinstance(assertions, dict):
        errors.append("review.assertions must be an object")
        return
    for assertion in REQUIRED_ASSERTIONS:
        if assertions.get(assertion) is not True:
            errors.append(f"review.assertions.{assertion} must be true")
    structure = manifest.get("structure")
    sections = structure.get("sections") if isinstance(structure, dict) else []
    expected_files = {"reference/contract.md"}
    if isinstance(sections, list):
        expected_files.update(
            f"reference/{section}.md"
            for section in sections
            if isinstance(section, str) and SOURCE_SECTION_ID_PATTERN.fullmatch(section)
        )
    files = review.get("files")
    if not isinstance(files, dict):
        errors.append("review.files must be an object of reviewed local SHA-256 digests")
        return
    if set(files) != expected_files:
        errors.append("review.files must cover exactly the composed reference section files")
        return
    for relative, expected_hash in files.items():
        if not SHA256_PATTERN.fullmatch(_string(expected_hash)):
            errors.append(f"review.files.{relative} must be a lowercase SHA-256 digest")
            continue
        path = package / relative
        if not path.is_file():
            errors.append(f"reviewed file is missing: {relative}")
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            errors.append(f"reviewed file changed after verification: {relative}")


def validate_source_fidelity(package: Path) -> SourceFidelityStatus:
    manifest_path = package / MANIFEST_NAME
    if not manifest_path.is_file():
        return SourceFidelityStatus(status="unverified")

    errors: list[str] = []
    manifest = _load_json(manifest_path, errors)
    metadata = _metadata(package, errors)
    if manifest.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if manifest and metadata:
        _validate_identity(manifest, metadata, errors)
        _validate_structure(package, manifest, errors)
        _validate_review(package, manifest, errors)
    return SourceFidelityStatus(
        status="invalid" if errors else "verified",
        errors=tuple(errors),
    )


def local_structure_snapshot(package: Path) -> dict[str, object]:
    reference_dir = package / "reference"
    has_generated_metadata_table = False
    if reference_dir.is_dir():
        markdown = "\n\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(reference_dir.glob("*.md"))
            if path.is_file()
        )
    else:
        doc = package / "doc.md"
        markdown = doc.read_text(encoding="utf-8") if doc.is_file() else ""
        has_generated_metadata_table = bool(
            re.search(r"(?m)^\|\s*Field\s*\|\s*Value\s*\|\s*$", markdown)
        )
    table_count = _markdown_table_count(markdown)
    if has_generated_metadata_table and table_count:
        table_count -= 1
    return {
        "example_count": len(EXAMPLE_HEADING_PATTERN.findall(markdown)),
        "explained_example_count": len(
            re.findall(r"(?mi)^-?\s*(?:\*\*)?Explanation:(?:\*\*)?\s*\S", markdown)
        ),
        "has_constraints": bool(
            re.search(r"(?mi)^#{2,3}\s+Constraints\s*$", markdown)
        ),
        "image_count": _markdown_image_count(markdown),
        "table_count": table_count,
        "diagram_count": _markdown_diagram_count(markdown),
    }
