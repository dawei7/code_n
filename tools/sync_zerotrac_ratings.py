"""Sync optional ZeroTrac contest Elo ratings into the canonical dataset.

ZeroTrac does not rate every LeetCode problem.  This tool therefore writes a
separate, sparse mapping under ``dsa/leetcode/_meta``.  Runtime code joins the
mapping to canonical packages by numeric LeetCode frontend id.  The companion
``ratings.txt`` source also supplies the originating contest and problem index;
those values are mirrored into every canonical metadata record when available.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import os
import re
import tempfile
import urllib.request
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
LEETCODE_ROOT = REPO_ROOT / "dsa" / "leetcode"
INDEX_PATH = LEETCODE_ROOT / "index.json"
OUTPUT_PATH = LEETCODE_ROOT / "_meta" / "zerotrac-ratings.json"
LICENSE_PATH = LEETCODE_ROOT / "_meta" / "zerotrac-LICENSE.txt"
SOURCE_REPOSITORY = "https://github.com/zerotrac/leetcode_problem_rating"
DATA_URL = f"{SOURCE_REPOSITORY}/raw/main/data.json"
LICENSE_URL = f"{SOURCE_REPOSITORY}/raw/main/LICENSE"
COMMITS_URL = "https://api.github.com/repos/zerotrac/leetcode_problem_rating/commits?path=data.json&per_page=1"
RATINGS_COMMITS_URL = (
    "https://api.github.com/repos/zerotrac/leetcode_problem_rating/commits"
    "?path=ratings.txt&per_page=1"
)
FROZEN_REVISION = "a99138e145f303597b85290519aaf3d219b3a3e7"
FROZEN_RATINGS_URL = f"{SOURCE_REPOSITORY}/raw/{FROZEN_REVISION}/ratings.txt"
CONTEST_FIELDS = ("contest_source", "contest_slug", "contest_problem_index")
LEGACY_CONTEST_REPOSITORY = "https://github.com/Abhishekvaish/leetcode-contest-problems-list"
LEGACY_CONTEST_DATA_URL = f"{LEGACY_CONTEST_REPOSITORY}/raw/master/README.md"
LEGACY_CONTEST_COMMITS_URL = (
    "https://api.github.com/repos/Abhishekvaish/leetcode-contest-problems-list/commits"
    "?path=README.md&per_page=1"
)
USER_AGENT = "cOde(n) ZeroTrac rating sync"


def _request(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def _request_json(url: str) -> Any:
    return json.loads(_request(url).decode("utf-8"))


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)


def _load_json_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read JSON object {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected a JSON object in {path}")
    return payload


def _canonical_slugs() -> dict[str, str]:
    payload = _load_json_object(INDEX_PATH)
    return {
        str(question["frontend_id"]): str(question["slug"])
        for question in payload.get("questions", [])
        if isinstance(question, dict) and question.get("frontend_id") and question.get("slug")
    }


def _contest_label(contest_slug: str) -> str:
    match = re.fullmatch(r"(weekly|biweekly)-contest-(\d+)", contest_slug)
    if not match:
        raise RuntimeError(f"Unsupported ZeroTrac contest slug: {contest_slug!r}")
    contest_kind, contest_number = match.groups()
    prefix = "Weekly" if contest_kind == "weekly" else "Biweekly"
    return f"{prefix} Contest {int(contest_number)}"


def parse_contest_sources(
    text: str,
    *,
    canonical_slugs: dict[str, str],
    expected_ratings: dict[str, float],
) -> dict[str, dict[str, str]]:
    """Parse and identity-check ZeroTrac's tab-separated contest provenance."""
    reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff")), delimiter="\t")
    expected_columns = {
        "Rating",
        "ID",
        "Title",
        "Title ZH",
        "Title Slug",
        "Contest Slug",
        "Problem Index",
    }
    if set(reader.fieldnames or []) != expected_columns:
        raise RuntimeError(
            "ZeroTrac ratings.txt columns changed; review the source before syncing"
        )

    sources: dict[str, dict[str, str]] = {}
    for row_number, row in enumerate(reader, start=2):
        frontend_id = str(row.get("ID") or "").strip()
        source_slug = str(row.get("Title Slug") or "").strip()
        contest_slug = str(row.get("Contest Slug") or "").strip()
        problem_index = str(row.get("Problem Index") or "").strip()
        raw_rating = str(row.get("Rating") or "").strip()
        if not frontend_id.isdigit() or not re.fullmatch(r"Q[1-9]\d*", problem_index):
            raise RuntimeError(f"Invalid ZeroTrac ratings.txt row {row_number}: {row!r}")
        try:
            rating = float(raw_rating)
        except ValueError as exc:
            raise RuntimeError(
                f"Invalid ZeroTrac rating on row {row_number}: {raw_rating!r}"
            ) from exc
        if not math.isfinite(rating):
            raise RuntimeError(f"Non-finite ZeroTrac rating on row {row_number}")
        if frontend_id in sources:
            raise RuntimeError(f"Duplicate ZeroTrac ratings.txt frontend id: {frontend_id}")

        canonical_slug = canonical_slugs.get(frontend_id)
        expected_rating = expected_ratings.get(frontend_id)
        if canonical_slug is None or expected_rating is None:
            raise RuntimeError(
                f"ZeroTrac ratings.txt frontend id {frontend_id} is absent from the frozen snapshot"
            )
        if canonical_slug != source_slug:
            raise RuntimeError(
                f"ZeroTrac identity mismatch for {frontend_id}: "
                f"{source_slug!r} != {canonical_slug!r}"
            )
        if not math.isclose(rating, expected_rating, rel_tol=0.0, abs_tol=1e-9):
            raise RuntimeError(
                f"ZeroTrac rating mismatch for {frontend_id}: {rating} != {expected_rating}"
            )

        sources[frontend_id] = {
            "contest_source": _contest_label(contest_slug),
            "contest_slug": contest_slug,
            "contest_problem_index": problem_index,
        }

    source_ids = set(sources)
    expected_ids = set(expected_ratings)
    if source_ids != expected_ids:
        missing = sorted(expected_ids - source_ids, key=int)
        extra = sorted(source_ids - expected_ids, key=int)
        raise RuntimeError(
            "ZeroTrac ratings.txt does not match the rating snapshot: "
            f"missing={missing[:10]}, extra={extra[:10]}"
        )
    return dict(sorted(sources.items(), key=lambda item: int(item[0])))


