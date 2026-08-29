"""Canonical challenge package paths.

LeetCode is stored as one folder per challenge under the DSA root. The numeric
prefix is zero-padded to four digits so filesystem and GitHub ordering match
frontend-ID order:

``dsa/leetcode/<frontend_id:04d>_<slug>/``
    ``metadata.json``
    ``doc.md`` (legacy document or compatibility anchor)
    ``reference/`` (optional section-authored document)
        ``description.md``
        ``contract.md``
        ``examples.md``
        ``constraints.md``
        ``follow_up.md`` (optional source-native section)
    ``source_fidelity.json`` (optional reviewed structure and factual evidence)
    ``cases.json``
    ``benchmark.json``
    ``complexity_certificate.json``
    ``guided_example.md`` (optional)
    ``solutions/solve.py`` for Python or ``solutions/<language>.<ext>`` for
    other app-local languages
    ``solution_variants.json`` (optional)
    ``variants/<variant>/approach.md`` (optional)
    ``variants/<variant>/solutions/solve.py`` for Python or
    ``variants/<variant>/solutions/<language>.<ext>`` for other languages

These packages are the sole source for challenge metadata and artifacts.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from engine.complexity_certificates import (
    ComplexityCertificateStatus,
    validate_complexity_certificate,
)
from engine.languages import app_solution_filename, language_extension, normalize_language
from engine.solution_variants import SolutionVariantStatus, validate_solution_variants
from server.app.config import EULER_ROOT, LEETCODE_ROOT


LEETCODE_ID_PREFIX = "lc_"
EULER_ID_PREFIX = "euler_"
LEETCODE_PACKAGE_ID_WIDTH = 4
LEETCODE_REFERENCE_REQUIRED_SECTIONS = (
    "description.md",
    "contract.md",
    "examples.md",
    "constraints.md",
)
LEETCODE_SOURCE_SECTION_ID = re.compile(r"^[a-z][a-z0-9_]*$")
LEETCODE_MONOLITHIC_DESCRIPTION_HEADING = re.compile(
    r"^###\s+1\.\s+Description\s*$",
    flags=re.MULTILINE,
)


def is_leetcode_id(challenge_id: str) -> bool:
    return challenge_id.startswith(LEETCODE_ID_PREFIX)


def is_euler_id(challenge_id: str) -> bool:
    return challenge_id.startswith(EULER_ID_PREFIX)


def leetcode_frontend_id(challenge_id: str) -> str:
    return challenge_id.removeprefix(LEETCODE_ID_PREFIX)


def euler_frontend_id(challenge_id: str) -> str:
    return challenge_id.removeprefix(EULER_ID_PREFIX)


@lru_cache(maxsize=1)
def _euler_packages_by_frontend_id() -> dict[str, Path]:
    if not EULER_ROOT.is_dir():
        return {}
    mapping: dict[str, Path] = {}
    for entry in EULER_ROOT.iterdir():
        if entry.is_dir():
            prefix = entry.name.split("_")[0]
            mapping[prefix] = entry
            stripped = prefix.lstrip("0") or "0"
            mapping[stripped] = entry
    return mapping


def euler_package_dir(challenge_id: str) -> Path | None:
    if not is_euler_id(challenge_id):
        return None
    frontend_id = euler_frontend_id(challenge_id)
    mapping = _euler_packages_by_frontend_id()
    padded = frontend_id.zfill(4)
    return mapping.get(padded) or mapping.get(frontend_id) or mapping.get(frontend_id.lstrip("0") or "0")


def _safe_slug(value: str) -> str:
    lowered = value.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-") or "challenge"


@lru_cache(maxsize=1)
def leetcode_index() -> dict[str, Any]:
    path = LEETCODE_ROOT / "index.json"
    if not path.is_file():
        return {"questions": []}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"questions": []}
    questions = payload.get("questions")
    if not isinstance(questions, list):
        return {"questions": []}
    return payload


@lru_cache(maxsize=1)
def leetcode_questions_by_frontend_id() -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for raw in leetcode_index().get("questions", []):
        if not isinstance(raw, dict):
            continue
        frontend_id = str(raw.get("frontend_id") or "")
        if frontend_id:
            result[frontend_id] = raw
    return result


def leetcode_question(challenge_id: str) -> dict[str, Any] | None:
    return leetcode_questions_by_frontend_id().get(leetcode_frontend_id(challenge_id))


def _leetcode_problem_name(challenge_id: str, *, pad_frontend_id: bool) -> str | None:
    frontend_id = leetcode_frontend_id(challenge_id)
    question = leetcode_question(challenge_id)
    slug = ""
    if question is not None:
        slug = str(question.get("slug") or question.get("title_slug") or "")
    if not slug:
        return None
    directory_id = (
        frontend_id.zfill(LEETCODE_PACKAGE_ID_WIDTH)
        if pad_frontend_id
        else frontend_id
    )
    return f"{directory_id}_{_safe_slug(slug)}"


def leetcode_package_name(challenge_id: str) -> str | None:
    """Return the zero-padded canonical resource-package name."""
    return _leetcode_problem_name(challenge_id, pad_frontend_id=True)


def leetcode_user_package_name(challenge_id: str) -> str | None:
    """Return the stable, unpadded package name used by existing user data."""
    return _leetcode_problem_name(challenge_id, pad_frontend_id=False)


def leetcode_package_dir(challenge_id: str) -> Path | None:
    if is_euler_id(challenge_id):
        return euler_package_dir(challenge_id)
    name = leetcode_package_name(challenge_id)
    if name is None:
        return None
    return LEETCODE_ROOT / name


def leetcode_metadata_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "metadata.json"


@lru_cache(maxsize=4096)
def leetcode_metadata(challenge_id: str) -> dict[str, Any]:
    path = leetcode_metadata_path(challenge_id)
    if path is None or not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def leetcode_supported_languages(challenge_id: str) -> list[str]:
    languages = leetcode_metadata(challenge_id).get("supported_languages")
    if not isinstance(languages, list):
        return []
    return [str(language) for language in languages if isinstance(language, str)]


def leetcode_runnable_in_coden(challenge_id: str) -> bool:
    metadata = leetcode_metadata(challenge_id)
    if "runnable_in_coden" not in metadata:
        return True
    return bool(metadata.get("runnable_in_coden"))


def _reviewed_source_section_files(package_dir: Path) -> tuple[str, ...] | None:
    manifest_path = package_dir / "source_fidelity.json"
    if not manifest_path.is_file():
        return None
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    structure = manifest.get("structure") if isinstance(manifest, dict) else None
    review = manifest.get("review") if isinstance(manifest, dict) else None
    sections = structure.get("sections") if isinstance(structure, dict) else None
    if not isinstance(review, dict) or review.get("status") != "verified":
        return None
    if not isinstance(sections, list) or not sections:
        return None
    constraint_count = structure.get("constraint_count")
    section_ids = [str(section) for section in sections]
    if (
        len(section_ids) != len(set(section_ids))
        or not all(LEETCODE_SOURCE_SECTION_ID.fullmatch(section) for section in section_ids)
        or not all(section in section_ids for section in ("description", "examples"))
        or not isinstance(constraint_count, int)
        or constraint_count < 0
        or (constraint_count > 0 and "constraints" not in section_ids)
    ):
        return None
    filenames: list[str] = []
    for section in section_ids:
        filenames.append(f"{section}.md")
        if section == "description":
            filenames.append("contract.md")
    return tuple(filenames)


def _reference_section_paths(package_dir: Path) -> tuple[Path, ...] | None:
    reference_dir = package_dir / "reference"
    reviewed_files = _reviewed_source_section_files(package_dir)
    if reviewed_files is not None:
        reviewed_paths = tuple(reference_dir / filename for filename in reviewed_files)
        return reviewed_paths if all(path.is_file() for path in reviewed_paths) else None

    section_paths = tuple(
        reference_dir / filename
        for filename in LEETCODE_REFERENCE_REQUIRED_SECTIONS
    )
    if all(path.is_file() for path in section_paths):
        return section_paths

    # The current reference corpus stores the complete problem statement in
    # one numbered description document. Treat that file as the canonical
    # source instead of falling back to ``doc.md``: many migrated packages keep
    # only a compatibility comment in the latter.
    monolithic_path = reference_dir / "description.md"
    if monolithic_path.is_file():
        try:
            monolithic = monolithic_path.read_text(encoding="utf-8")
        except OSError:
            return None
        if LEETCODE_MONOLITHIC_DESCRIPTION_HEADING.search(monolithic):
            return (monolithic_path,)
    return None


def _markdown_table_value(value: object) -> str:
    return str(value).strip().replace("|", "\\|")


def _reference_primary_language_name(metadata: dict[str, Any]) -> str:
    configured_language = str(metadata.get("primary_language") or "").strip().lower()
    if not configured_language:
        category = str(metadata.get("category") or "").strip().lower()
        configured_language = {
            "database": "sql",
            "shell": "bash",
            "javascript": "javascript",
        }.get(category, "python")
    try:
        primary_language = normalize_language(configured_language)
    except ValueError:
        primary_language = "python"
    language_name = {
        "python": "Python",
        "javascript": "JavaScript",
        "sql": "SQL",
        "bash": "Bash",
    }.get(primary_language, "Python")
    return language_name


def _normalize_legacy_reference_header(markdown: str, metadata: dict[str, Any]) -> str:
    language_name = _reference_primary_language_name(metadata)
    return re.sub(
        r"^\|\s*Supported Languages?\s*\|.*\|\s*$",
        f"| Supported Language | {language_name} |",
        markdown,
        flags=re.MULTILINE,
    )


def _reference_header(metadata: dict[str, Any]) -> str:
    topics = metadata.get("topics")
    topic_names = [
        str(topic.get("name") or "").strip()
        for topic in topics
        if isinstance(topic, dict) and str(topic.get("name") or "").strip()
    ] if isinstance(topics, list) else []
    language_name = _reference_primary_language_name(metadata)
    url = str(metadata.get("url") or "").strip()
    contest_source = str(metadata.get("contest_source") or "").strip()
    contest_problem_index = str(metadata.get("contest_problem_index") or "").strip()
    source_name = "Project Euler" if metadata.get("source") == "euler" else "LeetCode"
    link_label = "Project Euler" if metadata.get("source") == "euler" else "LeetCode"
    fields = (
        ("Source", source_name),
        ("Frontend ID", metadata.get("frontend_id") or ""),
        ("Difficulty", metadata.get("difficulty") or ""),
        ("Contest Source", contest_source),
        ("Contest Problem", contest_problem_index if contest_source else ""),
        ("Category", metadata.get("category_title") or metadata.get("category") or ""),
        ("Topics", ", ".join(topic_names)),
        ("Supported Language", language_name),
        ("Official Link", f"[{link_label}]({url})" if url else ""),
    )

    rows = [
        f"| {_markdown_table_value(label)} | {_markdown_table_value(value)} |"
        for label, value in fields
        if str(value).strip()
    ]
    title = _markdown_table_value(metadata.get("title") or "Untitled LeetCode Problem")
    return "\n".join((f"# {title}", "", "| Field | Value |", "|---|---|", *rows))


def leetcode_doc_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    canonical_sections = _reference_section_paths(package_dir)
    if canonical_sections is not None:
        return canonical_sections[0]
    doc = package_dir / "doc.md"
    return doc if doc.is_file() else None


def leetcode_doc_markdown(challenge_id: str) -> str | None:
    """Return one composed section document or a legacy monolithic document."""

    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    canonical_sections = _reference_section_paths(package_dir)
    if canonical_sections is not None:
        return "\n\n".join(
            (_reference_header(leetcode_metadata(challenge_id)),)
            + tuple(path.read_text(encoding="utf-8").strip() for path in canonical_sections)
        ) + "\n"
    doc = package_dir / "doc.md"
    return (
        _normalize_legacy_reference_header(
            doc.read_text(encoding="utf-8"),
            leetcode_metadata(challenge_id),
        )
        if doc.is_file()
        else None
    )


def leetcode_guided_example_path(challenge_id: str) -> Path | None:
    """Return the optional package-authored guided-example document."""
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "guided_example.md"


def leetcode_optimal_approach_path(challenge_id: str) -> Path | None:
    """Return the canonical Optimal branch's authored approach path."""
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is not None:
        top_approach = package_dir / "approach.md"
        if top_approach.is_file():
            return top_approach
    variant_dir = _variant_directory(challenge_id, "optimal")
    return None if variant_dir is None else variant_dir / "approach.md"


