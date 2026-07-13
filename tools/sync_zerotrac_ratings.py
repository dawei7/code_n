"""Sync optional ZeroTrac contest Elo ratings into the canonical dataset.

ZeroTrac does not rate every LeetCode problem.  This tool therefore writes a
separate, sparse mapping under ``dsa/leetcode/_meta``.  Runtime code joins the
mapping to canonical packages by numeric LeetCode frontend id.
"""

from __future__ import annotations

import argparse
import json
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


def _canonical_slugs() -> dict[str, str]:
    payload = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return {
        str(question["frontend_id"]): str(question["slug"])
        for question in payload.get("questions", [])
        if isinstance(question, dict) and question.get("frontend_id") and question.get("slug")
    }


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

    legacy_commits = _request_json(LEGACY_CONTEST_COMMITS_URL)
    if not isinstance(legacy_commits, list) or not legacy_commits:
        raise RuntimeError("Could not resolve the legacy contest source revision")
    legacy_revision = str(legacy_commits[0].get("sha") or "")
    if not legacy_revision:
        raise RuntimeError("The legacy contest source revision response is incomplete")

    license_text = _request(LICENSE_URL).decode("utf-8").strip() + "\n"
    if "MIT License" not in license_text or "Copyright (c) 2021 Shuxin Chen" not in license_text:
        raise RuntimeError("The upstream license changed; review it before syncing")

    payload = {
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
    }
    _atomic_write(OUTPUT_PATH, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    _atomic_write(LICENSE_PATH, license_text)
    return {
        "upstream": len(raw_entries),
        "matched": len(ratings),
        "legacy": len(legacy_contests),
        "skipped": skipped,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = sync()
    print(
        f"Synced {result['matched']} ZeroTrac ratings "
        f"and {result['legacy']} legacy-contest fallbacks "
        f"({result['upstream']} upstream, {len(result['skipped'])} unmatched)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