def _with_contest_fields(
    payload: dict[str, Any],
    source: dict[str, str] | None,
) -> dict[str, Any]:
    values = {
        field: source.get(field) if source is not None else None
        for field in CONTEST_FIELDS
    }
    result: dict[str, Any] = {}
    inserted = False
    for key, value in payload.items():
        if key in CONTEST_FIELDS:
            continue
        result[key] = value
        if key == "estimated_elo_rating":
            result.update(values)
            inserted = True
    if not inserted:
        result.update(values)
    return result


def _mirror_contest_sources(
    contest_sources: dict[str, dict[str, str]],
) -> dict[str, int]:
    index_payload = _load_json_object(INDEX_PATH)
    questions = index_payload.get("questions")
    if not isinstance(questions, list) or not questions:
        raise RuntimeError(f"{INDEX_PATH} has no canonical question list")

    updated_questions: list[dict[str, Any]] = []
    package_writes: list[tuple[Path, dict[str, Any]]] = []
    seen_ids: set[str] = set()
    for raw_question in questions:
        if not isinstance(raw_question, dict):
            raise RuntimeError(f"{INDEX_PATH} contains a non-object question")
        frontend_id = str(raw_question.get("frontend_id") or "")
        slug = str(raw_question.get("slug") or "")
        if not frontend_id.isdigit() or not slug or frontend_id in seen_ids:
            raise RuntimeError(f"Invalid canonical question identity: {raw_question!r}")
        seen_ids.add(frontend_id)
        source = contest_sources.get(frontend_id)
        updated_questions.append(_with_contest_fields(raw_question, source))

        package_path = LEETCODE_ROOT / f"{int(frontend_id):04d}_{slug}" / "metadata.json"
        package = _load_json_object(package_path)
        if (
            str(package.get("frontend_id") or "") != frontend_id
            or str(package.get("slug") or "") != slug
        ):
            raise RuntimeError(f"Package identity mismatch: {package_path}")
        updated_package = _with_contest_fields(package, source)
        if updated_package != package:
            package_writes.append((package_path, updated_package))

    unknown_sources = sorted(set(contest_sources) - seen_ids, key=int)
    if unknown_sources:
        raise RuntimeError(
            f"Contest provenance contains non-canonical frontend ids: {unknown_sources[:10]}"
        )

    updated_index = dict(index_payload)
    updated_index["questions"] = updated_questions
    updated_index["count"] = len(updated_questions)
    _atomic_write(INDEX_PATH, json.dumps(updated_index, indent=2, ensure_ascii=False) + "\n")
    for path, payload in package_writes:
        _atomic_write(path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return {
        "canonical": len(updated_questions),
        "matched": len(contest_sources),
        "changed_packages": len(package_writes),
    }


def _with_snapshot_contest_sources(
    payload: dict[str, Any],
    contest_sources: dict[str, dict[str, str]],
    *,
    revision: str,
) -> dict[str, Any]:
    result = dict(payload)
    result["contest_source_url"] = (
        f"{SOURCE_REPOSITORY}/blob/{revision}/ratings.txt"
    )
    result["contest_source_count"] = len(contest_sources)
    result["contest_sources"] = contest_sources
    return result


def sync_frozen_contest_provenance() -> dict[str, Any]:
    """Add contest provenance without refreshing any frozen rating or Elo value."""
    payload = _load_json_object(OUTPUT_PATH)
    revision = str(payload.get("upstream_revision") or "")
    if revision != FROZEN_REVISION:
        raise RuntimeError(
            f"Local ZeroTrac revision {revision!r} is not the frozen revision {FROZEN_REVISION}"
        )
    raw_ratings = payload.get("ratings")
    if not isinstance(raw_ratings, dict):
        raise RuntimeError(f"{OUTPUT_PATH} has no ratings mapping")
    ratings = {
        str(frontend_id): float(rating)
        for frontend_id, rating in raw_ratings.items()
        if isinstance(rating, (int, float)) and math.isfinite(float(rating))
    }
    if len(ratings) != len(raw_ratings):
        raise RuntimeError(f"{OUTPUT_PATH} contains invalid ratings")

    contest_sources = parse_contest_sources(
        _request(FROZEN_RATINGS_URL).decode("utf-8"),
        canonical_slugs=_canonical_slugs(),
        expected_ratings=ratings,
    )
    updated_payload = _with_snapshot_contest_sources(
        payload,
        contest_sources,
        revision=revision,
    )
    mirror_result = _mirror_contest_sources(contest_sources)
    _atomic_write(
        OUTPUT_PATH,
        json.dumps(updated_payload, indent=2, ensure_ascii=False) + "\n",
    )
    return {**mirror_result, "upstream_revision": revision}


def verify_contest_provenance() -> dict[str, int]:
    """Verify the sparse snapshot, canonical index, and every package mirror."""
    snapshot = _load_json_object(OUTPUT_PATH)
    raw_sources = snapshot.get("contest_sources")
    if not isinstance(raw_sources, dict):
        raise RuntimeError(f"{OUTPUT_PATH} has no contest_sources mapping")
    contest_sources = {
        str(frontend_id): source
        for frontend_id, source in raw_sources.items()
        if isinstance(source, dict)
    }
    if len(contest_sources) != len(raw_sources):
        raise RuntimeError(f"{OUTPUT_PATH} contains invalid contest provenance")

    index_payload = _load_json_object(INDEX_PATH)
    questions = index_payload.get("questions")
    if not isinstance(questions, list):
        raise RuntimeError(f"{INDEX_PATH} has no canonical question list")
    for question in questions:
        if not isinstance(question, dict):
            raise RuntimeError(f"{INDEX_PATH} contains a non-object question")
        frontend_id = str(question.get("frontend_id") or "")
        slug = str(question.get("slug") or "")
        source = contest_sources.get(frontend_id)
        expected = {
            field: source.get(field) if source is not None else None
            for field in CONTEST_FIELDS
        }
        actual = {field: question.get(field) for field in CONTEST_FIELDS}
        if actual != expected:
            raise RuntimeError(f"Index contest provenance mismatch for {frontend_id}")
        package_path = LEETCODE_ROOT / f"{int(frontend_id):04d}_{slug}" / "metadata.json"
        package = _load_json_object(package_path)
        package_actual = {field: package.get(field) for field in CONTEST_FIELDS}
        if package_actual != expected:
            raise RuntimeError(f"Package contest provenance mismatch for {frontend_id}")
    return {"canonical": len(questions), "matched": len(contest_sources)}


def _legacy_weekly_contests(canonical_slugs: dict[str, str]) -> dict[str, int]:
    """Resolve the fixed Weekly Contest 1-62 membership by canonical slug.

    The historical source calls the first event ``Warm Up Contest``.  It is
    the event ZeroTrac describes as the first weekly contest, so it is stored
    as contest 1 here.  Only membership facts are imported; the source's own
    numeric difficulty column is intentionally ignored.
    """
    text = _request(LEGACY_CONTEST_DATA_URL).decode("utf-8")
    slug_to_frontend_id = {slug: frontend_id for frontend_id, slug in canonical_slugs.items()}
    by_frontend_id: dict[str, int] = {}
    seen_contests: set[int] = set()
    current_contest: int | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        # Historical contests 16 and 18 were split into A/B divisions. Both
        # divisions belong to the same numbered legacy contest for fallback
        # purposes.
        weekly_match = re.fullmatch(r"\|Weekly Contest (\d+)[AB]?\|", line)
        if weekly_match:
            contest_number = int(weekly_match.group(1))
            current_contest = contest_number if 2 <= contest_number <= 62 else None
            if current_contest is not None:
                seen_contests.add(current_contest)
            continue
        if line == "|Warm Up Contest|":
            current_contest = 1
            seen_contests.add(1)
            continue
        if line.startswith("|") and not line.startswith("| ["):
            current_contest = None
            continue
        if current_contest is None:
            continue

        problem_match = re.match(r"\| \[[^]]+\]\(https://leetcode\.com/problems/([^)]+)\)\|", line)
        if not problem_match:
            continue
        slug = problem_match.group(1).strip("/")
        frontend_id = slug_to_frontend_id.get(slug)
        if frontend_id is None:
            raise RuntimeError(
                f"Legacy Weekly Contest {current_contest} slug is not canonical: {slug!r}"
            )
        if frontend_id in by_frontend_id:
            raise RuntimeError(f"Duplicate legacy contest problem: {frontend_id}")
        by_frontend_id[frontend_id] = current_contest

    expected_contests = set(range(1, 63))
    if seen_contests != expected_contests:
        missing = sorted(expected_contests - seen_contests)
        raise RuntimeError(f"Legacy contest source is incomplete; missing contests: {missing}")
    if not by_frontend_id:
        raise RuntimeError("Legacy contest source did not contain any canonical problems")
    return by_frontend_id


def sync() -> dict[str, Any]:
    raw_entries = _request_json(DATA_URL)
    if not isinstance(raw_entries, list):
        raise RuntimeError("ZeroTrac data.json must contain a JSON array")

    canonical_slugs = _canonical_slugs()
    legacy_contests = _legacy_weekly_contests(canonical_slugs)
    ratings: dict[str, float] = {}
    skipped: list[str] = []
    for entry in raw_entries:
        if not isinstance(entry, dict):
            raise RuntimeError("ZeroTrac data.json contains a non-object entry")
        frontend_id = str(entry.get("ID") or "")
        source_slug = str(entry.get("TitleSlug") or "")
        rating = entry.get("Rating")
        if not frontend_id or not isinstance(rating, (int, float)):
            raise RuntimeError(f"Invalid ZeroTrac entry: {entry!r}")
        if frontend_id in ratings:
            raise RuntimeError(f"Duplicate ZeroTrac frontend id: {frontend_id}")
        canonical_slug = canonical_slugs.get(frontend_id)
        if canonical_slug is None:
            skipped.append(frontend_id)
            continue
        if canonical_slug != source_slug:
            raise RuntimeError(
                f"ZeroTrac identity mismatch for {frontend_id}: {source_slug!r} != {canonical_slug!r}"
            )
        ratings[frontend_id] = float(rating)

    commits = _request_json(COMMITS_URL)
    if not isinstance(commits, list) or not commits:
        raise RuntimeError("Could not resolve the upstream data.json revision")
    commit = commits[0]
    revision = str(commit.get("sha") or "")
    updated_at = str(((commit.get("commit") or {}).get("committer") or {}).get("date") or "")
    if not revision or not updated_at:
        raise RuntimeError("The upstream revision response is incomplete")

    ratings_commits = _request_json(RATINGS_COMMITS_URL)
    if not isinstance(ratings_commits, list) or not ratings_commits:
        raise RuntimeError("Could not resolve the upstream ratings.txt revision")
    ratings_revision = str(ratings_commits[0].get("sha") or "")
    if ratings_revision != revision:
        raise RuntimeError(
            "ZeroTrac data.json and ratings.txt were not updated together; "
            "review the upstream change before syncing"
        )
    contest_sources = parse_contest_sources(
        _request(f"{SOURCE_REPOSITORY}/raw/{revision}/ratings.txt").decode("utf-8"),
        canonical_slugs=canonical_slugs,
        expected_ratings=ratings,
    )

    legacy_commits = _request_json(LEGACY_CONTEST_COMMITS_URL)
    if not isinstance(legacy_commits, list) or not legacy_commits:
        raise RuntimeError("Could not resolve the legacy contest source revision")
    legacy_revision = str(legacy_commits[0].get("sha") or "")
    if not legacy_revision:
        raise RuntimeError("The legacy contest source revision response is incomplete")

    license_text = _request(LICENSE_URL).decode("utf-8").strip() + "\n"
    if "MIT License" not in license_text or "Copyright (c) 2021 Shuxin Chen" not in license_text:
        raise RuntimeError("The upstream license changed; review it before syncing")

    payload = _with_snapshot_contest_sources({
        "source": "ZeroTrac LeetCode Problem Rating",
        "source_url": "https://zerotrac.github.io/leetcode_problem_rating/#/",
        "source_repository": SOURCE_REPOSITORY,
        "license": "MIT",
        "license_file": "zerotrac-LICENSE.txt",
        "upstream_revision": revision,
        "upstream_updated_at": updated_at,
        "count": len(ratings),
        "ratings": dict(sorted(ratings.items(), key=lambda item: int(item[0]))),
        "legacy_acceptance_estimate": {
            "description": (
                "Weekly Contests 1-62 have no ZeroTrac Elo. These problem ids use the "
                "former acceptance-percentile 1-10 estimate as an explicitly labelled fallback."
            ),
            "source_repository": LEGACY_CONTEST_REPOSITORY,
            "source_revision": legacy_revision,
            "count": len(legacy_contests),
            "contest_by_frontend_id": dict(
                sorted(legacy_contests.items(), key=lambda item: int(item[0]))
            ),
        },
    }, contest_sources, revision=revision)
    _atomic_write(OUTPUT_PATH, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    mirror_result = _mirror_contest_sources(contest_sources)
    _atomic_write(LICENSE_PATH, license_text)
    return {
        "upstream": len(raw_entries),
        "matched": len(ratings),
        "contest_sources": len(contest_sources),
        "canonical": mirror_result["canonical"],
        "changed_packages": mirror_result["changed_packages"],
        "legacy": len(legacy_contests),
        "skipped": skipped,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument(
        "--contest-provenance-only",
        action="store_true",
        help=(
            "Add contest provenance from the pinned frozen ratings.txt without "
            "refreshing ZeroTrac ratings, estimates, or LeetCode metadata."
        ),
    )
    modes.add_argument(
        "--verify-contest-provenance",
        action="store_true",
        help="Verify the contest provenance snapshot, index, and package mirrors.",
    )
    args = parser.parse_args(argv)
    if args.verify_contest_provenance:
        result = verify_contest_provenance()
        print(
            f"Verified contest provenance for {result['matched']} of "
            f"{result['canonical']} canonical problems."
        )
        return 0
    if args.contest_provenance_only:
        result = sync_frozen_contest_provenance()
        print(
            f"Added frozen contest provenance for {result['matched']} of "
            f"{result['canonical']} canonical problems "
            f"({result['changed_packages']} package files changed)."
        )
        return 0

    result = sync()
    print(
        f"Synced {result['matched']} ZeroTrac ratings "
        f"and {result['contest_sources']} contest sources "
        f"and {result['legacy']} legacy-contest fallbacks "
        f"({result['upstream']} upstream, {len(result['skipped'])} unmatched)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