def leetcode_editorial_markdown(challenge_id: str) -> str:
    """Return the package's monolithic editorial without rewriting it."""

    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return ""
    editorial = package_dir / "reference" / "editorial.md"
    if editorial.is_file():
        try:
            return editorial.read_text(encoding="utf-8")
        except OSError:
            pass

    top_approach = package_dir / "approach.md"
    if top_approach.is_file():
        try:
            text = top_approach.read_text(encoding="utf-8")
            metadata = leetcode_metadata(challenge_id)
            primary_lang = metadata.get("primary_language", "python")
            sol_path = leetcode_solution_path(challenge_id, primary_lang)
            if sol_path and sol_path.is_file():
                lang_tag = "python" if primary_lang == "python" else primary_lang
                text += f"\n\n## Reference Implementation\n\n```{lang_tag}\n" + sol_path.read_text(encoding="utf-8") + "\n```\n"
            return text
        except OSError:
            pass

    optimal_dir = package_dir / "variants" / "optimal"
    approach = optimal_dir / "approach.md"
    if approach.is_file():
        try:
            text = approach.read_text(encoding="utf-8")
            sol_py = optimal_dir / "solutions" / "solution.py"
            if sol_py.is_file():
                text += "\n\n## Reference Implementation\n\n```python\n" + sol_py.read_text(encoding="utf-8") + "\n```\n"
            return text
        except OSError:
            pass

    return ""


def leetcode_solution_variants_manifest_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    config = leetcode_metadata(challenge_id).get("solution_variants")
    if not isinstance(config, dict):
        return None
    raw_relative = str(config.get("manifest") or "").strip()
    if not raw_relative:
        return None
    relative = Path(raw_relative)
    if relative.is_absolute():
        return None
    target = (package_dir / relative).resolve()
    try:
        target.relative_to(package_dir.resolve())
    except ValueError:
        return None
    return target


@lru_cache(maxsize=4096)
def _raw_solution_variants(challenge_id: str) -> dict[str, Any]:
    path = leetcode_solution_variants_manifest_path(challenge_id)
    if path is None or not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _variant_row(challenge_id: str, variant_id: str | None = None) -> dict[str, Any] | None:
    payload = _raw_solution_variants(challenge_id)
    selected = variant_id or str(payload.get("default_variant") or "")
    rows = payload.get("variants")
    if not selected or not isinstance(rows, list):
        return None
    return next(
        (
            item
            for item in rows
            if isinstance(item, dict) and str(item.get("id") or "") == selected
        ),
        None,
    )


def _variant_directory(challenge_id: str, variant_id: str | None = None) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    row = _variant_row(challenge_id, variant_id)
    if row is None:
        return None
    raw_relative = str(row.get("directory") or "").strip()
    if not raw_relative:
        return None
    relative = Path(raw_relative)
    if relative.is_absolute():
        return None
    target = (package_dir / relative).resolve()
    try:
        target.relative_to(package_dir.resolve())
    except ValueError:
        return None
    return target


def leetcode_solution_variant_complexity(
    challenge_id: str,
    variant_id: str | None = None,
) -> tuple[str, str]:
    """Return the selected branch's authored time and space bounds."""

    row = _variant_row(challenge_id, variant_id)
    if row is not None:
        return (
            str(row.get("time_complexity") or "").strip(),
            str(row.get("space_complexity") or "").strip(),
        )

    approach_path = leetcode_optimal_approach_path(challenge_id)
    if approach_path is not None and approach_path.is_file():
        try:
            content = approach_path.read_text(encoding="utf-8")
            time_m = re.search(r"-\s*\*\*Time [Cc]omplexity(?:\:|\*\*:?)\s*\$?((?:O|\\Theta|\\Omega|[A-Za-z]+)\([^\)\n]+\))", content)
            if not time_m:
                time_m = re.search(r"-\s*\*\*Time [Cc]omplexity(?:\:|\*\*:?)\s*\$?([^$.\n*]+?)\$?(?:\.|\*\*|$)", content)
            
            space_m = re.search(r"-\s*\*\*(?:Auxiliary )?Space [Cc]omplexity(?:\:|\*\*:?)\s*\$?((?:O|\\Theta|\\Omega|[A-Za-z]+)\([^\)\n]+\))", content)
            if not space_m:
                space_m = re.search(r"-\s*\*\*(?:Auxiliary )?Space [Cc]omplexity(?:\:|\*\*:?)\s*\$?([^$.\n*]+?)\$?(?:\.|\*\*|$)", content)
                
            time_str = time_m.group(1).strip() if time_m else ""
            space_str = space_m.group(1).strip() if space_m else ""
            if time_str or space_str:
                return time_str, space_str
        except OSError:
            pass

    return "", ""


def leetcode_solution_variants_status(challenge_id: str) -> SolutionVariantStatus:
    path = leetcode_solution_variants_manifest_path(challenge_id)
    if path is None:
        return SolutionVariantStatus(complete=False, errors=("solution variants are not configured",))
    return validate_solution_variants(
        path,
        metadata=leetcode_metadata(challenge_id),
        expected_challenge_id=challenge_id,
    )


def leetcode_variant_solution_path(
    challenge_id: str,
    variant_id: str,
    language: str | None = "python",
) -> Path | None:
    if variant_id in ("optimal", "canonical", ""):
        sol = leetcode_solution_path(challenge_id, language)
        if sol is not None and sol.is_file():
            return sol
    variant_dir = _variant_directory(challenge_id, variant_id)
    if variant_dir is None:
        return leetcode_solution_path(challenge_id, language)
    language_id = normalize_language(language)
    ext = language_extension(language_id)
    path = variant_dir / f"solution.{ext}"
    if path.exists():
        return path
    nested_path = variant_dir / "solutions" / f"solution.{ext}"
    if nested_path.exists():
        return nested_path
    for legacy_name in [f"leetcode.{ext}", "leetcode_sqlite.sql", "leetcode.sql", "solve.py"]:
        legacy_path = variant_dir / "solutions" / legacy_name
        if legacy_path.exists():
            return legacy_path
    return path


def leetcode_solution_path(challenge_id: str, language: str | None = None) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    if language is None:
        meta = leetcode_metadata(challenge_id)
        language = meta.get("primary_language")
        if not language:
            for cand in [package_dir / "solution.py", package_dir / "solution.sql", package_dir / "solution.js", package_dir / "solution.sh"]:
                if cand.is_file():
                    return cand
            return package_dir / "solution.py"

    language_id = normalize_language(language)
    ext = language_extension(language_id)
    path = package_dir / f"solution.{ext}"
    if path.is_file():
        return path
    nested_path = package_dir / "solutions" / f"solution.{ext}"
    if nested_path.is_file():
        return nested_path

    # Legacy fallback to variant directory
    default_variant = _variant_directory(challenge_id)
    if default_variant is not None:
        variant_path = default_variant / f"solution.{ext}"
        if variant_path.is_file():
            return variant_path
        variant_nested = default_variant / "solutions" / f"solution.{ext}"
        if variant_nested.is_file():
            return variant_nested
        for legacy_name in [f"leetcode.{ext}", "leetcode_sqlite.sql", "leetcode.sql", "solve.py"]:
            legacy_path = default_variant / "solutions" / legacy_name
            if legacy_path.is_file() and legacy_path.name.endswith(f".{ext}"):
                return legacy_path

    return None


def leetcode_template_path(challenge_id: str, language: str | None = "python") -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    language_id = normalize_language(language)
    ext = language_extension(language_id)
    template_file = package_dir / f"template.{ext}"
    if template_file.is_file():
        return template_file
    return None


def leetcode_cases_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "cases.json"


def leetcode_benchmark_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "benchmark.json"


def leetcode_complexity_certificate_path(challenge_id: str) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    return None if package_dir is None else package_dir / "complexity_certificate.json"


def leetcode_complexity_certificate(challenge_id: str) -> dict[str, Any]:
    path = leetcode_complexity_certificate_path(challenge_id)
    if path is None or not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    status = validate_complexity_certificate(payload, expected_challenge_id=challenge_id)
    return payload if status.complete and isinstance(payload, dict) else {}


def leetcode_complexity_certificate_status(challenge_id: str) -> ComplexityCertificateStatus:
    path = leetcode_complexity_certificate_path(challenge_id)
    if path is None or not path.is_file():
        return ComplexityCertificateStatus(complete=False, errors=("certificate is missing",))
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return ComplexityCertificateStatus(complete=False, errors=(f"invalid JSON: {exc}",))
    return validate_complexity_certificate(payload, expected_challenge_id=challenge_id)


def leetcode_submission_manifest_path(
    challenge_id: str,
    variant_id: str | None = None,
) -> Path | None:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        return None
    root_candidate = package_dir / "submission.json"
    if root_candidate.is_file():
        return root_candidate
    candidate = package_dir / "variants" / (variant_id or "optimal") / "submission.json"
    return candidate if candidate.is_file() else None


def iter_leetcode_package_dirs() -> list[Path]:
    if not LEETCODE_ROOT.is_dir():
        return []
    return sorted(
        path
        for path in LEETCODE_ROOT.iterdir()
        if path.is_dir() and (path / "metadata.json").is_file()
    )


def iter_leetcode_doc_paths() -> list[Path]:
    paths: list[Path] = []
    for package_dir in iter_leetcode_package_dirs():
        challenge_id = leetcode_package_id(package_dir)
        doc = leetcode_doc_path(challenge_id) if challenge_id else None
        if doc is not None:
            paths.append(doc)
    return paths


def leetcode_package_id(package_dir: Path) -> str | None:
    metadata_path = package_dir / "metadata.json"
    if metadata_path.is_file():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            metadata = {}
        challenge_id = str(metadata.get("challenge_id") or "")
        if challenge_id:
            return challenge_id
    if package_dir.parent == EULER_ROOT or package_dir.parent.name == "euler":
        match = re.match(r"^(\d+)_", package_dir.name)
        if match:
            return f"euler_{int(match.group(1))}"
    match = re.match(r"^(\d+)_", package_dir.name)
    if match:
        return f"lc_{int(match.group(1))}"
    return None
